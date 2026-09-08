"""Where daily bars come from, and how to tell when two sources disagree.

The repo reads bars from a cache under `data/daily/`. This module owns what can
fill that cache and what shape the rows have, so that adding a provider does not
mean touching the indicator code.

**Row format, one per session:**

    [epoch, open, high, low, close, adj, volume]

`close` is the printed close — split-adjusted by the provider, not
dividend-adjusted — and it is what indicators run on (`signals.PRICE_FIELD`).
`adj` is the dividend-adjusted series, kept as a cross-check. A provider that
does not publish an adjusted series stores `close` in both slots, and
`adj_is_close` records that so a later comparison does not read a duplicated
column as agreement.

**Sources.**

- `yahoo` — the default, and the only one reachable from this environment
  today. No key.
- `twelvedata` — needs `TWELVE_DATA_API_KEY` **and** `api.twelvedata.com` on the
  network allowlist. Neither is present here: the host answers 403 at the proxy,
  so this path is written against the provider's documented CSV response and has
  **not been exercised end to end**. `--selftest` proves it in one call once the
  host is reachable. Until then it raises a message saying exactly that rather
  than failing obscurely.
- `import` — bars handed in as the provider's CSV, which is how Twelve Data data
  reaches this repo today: an assistant with the connector pastes the response
  into `scripts/td_import.py`. Same cache, same format.

**The partial-bar trap.** A live provider returns *today's* bar while the
session is still open. A 14-day RSI computed on a half-formed close is not a
smaller error than a wrong price — it is a signal that will not exist at the
close. Every path here drops a bar dated today unless told otherwise, and warns
when a bar's volume is a small fraction of its recent median, which is what an
in-progress session looks like.
"""

from __future__ import annotations

import csv
import datetime as dt
import io
import json
import os
import statistics as st
import urllib.request
from typing import Iterable

CACHE_DIR = os.path.join("data", "daily")
BAR_FIELDS = ("open", "high", "low", "close", "adj", "volume")

TD_BASE = "https://api.twelvedata.com"
TD_KEY_ENV = "TWELVE_DATA_API_KEY"

# Below this share of the trailing median, a bar is almost certainly a session
# still in progress rather than a quiet day.
PARTIAL_VOLUME_RATIO = 0.20


class SourceUnavailable(RuntimeError):
    """Raised when a source cannot be reached, with what to do about it."""


def _epoch(day: dt.date) -> int:
    return int(dt.datetime(day.year, day.month, day.day).timestamp())


# ---------------------------------------------------------------------------
# Twelve Data CSV — the shape this repo has actually observed
# ---------------------------------------------------------------------------

def parse_twelvedata_csv(text: str) -> list[list]:
    """Rows from a Twelve Data time_series CSV response.

    Observed shape, semicolon-delimited and **newest first**:

        datetime;open;high;low;close;volume
        2026-09-04;452.5;460.20001;443.35999;454.70999;6009400

    Twelve Data publishes no adjusted-close column on this endpoint, so `adj`
    is filled with `close` and the caller is told via `adj_is_close`.
    """
    rows: list[list] = []
    reader = csv.DictReader(io.StringIO(text.strip()), delimiter=";")
    for raw in reader:
        stamp = (raw.get("datetime") or "").strip()
        if not stamp:
            continue
        day = dt.date.fromisoformat(stamp[:10])
        try:
            o = float(raw["open"]); h = float(raw["high"])
            lo = float(raw["low"]); c = float(raw["close"])
        except (KeyError, TypeError, ValueError):
            continue
        volume = raw.get("volume")
        rows.append([_epoch(day), round(o, 6), round(h, 6), round(lo, 6),
                     round(c, 6), round(c, 6), int(float(volume or 0))])
    rows.sort(key=lambda r: r[0])          # cache is oldest-first
    return rows


