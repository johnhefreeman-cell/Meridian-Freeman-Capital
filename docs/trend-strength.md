# The 200-day SMA strength tag — and what it is worth

**The rule.** A name at or above its 200-day simple moving average is tagged
**STRONG**; below it, **WEAK**. `scripts/trend_state.py` computes it.

**The finding, first.** In this universe, over this window, the tag **does not
separate returns at any horizon**. What it does separate, consistently, is
**volatility**. It belongs in the sizing decision, not the selection decision.

---

## 1. The weekly approximation

The workbook carries weekly closes. 200 trading days is 40 weeks, and a 40-week
SMA of weekly closes is the standard equivalent — but it is not the same number
as a 200-day SMA of daily closes. On a liquid name the two track within roughly
a percent, which is immaterial for a name 20% clear of its average and decisive
for one sitting on it.

Every name inside **3%** of the line is therefore flagged. On the last weekly
close those were KLAC −0.6%, META −1.6%, UPS −2.0%, AVGO −3.0%. A true daily
series could put any of them on the other side, and the tag should not be relied
on for those four without one.

Yahoo and Stooq are both unavailable from this environment (rate-limited and
blocked at the proxy respectively), so a daily series could not be fetched to
check. This is a stated limitation, not a resolved one.

## 2. The walk-forward test

Causal throughout: the state at week *t* is computed from closes through *t*
only, and applied to the return from *t* to *t+1*. Nothing is fitted on the
evaluation sample — 40 weeks is the definition of the rule, not a choice.

20 names, 220 weeks (Sep 2021 – Aug 2026). Each week, the mean return of the
STRONG bucket minus the mean return of the WEAK bucket. The t-statistic is
computed **across weeks**, not pooled over name-weeks.

| Horizon | Windows | STRONG mean | WEAK mean | Spread | t-stat | Weeks STRONG won |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 week | 220 | +0.72% | +0.77% | −0.05% | −0.18 | 55% |
| 1 month | 217 | +3.00% | +3.28% | −0.28% | −0.48 | 51% |
| 1 quarter | 208 | +10.49% | +9.72% | **+0.77%** | +0.60 | 50% |
| 6 months | 195 | +19.91% | +20.14% | −0.23% | −0.12 | 46% |
| 1 year | 169 | +38.48% | +49.95% | **−11.47%** | −4.42 | 37% |

**The one-year row does not mean what its t-statistic says.** Those 169 windows
overlap: every week is reused 52 times. Split into non-overlapping years, there
are three or four independent observations and they disagree completely —
`+23%, +12%, −23%, −47%` from one starting offset, `−24%, +76%, −12%` from
another. A 52-week block bootstrap puts the spread at **−11.5%, 95% interval
[−25.4%, +2.3%]**, which crosses zero.

So the honest reading of the whole table is: **no signal.** The point estimate
leans negative at a one-year hold — the horizon this fund actually uses — but
the sample cannot support the claim, and it certainly cannot support the
opposite one.

## 3. Portfolios

Equal weight, rebalanced weekly, cash when nothing qualifies.

| Portfolio | $1 becomes | CAGR | Vol | Sharpe | Max DD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Buy & hold, all 20 | 4.38 | 42.0% | 26.7% | 1.58 | −26.6% |
| STRONG only | 4.27 | 41.1% | 25.5% | **1.61** | −30.3% |
| WEAK only | 4.23 | 40.8% | **35.0%** | 1.17 | −30.0% |

**The WEAK bucket compounded at 40.8% against STRONG's 41.1%.** They are the
same return. The difference between them is 9.5 points of volatility.

Filtering the tag by the direction of the average — above the SMA *and* the SMA
rising over 13 weeks — cuts max drawdown to −25.8% but takes $1 to **3.71**
against 4.27. It buys a smoother ride with real wealth.

## 4. Sign instability

Reported, not selected. The rule's spread changes sign between adjacent window
lengths, which is the signature of noise rather than edge:

| Window | Annualized spread | t-stat | STRONG $1 | B&H $1 |
| --- | ---: | ---: | ---: | ---: |
| 26 weeks | **+10.49%** | 0.79 | 5.16 | 4.19 |
| 30 weeks | **+13.95%** | 1.04 | 4.63 | 3.63 |
| **40 weeks** | **−2.60%** | −0.18 | 4.27 | 4.38 |
| 50 weeks | −1.71% | −0.11 | 4.16 | 3.83 |
| 60 weeks | **−16.86%** | −1.07 | 3.53 | 4.36 |

A real effect does not swing from +14% to −17% because the average got twenty
weeks longer.

## 5. What the tag does do

**It sorts volatility, and that result is stable.** Median 13-week forward
realized volatility, by state at the time of tagging, across 3,981 name-weeks:

| State | Median forward volatility | n |
| --- | ---: | ---: |
| STRONG | 32.8% | 2,598 |
| WEAK | **39.7%** | 1,383 |

A name below its 200-day average went on to realize **1.21×** the volatility of
one above it. The drawdown lift is weaker but points the same way: 40% of the
worst decile of 13-week outcomes were already WEAK, against a 35% base rate — a
lift of 1.14×, real but small.

## 6. How to use it

- **As a risk tag, feeding position size.** WEAK names carry more volatility,
  and volatility is what decides an account's risk concentration. This connects
  directly to `scripts/portfolio_extract.py`, where risk share is value ×
  volatility.
- **As a watchlist sort**, to decide what to look at first. It costs nothing.
- **Not as a buy or sell rule.** A weekly-rebalanced trend filter is out of
  mandate under CLAUDE.md §1 — this is not a quant fund and holds 2–4 years —
  and the test above gives no reason to make an exception.
- **Never as a substitute for the gates.** On 5 September KLAC tags **STRONG**,
  6.7% above its average. It also fails three of the six gates in §3.1 and
  breaches §5 by a wide margin. The tag describes the price series. It knows
  nothing about the business.

## 7. Limits of the test

- **20 names, all large-cap, most of them technology, over a period when equal
  weight compounded at 42% a year.** That is not a representative sample and
  the window is not a representative regime.
- **The names were chosen after the fact** — they are what the holder tracks
  today, so survivors are over-represented.
- **220 weeks is roughly four independent years** at the horizon that matters.
  Almost no power.
- **No transaction costs or taxes.** The STRONG-only portfolio trades every
  week; the buy-and-hold comparison does not. The gap in the table is therefore
  flattering to the rule, and it still loses.

*Test scripts are in the session scratchpad; the classifier and its behaviour
are pinned by `tests/test_trend_state.py`.*
