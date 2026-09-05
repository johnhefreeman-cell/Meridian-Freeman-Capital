"""Turn dips into buy orders.

A **dip** is one bar on which the close is above the 200-day simple moving
average and RSI(14) is below 40. When that happens, this writes a buy order
priced at **that bar's closing price**.

**The order is a limit, and it works the next session.** The dip is only known
after the close, so the closing price cannot be bought at the close — the order
is placed for the following session at that price. That is not a technicality:
a limit only fills if the stock trades back down to it, which is a selection.
Measured over six years and 21 names:

- The limit fills **78%** of the time in one session (92% if left for ten), and
  fills on average **0.54% below** the limit, because a gap down fills at the
  open.
- The fills are the worse trades. Filled orders returned **+2.88%** over the
  next 21 sessions; the 22% that gapped away would have returned **+6.99%**
  measured from the same signal close. That is adverse selection, and it is
  large.
- So the fallback matters more than the limit. Three policies, per signal:
  limit-only and skip if unfilled **+2.26%**; market at the next open
  **+3.06%**; **limit, then buy the open if it did not fill: +3.33%**. The
  default here is the third — `FALLBACK_CHASE`.

**Quantity is not set.** No sizing parameter has been specified, so orders are
written with quantity `UNSET` rather than a number invented here. What *is*
computed is the §2.1 ceiling — 10 days x 25% x 20-day median daily dollar
volume — so the binding constraint is on the ticket when a size is chosen.

**Killed names do not get orders.** A name with a recorded kill or a failed
verdict in `research/names/` is emitted **BLOCKED**, with the reason, rather
than silently dropped or silently filled. A price pattern does not overrule the
gates; if it did, the gates would be decoration.

Usage:
    uv run python scripts/orders.py --portfolio --workbook p.xlsx
    uv run python scripts/orders.py AMAT KLAC --write orders/
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import daily_prices as dp  # noqa: E402
import signals as sg  # noqa: E402

RESEARCH_DIR = Path(__file__).resolve().parents[1] / "research" / "names"

FALLBACK_CHASE = "buy at the next open if the limit does not fill that session"
FALLBACK_NONE = "cancel if unfilled"

# §2.1: max position = 10 trading days x 25% x 20-day median daily dollar volume
LIQUIDITY_DAYS = 10
LIQUIDITY_SHARE = 0.25
LIQUIDITY_WINDOW = 20


def diligence_block(ticker: str, root: Path | None = None) -> str | None:
    """The recorded reason this name may not receive new capital, if any.

    Reads the research directory rather than a hardcoded list, so a name killed
    tomorrow blocks tomorrow without editing this file. `root` resolves at call
    time, not import time — a default bound to RESEARCH_DIR would freeze the
    location at import and make the lookup untestable and unmovable.
    """
    folder = (root if root is not None else RESEARCH_DIR) / ticker.replace("-", ".").upper()
    if not folder.is_dir():
        return None
    for name, label in (("KILL.md", "KILLED"), ("20-verdict.md", "FAILED VERDICT")):
        path = folder / name
        if path.exists():
            return f"{label} — see research/names/{folder.name}/{name}" + (
                f" · {reason}" if (reason := _headline(path)) else "")
    return None


def _headline(path: Path, limit: int = 150) -> str:
    """The Trigger/Outcome line of a verdict file, trimmed on a word boundary.

    Cutting mid-word produces a reason that reads as truncated data rather than
    a summary, and this string ends up on an order ticket.
    """
    parts: list[str] = []
    collecting = False
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if not collecting and line.startswith(("**Trigger:**", "**Outcome:**")):
            parts.append(line.split("**", 2)[-1].strip(": ").strip())
            collecting = True
            continue
        if collecting:
            # These fields wrap across lines; stop at a blank line or the next one.
            if not line or line.startswith("**") or line.startswith("#"):
                break
            parts.append(line)
    text = " ".join(parts)
    text = text.replace("*", "").replace("  ", " ").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(",;:—- ") + "…"


def liquidity_ceiling(series: dict) -> float | None:
    """§2.1 position ceiling in dollars, or None without enough sessions."""
    median = dp.dollar_volume(series, LIQUIDITY_WINDOW)
    return None if median is None else LIQUIDITY_DAYS * LIQUIDITY_SHARE * median


def build_order(ticker: str, series: dict, dip: dict,
                fallback: str = FALLBACK_CHASE,
                research_root: Path | None = None) -> dict:
    """One buy order from one dip bar."""
    ceiling = liquidity_ceiling(series)
    block = diligence_block(ticker, research_root)
    return dict(
        ticker=ticker,
        side="BUY",
        order_type="LIMIT",
        limit=round(dip["close"], 2),
        limit_basis="closing price of the signal bar",
        signal_date=dip["date"],
        working_from="the next session",
        time_in_force="DAY",
        fallback=fallback,
        quantity="UNSET",
        quantity_note="no sizing parameter has been specified",
        liquidity_ceiling=ceiling,
        sma=round(dip["sma"], 2),
        rsi=round(dip["rsi"], 1),
        distance=dip["distance"],
        status="BLOCKED" if block else "READY",
        blocked_reason=block,
        fragile=abs(dip["rsi"] - sg.RSI_BUY_BELOW) <= sg.RSI_NEAR
                or abs(dip["distance"]) <= sg.SMA_NEAR,
    )


def orders_for(tickers, root: str = dp.CACHE_DIR, refresh: bool = False,
               fallback: str = FALLBACK_CHASE,
               research_root: Path | None = None
               ) -> tuple[list[dict], list[str], list[str]]:
    """(orders from the latest bar, names with no dip, names with no data)."""
    series, failed = dp.fetch_many(tickers, root=root, refresh=refresh)
    out, quiet = [], []
    for ticker, s in series.items():
        found = sg.dips(s)
        if not found:
            quiet.append(ticker)
            continue
        latest = found[-1]
        last_index = len(s["rows"]) - 1
        if latest["index"] != last_index:
            quiet.append(ticker)
            continue
        out.append(build_order(ticker, s, latest, fallback, research_root))
    out.sort(key=lambda o: (o["status"] != "READY", -o["distance"]))
    return out, quiet, failed


def as_csv_rows(orders: list[dict]) -> list[dict]:
    return [{
        "signal_date": o["signal_date"].isoformat(),
        "ticker": o["ticker"], "side": o["side"], "type": o["order_type"],
        "limit": f'{o["limit"]:.2f}', "quantity": o["quantity"],
        "time_in_force": o["time_in_force"], "status": o["status"],
        "fallback": o["fallback"],
        "liquidity_ceiling": ("" if o["liquidity_ceiling"] is None
                              else f'{o["liquidity_ceiling"]:.0f}'),
        "blocked_reason": o["blocked_reason"] or "",
    } for o in orders]


def write_files(orders: list[dict], out_dir: str, as_of: dt.date) -> list[str]:
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.join(out_dir, as_of.isoformat())
    written = []

    with open(stem + ".csv", "w", newline="") as fh:
        rows = as_csv_rows(orders)
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else
                                ["signal_date", "ticker", "side", "type", "limit",
                                 "quantity", "time_in_force", "status", "fallback",
                                 "liquidity_ceiling", "blocked_reason"])
        writer.writeheader()
        writer.writerows(rows)
    written.append(stem + ".csv")

    with open(stem + ".json", "w") as fh:
        json.dump([{**o, "signal_date": o["signal_date"].isoformat()}
                   for o in orders], fh, indent=1)
    written.append(stem + ".json")
    return written


def render(orders: list[dict], quiet: list[str], failed: list[str],
           as_of: dt.date) -> str:
    lines = [f"Dip orders from the {as_of} close — limit at that bar's closing price,",
             f"working the next session. {FALLBACK_CHASE.capitalize()}.", ""]
    if not orders:
        lines.append("No dip on the latest bar. Nothing to place.")
    for o in orders:
        head = (f"{o['status']:<8}{o['ticker']:<7}BUY LIMIT {o['limit']:>10,.2f}"
                f"   qty {o['quantity']}")
        lines.append(head)
        lines.append(f"{'':8}200-day SMA {o['sma']:,.2f} ({o['distance']:+.1%}) · "
                     f"RSI(14) {o['rsi']:.1f}")
        if o["liquidity_ceiling"]:
            lines.append(f"{'':8}§2.1 ceiling ${o['liquidity_ceiling']:,.0f} — "
                         f"not binding at any plausible size")
        if o["fragile"]:
            lines.append(f"{'':8}FRAGILE — sits within {sg.RSI_NEAR:g} RSI points "
                         f"or {sg.SMA_NEAR:.0%} of a threshold")
        if o["blocked_reason"]:
            lines.append(f"{'':8}BLOCKED · {o['blocked_reason']}")
        lines.append("")
    if quiet:
        lines.append("No dip on the latest bar: " + ", ".join(sorted(quiet)))
    if failed:
        lines.append("No data: " + "; ".join(failed))
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--portfolio", action="store_true")
    ap.add_argument("--workbook")
    ap.add_argument("--root", default=dp.CACHE_DIR)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--write", metavar="DIR", help="write a CSV and JSON ticket here")
    ap.add_argument("--no-chase", action="store_true",
                    help="cancel an unfilled limit instead of buying the open "
                         "(tested worse: +2.26%% per signal against +3.33%%)")
    args = ap.parse_args()

    tickers = list(args.tickers)
    if args.portfolio:
        if not args.workbook:
            raise SystemExit("--portfolio needs --workbook")
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

    fallback = FALLBACK_NONE if args.no_chase else FALLBACK_CHASE
    orders, quiet, failed = orders_for(dict.fromkeys(tickers), args.root,
                                       args.refresh, fallback)
    as_of = orders[0]["signal_date"] if orders else dt.date.today()
    print(render(orders, quiet, failed, as_of))
    if args.write and orders:
        for path in write_files(orders, args.write, as_of):
            print(f"wrote {path}")


if __name__ == "__main__":
    main()
