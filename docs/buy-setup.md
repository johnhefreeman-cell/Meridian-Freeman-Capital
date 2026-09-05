# The buy setup — close above the 200-day SMA, RSI(14) below 40

**The rule.** Buy when the current bar's close is above the 200-day simple
moving average **and** RSI(14) is below 40. Two conditions doing two jobs: the
average says the name is in an uptrend, the RSI says it has pulled back inside
that uptrend.

**The finding, first.** The setup has a real but modest edge over the trend
filter alone, and only over the next few weeks. **Waiting for it loses money** —
it fires too rarely to be worth sitting in cash for. Use it to choose *which*
candidate gets capital today, never to decide *when* to deploy.

---

## 0. This one needed real daily bars

Everything else in this repo runs off the workbook's weekly closes. That works
for a 200-day average — 40 weeks is the accepted equivalent — and it does **not**
work for RSI. RSI is a ratio of average gains to average losses over N bars, so
changing the bar frequency changes the indicator itself; a 14-week RSI and a
14-day RSI are different measurements, not two resolutions of one.

So `scripts/daily_prices.py` fetches daily closes and caches them. Six years,
21 names. The cache is gitignored: the repo is public and the data is a
vendor's, so the fetcher ships rather than the bars.

The daily series validates against the holdings workbook to the cent on most
names — MRVL $223.55, KLAC $185.60, AMAT $454.71, SNDK $1,740.00, GOOGL $338.46
all match. **It also closes a gap:** GOOGL has no tab in the workbook and so
appears in none of the weekly-based work. It has daily bars, and it is included
here.

## 1. What fires today

As of the close on 4 September 2026, of 19 held single names, **one fires**:

| Name | Close | 200-day SMA | vs SMA | RSI(14) | |
| --- | ---: | ---: | ---: | ---: | --- |
| **AMAT** | 454.71 | 406.28 | +11.9% | **39.8** | **BUY** |
| LLY | 1,149.36 | 1,060.38 | +8.4% | 41.4 | trend yes, RSI 1.4 short |
| AVGO | 357.90 | 369.03 | −3.0% | 38.1 | RSI yes, but below its average |
| CDNS | 292.70 | 327.13 | −10.5% | 31.0 | oversold *and* below — the case the trend leg exists to exclude |

**AMAT's RSI is 39.8 against a threshold of 40.** That is a fire by two tenths
of a point, and it survives on both adjusted and raw closes (39.8 / 39.7), but
it is not a comfortable margin and the file says so rather than reporting a
clean signal.

**AMAT is also killed** under §4 — $173.2M of insider selling against $0 of
buying with no 10b5-1 plan on any of ninety Form 4s. The setup is a price
pattern. It does not know that.

Two names sit within 3% of their average (BRK.B +2.8%, GOOGL +0.9%) where the
choice of price series can move them across. One name, UPS, sits on opposite
sides depending on dividend adjustment (+0.4% adjusted, −2.5% raw); it is not
held and does not fire either way, but it is why `evaluate_both` exists.

## 2. Does the setup pay?

Signal at the close of day *t*, entry at that close, return to *t+h*. No
lookahead, nothing fitted — 200, 14 and 40 are the specification, not choices.
1,261 signal days, 4.9% of all name-days, across **196 independent episodes**
(same name, gaps over 30 days).

| Horizon | BUY setup | Trend only | RSI only | All days | BUY − trend |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 week | **+1.24%** | +0.58% | +1.12% | +0.59% | **+0.66%** |
| 1 month | **+3.49%** | +2.60% | +3.36% | +2.53% | **+0.89%** |
| 1 quarter | +7.04% | +7.54% | +10.11% | +7.74% | −0.50% |
| 6 months | +14.12% | +14.88% | +16.91% | +14.99% | −0.77% |
| 1 year | +22.82% | +26.71% | +34.58% | +31.44% | **−3.89%** |

A 250-day block bootstrap puts the one-week BUY mean at [+0.71%, +1.78%] and
the one-month at [+2.62%, +4.54%], both clear of the trend-only means. **At a
quarter and beyond the intervals contain the baseline** and the point estimates
turn negative.

Read the third column: **most of the short-horizon edge is the RSI, not the
trend filter.** RSI-only returns +1.12% over a week against the setup's +1.24%.
And over a year, RSI-only beats the setup by 11.8 points — combining the two
actively hurt at long horizons in this sample.

