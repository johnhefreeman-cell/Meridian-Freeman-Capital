---
name: dip-orders
description: Find dips — close above the 200-day SMA with RSI(14) below 40 — and write buy order tickets limit-priced at that bar's close. Use when the user asks for buy orders, order tickets, what to place, dips or dip buying, or says "/dip-orders".
---

# Dip orders

```
uv run python scripts/daily_prices.py --portfolio --workbook <path> --refresh
uv run python scripts/orders.py      --portfolio --workbook <path> --write orders/
```

A **dip** is one bar: close above the 200-day SMA *and* RSI(14) below 40. Each
dip produces a BUY LIMIT at **that bar's closing price**.

---

## What you must say every time

**1. It is a limit for the next session, never a fill at that close.** The dip
is known only after the close. Never describe the order as buying at the signal
close, and never quote a backtest that assumes it.

**2. Quote the fallback with the order.** The limit fills 78% of the time in
one session and averages 0.54% below the limit — but the fills are the worse
trades (+2.88% over 21 sessions against +6.99% for the ones that gapped away,
both measured from the signal close). Per signal: cancel-if-unfilled **+2.26%**,
market-at-open **+3.06%**, **limit-then-chase +3.33%**. Chasing is the default.
If the user wants a resting limit only, say what it costs.

**3. Quantity is UNSET and that is deliberate.** No sizing parameter has been
given. Never invent one. Report the §2.1 ceiling that constrains it — 10 days ×
25% × 20-day median daily dollar volume — which is now computed from real
volume rather than asserted.

**4. Report BLOCKED tickets, do not hide them.** A name with a kill or a failed
verdict is emitted BLOCKED with the reason. Show it and show why. Do not present
a blocked ticket as actionable and do not omit it — the user needs to see that
the pattern fired on a name the gates rejected.

**5. Flag fragile signals.** Within 2 RSI points or 3% of the average, a
different price source can move the signal across. The generator sets the flag;
pass it through.

**6. Only the first bar of a run.** Consecutive dip bars are one pullback
restating itself, not new orders. The generator handles this; do not
double-count when describing history.

## Cadence, so expectations are set

389 episodes across 19 names in six years — a median of five tickets a month,
with occasional weeks where a quarter of the book fires together because these
names are correlated. That clustering is a sizing problem, not a signal.

## Doctrine

CLAUDE.md §10 permits order tickets **for the holder's own execution only**.
Nothing is transmitted to a broker; a ticket is a written intention. §10.1
governs the gate interaction — read it before changing how blocking works.

## What not to do

- Do not place, transmit, or describe an order as placed. This writes files.
- Do not fill in a quantity.
- Do not suppress a BLOCKED ticket to make the output tidier.
- Do not re-run the backtest with entry at the signal close; it is not a
  purchasable price and `docs/dip-orders.md` records what the honest version costs.
