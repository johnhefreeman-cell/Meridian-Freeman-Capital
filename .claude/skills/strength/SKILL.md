---
name: strength
description: Tag every name in the book STRONG or WEAK against its 200-day simple moving average, with distance, the direction of the average, and how long it has held its side. Use when the user asks which stocks are strong or weak, about the 200-day (or 40-week) moving average, trend state, what is above or below its average, or says "/strength".
---

# Trend strength — the 200-day SMA tag

A name at or above its 200-day simple moving average is **STRONG**; below it,
**WEAK**. That is the entire rule and it should be reported as such — plainly,
with no interpretation smuggled in.

Run it:

```
uv run python scripts/trend_state.py --workbook <path> --current-prices
```

`--current-prices` marks each name against the holdings sheet's live price
while the average stays as of the last weekly close. Omit it to mark on the
last weekly close throughout, which is internally consistent but staler.

---

## What you must say every time you report this

**1. The tag is a volatility signal, not a return signal.** This was tested
walk-forward over 220 weeks and 20 names (`docs/trend-strength.md`). The STRONG
bucket did not out-return the WEAK bucket at any horizon from one week to one
year, and the spread's sign flips with the window length. What it does separate
is volatility: names below their average went on to realize **1.21×** the
volatility of names above. Report the finding, not the folklore.

Never present the tag as a buy or sell signal. If the user asks for one, say
what the test found and give them the tag anyway — they asked for it, and the
number is theirs.

**2. The average is weekly, so name the approximation.** The workbook holds
weekly closes. 40 weeks is the standard 200-day equivalent but not the same
number. **Always print the names inside 3% of the line** and say that a true
daily series could flip them. Do not quietly report a tag you know is fragile.

**3. It says nothing about the business.** The clearest illustration is in the
book already: KLAC tags STRONG while failing three of the six gates in §3.1 and
breaching §5. Where a name has a file in `research/names/`, show its diligence
verdict beside the tag so the two are never confused.

**4. Distance and duration carry more than the tag.** A name 1% above its
average for one week and one 50% above it for a year both read STRONG. Always
report `vs SMA`, the 13-week slope of the average, and `weeks in state`.

## Output shape

Sort by distance from the average, strongest first. Columns: name, state,
price, SMA, vs SMA, SMA 13-week slope, weeks in state, 13-week volatility, and
the diligence verdict where one exists. Then, in order:

- the strong/weak count;
- median volatility of each bucket, which is the finding that holds;
- the names within 3% of the line;
- any held single name with **no price series at all** — it cannot be tagged
  and must be listed rather than omitted. GOOGL is one today.

## What not to do

- Do not run it on funds. The workbook has price history for single names only,
  and a fund's trend state is not derivable from the holdings sheet.
- Do not tune the window. 40 weeks is the definition of the rule. If asked for
  other lengths, show them as a sensitivity and say they were not selected —
  the spread runs +14% at 30 weeks and −17% at 60, which is what noise looks
  like, not a menu to pick from.
- Do not combine the tag with the gates into a single score. They answer
  different questions and a blended number would hide both.