def fetch_twelvedata(ticker: str, years: int = 6,
                     api_key: str | None = None) -> list[list]:
    """Daily bars from the Twelve Data REST API.

    Untested from this environment — `api.twelvedata.com` is not on the network
    allowlist and answers 403 at the proxy. Written against the CSV response
    this repo has observed through the MCP connector, and requested as CSV for
    that reason rather than JSON.
    """
    key = api_key or os.environ.get(TD_KEY_ENV)
    if not key:
        raise SourceUnavailable(
            f"{TD_KEY_ENV} is not set. Get a free key at twelvedata.com and "
            f"export it, or use --source yahoo.")

    start = (dt.date.today() - dt.timedelta(days=365 * years + 10)).isoformat()
    url = (f"{TD_BASE}/time_series?symbol={ticker}&interval=1day"
           f"&start_date={start}&format=CSV&delimiter=%3B&apikey={key}")
    try:
        req = urllib.request.Request(url, headers={"Accept": "text/csv"})
        with urllib.request.urlopen(req, timeout=40) as fh:
            text = fh.read().decode("utf-8", "replace")
    except Exception as exc:               # noqa: BLE001 — reported, not hidden
        raise SourceUnavailable(
            f"could not reach {TD_BASE}: {exc}. In this environment the host is "
            f"blocked at the proxy; add api.twelvedata.com to the network "
            f"allowlist, then run --selftest.") from exc

    if text.lstrip().startswith("{") or "code" in text[:40] and "message" in text[:120]:
        raise SourceUnavailable(f"Twelve Data returned an error: {text[:200]}")
    return parse_twelvedata_csv(text)


# ---------------------------------------------------------------------------
# Partial-bar handling
# ---------------------------------------------------------------------------

def drop_partial(rows: list[list], today: dt.date | None = None,
                 include_today: bool = False) -> tuple[list[list], list[str]]:
    """Remove a bar for a session that has not closed, and report why.

    Two independent checks, because either alone misses a case: a bar dated
    today is dropped outright, and any bar whose volume is a small fraction of
    the trailing median is flagged — that is what a live session looks like an
    hour after the open, and it is also what a half-day holiday looks like, so
    it warns rather than deletes.
    """
    notes: list[str] = []
    if not rows:
        return rows, notes
    today = today or dt.date.today()

    kept = list(rows)
    last_day = dt.date.fromtimestamp(kept[-1][0])
    if last_day >= today and not include_today:
        kept = kept[:-1]
        notes.append(f"dropped the {last_day} bar — today's session; pass "
                     f"--include-today after the close to keep it")

    if len(kept) >= 21:
        recent = [r[6] for r in kept[-21:-1] if r[6]]
        if recent:
            median = st.median(recent)
            last_volume = kept[-1][6]
            if median and last_volume and last_volume < median * PARTIAL_VOLUME_RATIO:
                notes.append(
                    f"WARNING: the {dt.date.fromtimestamp(kept[-1][0])} bar has "
                    f"{last_volume:,} shares against a median of {median:,.0f} — "
                    f"that looks like an unfinished session, not a quiet day")
    return kept, notes


# ---------------------------------------------------------------------------
# Cross-source comparison — CLAUDE.md §7: show both and say which we use
# ---------------------------------------------------------------------------

def by_date(rows: Iterable[list]) -> dict[str, list]:
    """Index bars by session date.

    Providers stamp a daily bar at different times — Yahoo at the market open in
    UTC, an imported CSV at local midnight — so the epoch is not a join key. The
    date is.
    """
    return {dt.date.fromtimestamp(r[0]).isoformat(): r for r in rows}


def compare(a: Iterable[list], b: Iterable[list],
            tolerance: float = 0.001) -> dict:
    """Bar-for-bar agreement between two sources on their common sessions."""
    left, right = by_date(a), by_date(b)
    shared = sorted(set(left) & set(right))
    diffs = []
    for day in shared:
        x, y = left[day][4], right[day][4]
        if y and abs(x / y - 1) > tolerance:
            diffs.append(dict(date=day, a=x, b=y, gap=x / y - 1))
    return dict(
        common=len(shared),
        only_a=sorted(set(left) - set(right)),
        only_b=sorted(set(right) - set(left)),
        disagreements=diffs,
        worst=max((abs(d["gap"]) for d in diffs), default=0.0),
    )


