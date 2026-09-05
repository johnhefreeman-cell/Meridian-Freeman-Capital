---
name: buy-setup
description: Screen names for the pullback-in-an-uptrend entry — close above the 200-day SMA and RSI(14) below 40 — on real daily bars. Use when the user asks what to buy today, about RSI, oversold or pullback entries, a buy signal or buy variable, entry timing on a name they already want, or says "/buy-setup".
---

# The buy setup — close > 200-day SMA, RSI(14) < 40

```
uv run python scripts/daily_prices.py --portfolio --workbook <path>   # refresh bars
uv run python scripts/signals.py     --portfolio --workbook <path>
```

Add `--rsi-below N` for a different threshold, but see the sensitivity note below.

---

## What you must say every time you report this

**1. It ranks candidates; it does not time entries.** Tested on six years of
daily bars across 21 names (`docs/buy-setup.md`), the setup beat the trend
filter alone by **+0.89% over the following month**, with a better hit rate
(64% vs 58%) and a better tenth percentile (−7.4% vs −10.4%). But **waiting for
it to fire cost −2.20%** over a 21-day window, interval [−3.55%, −1.11%],
because it only fires on 36% of attempts inside a month and the cash drag
exceeds the better entry.

So: if capital is already committed and several names clear the trend leg, the
one also at RSI < 40 is the better buy today. Never tell the user to sit in
cash waiting for it.

**2. The edge is short-horizon and this fund holds 2–4 years.** It is gone by
one quarter and negative at one year. Say so. Under CLAUDE.md §1 a
weekly-signal rule is out of mandate as a strategy; it is in scope only as
entry selection on a name already chosen on fundamentals.

**3. Most of the edge is the RSI leg, not the trend leg.** RSI-only returned
+1.12% over a week against the setup's +1.24%, and beat the full setup by 11.8
points over a year. Do not present the combination as the source of the edge.

**4. Report the near-misses, not just the fires.** A name at RSI 41.4 above its
average and one at RSI 38.1 below it are both one condition away and mean
different things. `scripts/signals.py` prints the flags — pass them through.
Always name any signal within 2 RSI points of the threshold or 3% of the
average as fragile.

**5. It says nothing about the business.** Show the diligence verdict beside
any name that has a file in `research/names/`. Today the only name firing is
AMAT, which is killed under §4.

## Data

RSI needs **daily** bars — a 14-week RSI is a different indicator, not a
coarser one — so this path does not use the workbook's weekly closes. Bars come
from `scripts/daily_prices.py`, cached under `data/daily/` and gitignored,
because the repo is public and the data is a vendor's.

Indicators run on adjusted closes; `evaluate_both` also runs them raw and flags
disagreement, which matters on higher-yield names where dividend adjustment
moves the 200-day average more than it moves today's close.

## What not to do

- Do not tune the threshold. The one-month edge runs +1.37% at RSI 30, +0.89%
  at 40, +0.25% at 45 and crosses zero near 50 — a smooth plateau, not a peak
  at 40. If asked for other levels, show the curve and say it was not selected.
- Do not measure "wait for the signal" by counting only the times it arrived.
  That conditions on the future and reverses the answer; the first version of
  this test made exactly that error and it is recorded in the docs.
- Do not combine this with the six gates into one score. Different questions.