**The left tail improves, which is the more useful half:**

| Horizon | BUY win rate | Trend win rate | BUY 10th pct | Trend 10th pct |
| --- | ---: | ---: | ---: | ---: |
| 1 month | **64%** | 58% | **−7.4%** | −10.4% |
| 1 quarter | 66% | 61% | **−13.6%** | −16.0% |
| 1 year | 70% | 71% | −26.2% | −25.0% |

## 3. Is 40 a cliff or a plateau?

Monotone, which is what a real effect looks like. One-month edge over the trend
filter, by threshold:

| RSI below | Mean 1-month | vs trend only | Win rate | 10th pct | Signals |
| --- | ---: | ---: | ---: | ---: | ---: |
| 30 | +3.97% | **+1.37%** | 77% | −5.8% | 112 |
| 35 | +3.29% | +0.69% | 65% | −6.7% | 461 |
| **40** | +3.49% | **+0.89%** | 64% | −7.4% | 1,242 |
| 45 | +2.85% | +0.25% | 61% | −9.3% | 2,751 |
| 50 | +2.55% | −0.05% | 59% | −10.2% | 4,941 |
| 55 | +2.37% | −0.23% | 58% | −10.6% | 7,609 |

The edge and the downside both degrade smoothly as the threshold loosens, and
the edge crosses zero around 50. There is no spike at 40 — it sits inside a
working range rather than on a lucky number. 30 is stronger but fires 112 times
in six years across 21 names, which is roughly nothing.

## 4. Waiting for it loses — and the first cut of this was wrong

The obvious use is "hold cash until the setup fires." Tested naively, that
looked excellent: a 21-day window gave +8.66% against +3.20% for buying
immediately.

**That number was wrong, and the error is worth recording.** It only counted
days where the setup *did* fire inside the window — a fact from the future. The
days it excludes are precisely the ones where the name kept rising and never
pulled back, which is exactly when waiting costs you.

Corrected to an executable rule — wait up to N days, and if it never fires, buy
at the deadline anyway — the answer reverses:

| Max wait | Cases | Fill rate | Buy now | Waited | Edge | Now 10th pct | Wait 10th pct |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 days | 16,571 | 23% | +8.94% | +7.81% | **−1.14%** | −16.6% | −15.9% |
| 21 days | 16,391 | 36% | +10.41% | +8.21% | **−2.20%** | −17.7% | −15.9% |
| 42 days | 16,114 | 55% | +13.00% | +9.53% | **−3.46%** | −18.8% | −16.3% |
| 63 days | 15,902 | 69% | +14.88% | +10.75% | **−4.13%** | −21.0% | −17.0% |

Paired difference over the 21-day window: **−2.20%, 95% interval [−3.55%,
−1.11%]**, entirely below zero. Waiting wins 46% of the time.

The setup fires on only 36% of attempts inside a month. The other 64% of the
time you are holding cash in a rising name, and that cost is larger than the
better entry is worth. Waiting does buy a better left tail — 10th percentile
−15.9% against −17.7% — so it is a genuine risk-for-return trade, not a free
lunch in either direction.

## 5. How to use it

- **As a ranking rule for capital already committed.** If you have money to
  deploy and several names clear the trend filter, the one also at RSI below 40
  has done better over the following month, with a better downside. That
  captures the +0.89% without paying the waiting cost.
- **Not as a market-timing rule.** Section 4 is unambiguous.
- **Not for a 2–4 year hold.** The edge is gone by one quarter and negative at
  a year, and CLAUDE.md §1 puts weekly-signal trading out of mandate anyway.
- **Never in place of the gates.** The only name firing today is one the
  framework killed.

## 6. Limits

- **21 names, mostly large-cap technology, over six years in which buying
  almost anything worked.** Not a representative universe or regime.
- **The names were chosen after the fact** — they are what the holder tracks
  today, so survivors are over-represented and the "buy now" leg is flattered.
- **196 independent episodes**, not 1,261. The signal-day count overstates the
  evidence by roughly six times.
- **No costs or taxes.** Every rule that trades more is flattered by that, and
  the waiting rule still lost.
- **Adjusted closes** are used for the indicators. Dividend adjustment moves a
  200-day average by more than it moves today's close; both series are computed
  and disagreements are reported.
