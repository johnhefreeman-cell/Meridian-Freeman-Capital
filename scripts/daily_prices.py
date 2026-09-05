"""Daily closes from the public Yahoo chart endpoint, cached to disk.

The holdings workbook carries weekly closes, which is fine for a 200-day
average (40 weeks is the accepted equivalent) and **not** fine for RSI. RSI is
a ratio of average gains to average losses over N bars, so changing the bar
frequency changes the indicator itself — a 14-week RSI and a 14-day RSI are
different measurements, not two resolutions of one. Anything involving RSI
needs real daily bars, which is what this fetches.

Responses are cached under `data/daily/` so a re-run costs nothing and the
figures in a memo can be reproduced from the same bars they were written from.
Requests are spaced; the endpoint rate-limits aggressively and answers 429
without a Retry-After, so failures are retried with backoff and reported rather
than silently returning short series.

**Full bars.** Each row is `[epoch, open, high, low, close, adj, volume]`.
The open, low and volume are not decoration: a limit order's fill depends on
whether the session traded down to it, and §2.1's position ceiling is computed
from dollar volume. `adj` is split- and dividend-adjusted; `close` is as
printed. Indicators default to `adj` because a split in the window otherwise
puts a false cliff in the average, but the two are compared before any signal
is reported — see `scripts/signals.py`.

Usage:
    uv run python scripts/daily_prices.py AAPL MSFT --years 6
    uv run python scripts/daily_prices.py --portfolio --workbook p.xlsx
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.request

CACHE_DIR = os.path.join("data", "daily")
CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
REQUEST_SPACING = 1.4          # seconds between calls; the endpoint is strict
MAX_TRIES = 5

# Yahoo spells class shares with a hyphen; filings and the workbook use a dot.
SYMBOL_ALIASES = {"BRK.B": "BRK-B", "BF.B": "BF-B"}


def to_yahoo(ticker: str) -> str:
    return SYMBOL_ALIASES.get(ticker.upper(), ticker.upper())


def from_yahoo(symbol: str) -> str:
    for k, v in SYMBOL_ALIASES.items():
        if v == symbol:
            return k
    return symbol


def cache_path(ticker: str, root: str = CACHE_DIR) -> str:
    return os.path.join(root, f"{to_yahoo(ticker)}.json")


def _request(symbol: str, years: int) -> dict:
    url = CHART_URL.format(sym=symbol) + f"?range={years}y&interval=1d"
    last: Exception | None = None
    for attempt in range(MAX_TRIES):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=40) as fh:
                return json.load(fh)
        except Exception as exc:            # noqa: BLE001 - reported, not swallowed
            last = exc
            if attempt < MAX_TRIES - 1:
                time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"{symbol}: {last}")


BAR_FIELDS = ("open", "high", "low", "close", "adj", "volume")


def fetch(ticker: str, years: int = 6, root: str = CACHE_DIR,
          refresh: bool = False) -> dict:
    """{ticker, rows: [[epoch, open, high, low, close, adj, volume], ...]}.

    Cached unless `refresh`. A cache written before full bars existed is
    refetched rather than used, so a short row never silently becomes a
    missing low.
    """
    path = cache_path(ticker, root)
    if not refresh and os.path.exists(path) and os.path.getsize(path) > 2000:
        cached = json.load(open(path))
        if cached.get("rows") and len(cached["rows"][0]) == 1 + len(BAR_FIELDS):
            return cached

    symbol = to_yahoo(ticker)
    payload = _request(symbol, years)
    result = payload["chart"]["result"][0]
    stamps = result["timestamp"]
    quote = result["indicators"]["quote"][0]["close"]
    adjusted = (result.get("indicators", {}).get("adjclose") or [{}])[0].get("adjclose")

    bars = result["indicators"]["quote"][0]
    volumes = bars.get("volume") or [None] * len(stamps)
    rows = []
    for i, stamp in enumerate(stamps):
        o, h, l, close = bars["open"][i], bars["high"][i], bars["low"][i], quote[i]
        if None in (o, h, l, close):
            continue
        adj = adjusted[i] if adjusted and adjusted[i] is not None else close
        rows.append([int(stamp), round(float(o), 6), round(float(h), 6),
                     round(float(l), 6), round(float(close), 6),
                     round(float(adj), 6), int(volumes[i] or 0)])
    if not rows:
        raise RuntimeError(f"{symbol}: no usable bars returned")

    out = dict(ticker=from_yahoo(symbol), symbol=symbol, rows=rows,
               currency=result["meta"].get("currency"),
               fetched=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
    os.makedirs(root, exist_ok=True)
    with open(path, "w") as fh:
        json.dump(out, fh)
    return out


def fetch_many(tickers, years: int = 6, root: str = CACHE_DIR,
               refresh: bool = False) -> tuple[dict[str, dict], list[str]]:
    """Returns (series by ticker, failures). A failure never becomes a gap."""
    got: dict[str, dict] = {}
    failed: list[str] = []
    for i, t in enumerate(tickers):
        try:
            cached = os.path.exists(cache_path(t, root)) and not refresh
            got[t] = fetch(t, years, root, refresh)
            if not cached:
                time.sleep(REQUEST_SPACING)
        except Exception as exc:            # noqa: BLE001
            failed.append(f"{t}: {exc}")
    return got, failed


def closes(series: dict, field: str = "adj") -> tuple[list[dt.date], list[float]]:
    return dates_of(series), column(series, field)


def dates_of(series: dict) -> list[dt.date]:
    return [dt.date.fromtimestamp(r[0]) for r in series["rows"]]


def column(series: dict, field: str) -> list[float]:
    """One field across every bar. Raises on an unknown name rather than
    silently returning the wrong column."""
    if field not in BAR_FIELDS:
        raise KeyError(f"unknown bar field {field!r}; have {BAR_FIELDS}")
    idx = 1 + BAR_FIELDS.index(field)
    return [r[idx] for r in series["rows"]]


def dollar_volume(series: dict, window: int = 20) -> float | None:
    """Median daily dollar volume over the last `window` sessions.

    Uses the printed close, not the adjusted one — §2.1 asks what the tape
    actually traded, and a dividend-adjusted price understates it."""
    rows = series["rows"][-window:]
    if len(rows) < window:
        return None
    values = sorted(r[4] * r[6] for r in rows)
    mid = len(values) // 2
    return (values[mid] if len(values) % 2
            else (values[mid - 1] + values[mid]) / 2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--years", type=int, default=6)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--root", default=CACHE_DIR)
    ap.add_argument("--portfolio", action="store_true",
                    help="every single name in the holdings workbook")
    ap.add_argument("--workbook")
    args = ap.parse_args()

    tickers = list(args.tickers)
    if args.portfolio:
        if not args.workbook:
            raise SystemExit("--portfolio needs --workbook")
        import sys
        from pathlib import Path
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import openpyxl
        import portfolio_extract as px
        wb = openpyxl.load_workbook(args.workbook, data_only=True, read_only=True)
        rows = list(wb[px.HOLDINGS_SHEET].iter_rows(values_only=True))
        accounts, _ = px.account_summary(rows)
        held = px.load_holdings(rows, {a["account"] for a in accounts})
        tickers += sorted({h["ticker"] for h in held
                           if px.bucket(h["ticker"]) == "Single names"})
    if not tickers:
        raise SystemExit("name at least one ticker, or pass --portfolio")

    got, failed = fetch_many(dict.fromkeys(tickers), args.years, args.root, args.refresh)
    for t, s in got.items():
        d, v = closes(s)
        print(f"{t:<7}{len(v):>6} bars  {d[0]} to {d[-1]}  last {v[-1]:>10.2f}")
    if failed:
        print("\nfailed:")
        for f in failed:
            print("  " + f)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
