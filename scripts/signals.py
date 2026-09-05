"""The buy setup: close above the 200-day SMA, and RSI(14) below 40.

Two conditions doing two different jobs. The moving average says the name is in
an uptrend; the RSI says it has pulled back inside that uptrend. Together they
are the classic "buy the dip, but only in something that is going up" filter,
and the point of separating them is that each can be tested on its own.

**What the test found** (`docs/buy-setup.md`, 21 names, 6 years of daily bars,
1,261 signal days across 196 independent episodes):

- Conditional on the setup firing, the next month returned **+3.49%** against
  **+2.60%** for every day the name was merely above its average — a real but
  modest **+0.89%**, with a better left tail (10th percentile −7.4% against
  −10.4%) and a higher hit rate (64% against 58%).
- The edge is short-horizon. By one quarter it is gone, and at one year the
  setup *underperformed* the trend filter alone by 3.9 points.
- **Waiting for the setup loses.** As a policy — hold cash until RSI drops
  below 40, buy at the deadline if it never does — it cost **−2.20%** over a
  21-day window, interval [−3.55%, −1.11%], because the signal fires on only
  36% of attempts inside a month and the days spent waiting cost more than the
  better entry is worth. It wins 46% of the time.

So the setup answers *"which of my candidates do I buy today"*, not *"when do I
buy this one"*. Use it to rank capital that is already committed. Do not use it
to hold cash.

**RSI needs daily bars.** RSI is a ratio of average gains to average losses
over N bars; changing the bar frequency changes the indicator. The workbook's
weekly closes cannot produce a 14-day RSI, so this module reads the daily cache
from `scripts/daily_prices.py`.

Usage:
    uv run python scripts/signals.py --portfolio --workbook p.xlsx
    uv run python scripts/signals.py AAPL MSFT AMAT
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import daily_prices as dp  # noqa: E402

SMA_DAYS = 200
RSI_DAYS = 14
RSI_BUY_BELOW = 40.0

# Inside this band of the RSI threshold or the average, the tag is fragile:
# a different price source, or dividend adjustment, can move it across.
RSI_NEAR = 2.0
SMA_NEAR = 0.03


def sma(values: list[float], window: int = SMA_DAYS) -> list[float | None]:
    """Rolling simple mean. Index i holds the mean of values[i-window+1:i+1]."""
    out: list[float | None] = [None] * len(values)
    total = 0.0
    for i, x in enumerate(values):
        total += x
        if i >= window:
            total -= values[i - window]
        if i >= window - 1:
            out[i] = total / window
    return out


def rsi(values: list[float], window: int = RSI_DAYS) -> list[float | None]:
    """Wilder's RSI.

    The first average gain and loss are simple means of the first `window`
    changes; every later one is smoothed as (prev * (window - 1) + current) /
    window. That smoothing is what makes this Wilder's RSI rather than a
    rolling-mean lookalike — the two differ by several points on a trending
    series, enough to move a name across a threshold, so the distinction is not
    cosmetic. An all-gains window gives 100 by definition.
    """
    out: list[float | None] = [None] * len(values)
    if len(values) < window + 1:
        return out

    gain = sum(max(values[i] - values[i - 1], 0.0) for i in range(1, window + 1)) / window
    loss = sum(max(values[i - 1] - values[i], 0.0) for i in range(1, window + 1)) / window
    out[window] = 100.0 if loss == 0 else 100.0 - 100.0 / (1.0 + gain / loss)

    for i in range(window + 1, len(values)):
        change = values[i] - values[i - 1]
        gain = (gain * (window - 1) + max(change, 0.0)) / window
        loss = (loss * (window - 1) + max(-change, 0.0)) / window
        out[i] = 100.0 if loss == 0 else 100.0 - 100.0 / (1.0 + gain / loss)
    return out


def evaluate(series: dict, field: str = "adj",
             sma_days: int = SMA_DAYS, rsi_days: int = RSI_DAYS,
             rsi_below: float = RSI_BUY_BELOW) -> dict | None:
    """State of the setup on the last bar, or None without enough history."""
    dates, values = dp.closes(series, field)
    averages = sma(values, sma_days)
    strengths = rsi(values, rsi_days)
    if averages[-1] is None or strengths[-1] is None:
        return None

    close, average, strength = values[-1], averages[-1], strengths[-1]
    above = close > average
    pulled_back = strength < rsi_below

    return dict(
        ticker=series.get("ticker", series.get("symbol")),
        date=dates[-1], close=close, sma=average, rsi=strength,
        distance=close / average - 1,
        above_sma=above, rsi_below=pulled_back,
        buy=above and pulled_back,
        near_rsi_line=abs(strength - rsi_below) <= RSI_NEAR,
        near_sma_line=abs(close / average - 1) <= SMA_NEAR,
        bars=len(values), field=field,
    )


def dips(series: dict, field: str = "adj",
         sma_days: int = SMA_DAYS, rsi_days: int = RSI_DAYS,
         rsi_below: float = RSI_BUY_BELOW) -> list[dict]:
    """Every bar in the series where the dip criteria hold.

    A **dip** is one bar, not a state: the close is above the 200-day average
    and RSI(14) is below 40 on that bar. Consecutive bars can each be a dip,
    so `first_of_run` marks the bar the condition became true — that is the
    one an order should be built from, since the later bars in a run are the
    same pullback re-announcing itself, not new information.
    """
    dates, values = dp.closes(series, field)
    averages = sma(values, sma_days)
    strengths = rsi(values, rsi_days)

    out: list[dict] = []
    previous = False
    for i, close in enumerate(values):
        avg, strength = averages[i], strengths[i]
        if avg is None or strength is None:
            previous = False
            continue
        hit = close > avg and strength < rsi_below
        if hit:
            out.append(dict(index=i, date=dates[i], close=close, sma=avg,
                            rsi=strength, distance=close / avg - 1,
                            first_of_run=not previous))
        previous = hit
    return out


def evaluate_both(series: dict, **kw) -> dict | None:
    """Evaluate on adjusted and raw closes, and flag any disagreement.

    Dividend adjustment shifts the average without shifting today's close, so a
    high-yield name can sit on opposite sides of its 200-day average depending
    on which series you use. A signal that survives only one of them is not a
    signal worth acting on, and this is where that gets caught.
    """
    adj = evaluate(series, "adj", **kw)
    raw = evaluate(series, "close", **kw)
    if adj is None:
        return None
    adj["raw"] = raw
    adj["agrees"] = bool(raw is not None and raw["buy"] == adj["buy"]
                         and raw["above_sma"] == adj["above_sma"])
    return adj


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--portfolio", action="store_true")
    ap.add_argument("--workbook")
    ap.add_argument("--root", default=dp.CACHE_DIR)
    ap.add_argument("--rsi-below", type=float, default=RSI_BUY_BELOW)
    ap.add_argument("--refresh", action="store_true")
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

    series, failed = dp.fetch_many(dict.fromkeys(tickers), root=args.root,
                                   refresh=args.refresh)
    results = {}
    short = []
    for t, s in series.items():
        got = evaluate_both(s, rsi_below=args.rsi_below)
        if got is None:
            short.append(t)
        else:
            results[t] = got

    ordered = sorted(results.values(), key=lambda r: (not r["buy"], -r["distance"]))
    as_of = ordered[0]["date"] if ordered else "?"
    print(f"Buy setup — close > {SMA_DAYS}-day SMA and RSI({RSI_DAYS}) < "
          f"{args.rsi_below:g}, as of {as_of}\n")
    print(f"{'name':<7}{'close':>10}{'SMA200':>10}{'vs SMA':>9}{'RSI14':>8}"
          f"{'above':>7}{'pulled back':>13}{'':>6}")
    print("-" * 70)
    for r in ordered:
        flags = []
        if r["near_rsi_line"]:
            flags.append(f"RSI within {RSI_NEAR:g} of the line")
        if r["near_sma_line"]:
            flags.append("price near the average")
        if not r["agrees"]:
            flags.append("adjusted and raw closes disagree")
        print(f"{r['ticker']:<7}{r['close']:>10.2f}{r['sma']:>10.2f}"
              f"{r['distance']:>+9.1%}{r['rsi']:>8.1f}"
              f"{('yes' if r['above_sma'] else 'no'):>7}"
              f"{('yes' if r['rsi_below'] else 'no'):>13}"
              f"{('   BUY' if r['buy'] else ''):>6}")
        if flags:
            print(f"{'':<7}{'· ' + '; '.join(flags)}")

    buys = [r["ticker"] for r in ordered if r["buy"]]
    print(f"\n{len(buys)} of {len(results)} fire: " + (", ".join(buys) or "none"))
    print(f"{sum(1 for r in results.values() if r['above_sma'])} above the average; "
          f"{sum(1 for r in results.values() if r['rsi_below'])} with RSI below "
          f"{args.rsi_below:g}")
    if short:
        print(f"\nnot enough history for a {SMA_DAYS}-day average: "
              + ", ".join(short))
    if failed:
        print("\nno data:")
        for f in failed:
            print("  " + f)


if __name__ == "__main__":
    main()
