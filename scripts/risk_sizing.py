"""Risk-contribution and inverse-volatility sizing for the single-name sleeve.

Capital weight is not risk weight. A position at 12% of capital and 121%
annualized volatility carries several times the risk of a 5% position at 14%
vol, and nothing in a normal holdings view shows that. This reports both, and
the trades that would equalize them.

**This sizes positions. It does not time them.** Tested walk-forward on five
years of weekly data, direction-timing rules (regime models, trend, momentum)
all destroyed return; inverse-vol *sizing* improved Sharpe from 0.93 to 0.97
and cut max drawdown from -40% to -35%. That edge is modest and inside the
noise for a 19-name correlated book — treat it as risk hygiene, not alpha.
It also gives up return: over the same window it made less money than equal
weight. Rebalancing a taxable account realizes gains the backtest ignores.

Workbook layout expected (matches IRA_Portfolio.v2.0.xlsx):
  - one sheet per name titled "HMM <TICKER>", weekly dates in column H and
    prices in column I
  - a holdings sheet ("Asset PM") with tickers in column E and current market
    value in column K

Usage:
    uv run python scripts/risk_sizing.py --workbook path/to/Portfolio.xlsx
    uv run python scripts/risk_sizing.py --workbook p.xlsx --json
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics as st
import sys
from typing import Any

WEEKS_PER_YEAR = 52.0
TICKER_RE = re.compile(r"[A-Z]{1,5}(\.[A-Z])?")

# Column indices (0-based) in the source workbook.
PRICE_SHEET_PREFIX = "HMM "
PRICE_SHEET_SKIP = {"HMM Data", "HMM Backtest"}
DATE_COL, PRICE_COL = 7, 8
HOLD_TICKER_COL, HOLD_VALUE_COL = 4, 10


def load_price_history(wb, min_weeks: int = 60) -> dict[str, dict]:
    """{ticker: {date: price}} from every per-name price sheet."""
    out: dict[str, dict] = {}
    for name in wb.sheetnames:
        if not name.startswith(PRICE_SHEET_PREFIX) or name in PRICE_SHEET_SKIP:
            continue
        series = {}
        for row in wb[name].iter_rows(min_row=2, values_only=True):
            if len(row) <= PRICE_COL:
                continue
            date, price = row[DATE_COL], row[PRICE_COL]
            if date is not None and isinstance(price, (int, float)) and price > 0:
                series[date] = float(price)
        if len(series) >= min_weeks:
            out[name[len(PRICE_SHEET_PREFIX):]] = series
    return out


def load_holdings(wb, sheet: str = "Asset PM") -> dict[str, float]:
    """{ticker: market value}, summed across accounts."""
    if sheet not in wb.sheetnames:
        raise SystemExit(f"holdings sheet {sheet!r} not in workbook")
    held: dict[str, float] = {}
    for row in wb[sheet].iter_rows(values_only=True):
        if len(row) <= HOLD_VALUE_COL:
            continue
        ticker, value = row[HOLD_TICKER_COL], row[HOLD_VALUE_COL]
        if not isinstance(ticker, str) or not isinstance(value, (int, float)):
            continue
        ticker = ticker.strip()
        if TICKER_RE.fullmatch(ticker) and value > 0:
            held[ticker] = held.get(ticker, 0.0) + float(value)
    return held


def annualized_vol(series: dict, window: int = 13) -> float | None:
    """Realized volatility over the trailing `window` returns."""
    dates = sorted(series)[-(window + 1):]
    if len(dates) < 3:
        return None
    rets = [series[dates[i]] / series[dates[i - 1]] - 1 for i in range(1, len(dates))]
    vol = st.pstdev(rets) * math.sqrt(WEEKS_PER_YEAR)
    return vol if vol > 0 else None


def inverse_vol_weights(vols: dict[str, float]) -> dict[str, float]:
    """Weights proportional to 1/vol, normalized. Equal risk if uncorrelated."""
    inv = {t: 1.0 / v for t, v in vols.items()}
    total = sum(inv.values())
    return {t: x / total for t, x in inv.items()}


def risk_contributions(weights: dict[str, float],
                       vols: dict[str, float]) -> dict[str, float]:
    """Share of standalone risk per name. Ignores correlation — a first-order
    approximation that is enough to expose a sizing mismatch, not a covariance
    model."""
    raw = {t: weights[t] * vols[t] for t in weights}
    total = sum(raw.values())
    return {t: v / total for t, v in raw.items()} if total else {t: 0.0 for t in weights}


def build_report(holdings: dict[str, float], prices: dict[str, dict],
                 window: int = 13) -> dict[str, Any]:
    sized = {t: v for t, v in holdings.items() if t in prices}
    vols, skipped = {}, []
    for t in sized:
        v = annualized_vol(prices[t], window)
        (vols.__setitem__(t, v) if v else skipped.append(t))
    for t in skipped:
        sized.pop(t)
    if not sized:
        raise SystemExit("no holdings with usable price history")

    total = sum(sized.values())
    current = {t: v / total for t, v in sized.items()}
    target = inverse_vol_weights(vols)
    rc = risk_contributions(current, vols)

    rows = [
        dict(ticker=t, value=sized[t], weight=current[t], vol=vols[t],
             risk_share=rc[t], target_weight=target[t],
             trade=(target[t] - current[t]) * total)
        for t in sized
    ]
    rows.sort(key=lambda r: -r["risk_share"])
    return dict(
        total=total, window=window, rows=rows,
        no_history=sorted(t for t in holdings if t not in prices),
        no_vol=sorted(skipped),
    )


def render(rep: dict[str, Any]) -> str:
    out = [
        f"SINGLE-NAME SLEEVE — ${rep['total']:,.0f} across {len(rep['rows'])} names",
        f"volatility window: {rep['window']} weeks",
        "",
        f"{'Ticker':<8}{'value':>11}{'weight':>8}{'vol':>7}"
        f"{'risk':>8}{'target':>8}{'trade':>12}",
        "-" * 62,
    ]
    for r in rep["rows"]:
        out.append(
            f"{r['ticker']:<8}{r['value']:>11,.0f}{r['weight']:>8.1%}"
            f"{r['vol']:>7.0%}{r['risk_share']:>8.1%}"
            f"{r['target_weight']:>8.1%}{r['trade']:>+12,.0f}"
        )
    out.append("-" * 62)

    top = rep["rows"][0]
    out += ["", f"Largest risk concentration: {top['ticker']} holds "
                f"{top['weight']:.1%} of capital and {top['risk_share']:.1%} "
                f"of risk ({top['risk_share']/top['weight']:.1f}x)."]
    if rep["no_history"]:
        out.append(f"\nNo price history (not sized): {', '.join(rep['no_history'])}")
    if rep["no_vol"]:
        out.append(f"Insufficient history: {', '.join(rep['no_vol'])}")
    out += [
        "",
        "Sizing only — this makes no forecast about direction. The measured",
        "edge is small and inside the noise; rebalancing a taxable account",
        "realizes gains this calculation does not model.",
    ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--workbook", required=True, help="path to the portfolio .xlsx")
    ap.add_argument("--holdings-sheet", default="Asset PM")
    ap.add_argument("--vol-window", type=int, default=13,
                    help="trailing weeks for realized vol (default 13)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    args = ap.parse_args(argv)

    try:
        import openpyxl
    except ImportError:
        raise SystemExit("openpyxl required: uv sync")

    wb = openpyxl.load_workbook(args.workbook, data_only=True, read_only=True)
    rep = build_report(load_holdings(wb, args.holdings_sheet),
                       load_price_history(wb), args.vol_window)
    print(json.dumps(rep, indent=2, default=str) if args.json else render(rep))
    return 0


if __name__ == "__main__":
    sys.exit(main())
