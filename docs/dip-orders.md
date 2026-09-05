# Dips, and the orders they produce

**A dip is one bar** on which the close is above the 200-day simple moving
average **and** RSI(14) is below 40. When a dip occurs, the system writes a buy
order priced at **that bar's closing price**.

Everything below is about the gap between that sentence and an order that can
actually be filled.

---

## 1. The close has already happened

The dip is only knowable after the bar closes, so its closing price cannot be
bought at that close. The order is a **limit working the next session** at that
price. Whether it fills depends on whether the stock comes back to it — which
is not a coincidence, it is a selection.

Measured on six years of daily OHLC across 21 names, 1,243 signals:

| Limit good for | Fills | Missed on a gap up | Average fill vs the limit |
| --- | ---: | ---: | ---: |
| 1 session | **78%** | 22% | **−0.54%** |
| 2 sessions | 84% | 16% | −0.51% |
| 3 sessions | 87% | 13% | −0.50% |
| 5 sessions | 89% | 11% | −0.49% |
| 10 sessions | 92% | 8% | −0.46% |

The fill price averages half a percent *below* the limit, because a gap down
fills at the open rather than at the limit. That is a real price improvement.

## 2. But the fills are the worse trades

| One-session limit | n | Return over the next 21 sessions | Win rate |
| --- | ---: | ---: | ---: |
| **Filled** at the limit | 975 | **+2.88%** | 61% |
| **Missed** — gapped away | 268 | +4.94% *(chasing the open)* | 69% |
| Missed, measured from the signal close | 268 | **+6.99%** | — |

The trades you get are the ones where the stock kept falling. The ones you miss
are the ones that ran. Measured from the same signal close, the names that
gapped away returned **+6.99%** against **+2.33%** for the names that filled —
a three-fold difference in outcome, selected entirely by whether your limit was
touched.

This is adverse selection and it is the single largest effect in the study.

## 3. So the fallback matters more than the limit

Three policies, each measured **per signal** so that an unfilled order counts as
the nothing it earns:

| Policy | Trades | Per trade | Per signal |
| --- | ---: | ---: | ---: |
| **A** limit at the close, cancel if unfilled | 78% of signals | +2.88% | **+2.26%** |
| **B** market at the next open, always | 100% | +3.06% | **+3.06%** |
| **C** limit at the close, buy the open if it does not fill | 100% | +3.33% | **+3.33%** |

**C is the default** (`FALLBACK_CHASE`). The limit is worth placing — it earns
the 0.54% improvement on the 78% that fill — but abandoning the 22% that gap
away costs far more than the improvement is worth. Passing `--no-chase` selects
A, and the help text says what it costs.

## 4. What the earlier backtest assumed

`docs/buy-setup.md` measured entry at the signal close, which is not
purchasable. Re-measured honestly:

| | 21-session return |
| --- | ---: |
| Buy at the signal close (not possible) | +3.34% |
| Limit at the close, chase the open if missed | +3.33% |
| Difference | **−0.01%**, interval [−0.09%, +0.07%] |

The earlier figures survive. The price improvement on the fills almost exactly
offsets the adverse selection on the misses. That is luck rather than design —
it would not hold for a wider limit or a less liquid book — but the number
stands as measured.

## 5. Order cadence

Across the 19 held single names over six years: **1,139 dip bars**, which
collapse to **389 distinct pullback episodes** once consecutive bars of the same
pullback are counted once. Only the first bar of a run generates an order; the
later bars are the same pullback restating itself.

| | |
| --- | --- |
| Episodes per year | 55, 43, 71, 92, 68, 60 |
| Months with at least one | 56 of 72 |
| Median episodes per month | **5** |
| Busiest month | 24 (July 2024) |

Roughly five order tickets a month, with occasional weeks where a quarter of the
book fires at once — because these names are correlated, and a market-wide
pullback trips them together. That clustering is a sizing problem, not a signal.

## 6. What the order carries

Every ticket is written with:

- **Limit** — the signal bar's close, to the cent.
- **Working from** — the next session. `DAY` time in force.
- **Fallback** — chase the open, per §3.
- **Quantity — `UNSET`.** No sizing parameter has been specified, so none is
  invented. This is the open parameter.
- **§2.1 liquidity ceiling** — 10 days × 25% × 20-day median daily dollar
  volume. Now computed rather than asserted; the market data that was missing
  all along arrived with the OHLC bars.
- **Fragility flag** — set when the signal sits within 2 RSI points or 3% of the
  average, where a different price source could move it across.
- **Status** — `READY` or `BLOCKED`.

## 7. Killed names are blocked

A name with a `KILL.md` or a `20-verdict.md` in `research/names/` is emitted
**BLOCKED**, with the reason and the file path attached. It is neither silently
dropped nor silently placed.

The block reads the research directory rather than a list in the code, so a name
killed tomorrow blocks tomorrow.

**This is not hypothetical.** The only dip on the current bar is **AMAT**, which
is killed under §4 for $173.2M of insider selling against $0 of buying with no
10b5-1 plan on any of ninety Form 4s. Historically the three names now carrying
verdicts — MRVL, AMAT, KLAC — account for **61 of the 389 episodes, 16%**.

## 8. The current ticket

```
BLOCKED AMAT   BUY LIMIT     454.71   qty UNSET
        200-day SMA 406.28 (+11.9%) · RSI(14) 39.8
        §2.1 ceiling $8,020,432,572 — not binding at any plausible size
        FRAGILE — within 2 RSI points of the threshold
        BLOCKED · KILLED — research/names/AMAT/KILL.md
```

Two further notes on this specific signal. RSI is **39.8** against a threshold
of 40 — it fires by two tenths. And the dip bar was a **+4.3% up day**
($435.91 → $454.71), so the limit sits above the previous four closes; the
pullback that produced the low RSI happened *before* the signal bar.

## 9. Limits

- **21 names, six years, one regime.** The fill and adverse-selection numbers
  are specific to large, liquid names in a rising market. A thinner book fills
  less often and suffers worse selection.
- **No costs, no taxes, no partial fills.** A limit at the close is modelled as
  filling in full if the session's low touches it.
- **Dividend adjustment** shifts the average more than it shifts today's close.
  Signals are computed on adjusted closes and checked against raw; disagreements
  are flagged on the ticket.
- **Quantity is unspecified**, so nothing here says how much to buy, and no
  result above depends on a sizing assumption.