def write_cache(ticker: str, rows: list[list], root: str = CACHE_DIR,
                source: str = "twelvedata", adj_is_close: bool = True) -> str:
    os.makedirs(root, exist_ok=True)
    symbol = ticker.upper().replace(".", "-") if ticker.upper() == "BRK.B" else ticker.upper()
    path = os.path.join(root, f"{symbol}.json")
    payload = dict(ticker=ticker.upper(), symbol=symbol, rows=rows, source=source,
                   adj_is_close=adj_is_close,
                   fetched=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
    with open(path, "w") as fh:
        json.dump(payload, fh)
    return path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _load_cache(ticker: str, root: str = CACHE_DIR) -> dict | None:
    symbol = "BRK-B" if ticker.upper() == "BRK.B" else ticker.upper()
    path = os.path.join(root, f"{symbol}.json")
    return json.load(open(path)) if os.path.exists(path) else None


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker", nargs="?")
    ap.add_argument("--import-csv", metavar="PATH",
                    help="a Twelve Data time_series CSV ('-' for stdin) to load "
                         "into the cache for TICKER")
    ap.add_argument("--verify", action="store_true",
                    help="compare the CSV against the cached bars instead of "
                         "overwriting them")
    ap.add_argument("--selftest", action="store_true",
                    help="one live REST call, to prove the key and the "
                         "allowlist once api.twelvedata.com is reachable")
    ap.add_argument("--include-today", action="store_true")
    ap.add_argument("--root", default=CACHE_DIR)
    ap.add_argument("--tolerance", type=float, default=0.001)
    args = ap.parse_args()

    if args.selftest:
        try:
            rows = fetch_twelvedata(args.ticker or "AAPL", years=1)
        except SourceUnavailable as exc:
            raise SystemExit(f"Twelve Data is not usable yet:\n  {exc}")
        kept, notes = drop_partial(rows, include_today=args.include_today)
        for note in notes:
            print(note)
        last = dt.date.fromtimestamp(kept[-1][0])
        print(f"OK — {len(kept):,} bars, last completed session {last}, "
              f"close {kept[-1][4]:.2f}")
        return

    if not args.import_csv or not args.ticker:
        raise SystemExit("give a TICKER and --import-csv PATH, or --selftest")

    text = (input() if args.import_csv == "-" and False else
            open(args.import_csv).read() if args.import_csv != "-" else
            __import__("sys").stdin.read())
    rows = parse_twelvedata_csv(text)
    if not rows:
        raise SystemExit("no bars parsed — is this a Twelve Data time_series CSV?")

    kept, notes = drop_partial(rows, include_today=args.include_today)
    for note in notes:
        print(note)

    cached = _load_cache(args.ticker, args.root)
    if cached:
        report = compare(cached["rows"], kept, args.tolerance)
        print(f"\nAgainst the cached bars: {report['common']:,} common sessions, "
              f"{len(report['disagreements'])} disagree beyond "
              f"{args.tolerance:.2%} (worst {report['worst']:.3%})")
        for d in report["disagreements"][:10]:
            print(f"  {d['date']}  cached {d['a']:.4f}  incoming {d['b']:.4f}  "
                  f"{d['gap']:+.3%}")
        if report["only_b"]:
            print(f"  incoming has {len(report['only_b'])} sessions the cache "
                  f"lacks, newest {report['only_b'][-1]}")
        if report["only_a"]:
            print(f"  cache has {len(report['only_a'])} sessions the incoming "
                  f"data lacks, newest {report['only_a'][-1]}")

    if args.verify:
        print("\n--verify: nothing written.")
        return

    path = write_cache(args.ticker, kept, args.root)
    print(f"\nwrote {path} — {len(kept):,} bars, last "
          f"{dt.date.fromtimestamp(kept[-1][0])}")


if __name__ == "__main__":
    main()
