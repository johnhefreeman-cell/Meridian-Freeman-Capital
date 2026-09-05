---
name: narrative
description: Capture the consensus narrative, catalyst and institutional view for holdings, sweeping the whole portfolio or named tickers. Use when the user asks why a stock is moving, what the market is saying, what the story is on a name, for a narrative or sentiment sweep, or says "/narrative".
---

# Narrative

Establishes **what consensus believes**. That is all it does. Its output is the
thing a thesis disagrees with — the input to CLAUDE.md §6 step 5, never a
finding in its own right.

## The evidence problem, stated up front

This skill reads news, social commentary and sell-side chatter. Those are the
**bottom three tiers** of the CLAUDE.md §7 hierarchy — *Filing > transcript >
press release > sell-side > news* — and the rule says never invert that order.

Two hard constraints follow, and they are not negotiable by convenience:

1. **Nothing this skill produces may be cited as fact anywhere else.** Not in a
   gate score, not in a valuation, not in a kill-criteria check. Its figures are
   tagged `[NEWS]` and stay quarantined in the variant-perception section.
2. **Contradictions are reported, never resolved.** When two sources disagree on
   a number, print both with their sources and mark it `UNRECONCILED`. Do not
   pick the more plausible one — the picking is where fabrication starts.

A single search on one name has already produced two irreconcilable revenue
figures for the same quarter. Expect that, and surface it.

## Inputs

Either named tickers (`/narrative MRVL,SNDK`) or nothing, which sweeps every
single-name holding.

**Never hand-maintain the ticker list.** Get it from the portfolio:

```bash
uv run python scripts/risk_sizing.py --workbook <path> --json
```

That returns per-account rows with `ticker`, `value`, `weight`, `vol` and
`risk_share`. Use it for the universe *and* for the position context in step 3.

## Procedure

1. **Order the work by risk, not alphabetically.** Sort by `risk_share`
   descending. The name carrying the most risk gets read first, and if the sweep
   is interrupted the important ones are already done.

2. **Dispatch `narrative-scout` agents in parallel**, batched at 4 tickers each,
   all in one message. Each writes
   `research/narrative/<YYYY-MM-DD>/<TICKER>.md`. Give each agent its ticker
   batch and the position facts for those names.

3. **Pair every narrative with the position.** A story is only interesting
   relative to what you own. Each file carries: cost basis and gain/loss, percent
   below the 52-week high, weight, volatility, and risk share. "The market is
   worried about margins" reads differently on a 2% position than on one holding
   a quarter of an account's risk.

4. **Write the index** at `research/narrative/<YYYY-MM-DD>/INDEX.md`: one row per
   name, sorted by risk share, with the one-line read and any `UNRECONCILED`
   flags. This is the deliverable that gets read.

5. **Report the disagreements, not the summary.** In chat, lead with: names where
   sources contradict each other, names where the narrative conflicts with the
   position (the market loves it and you are down; the market hates it and you
   are up), and names where nothing was found at all.

## Output per ticker

```
# <TICKER> — narrative as of <DATE>

**Position:** $X (Y% of <account>, Z% of its risk) · cost $C, P/L ±N%
· V% below 52wk high · vol W%

## Retail narrative        [NEWS] [SOCIAL]
## Catalyst                [NEWS] — dated, specific, with the number
## Institutional view      [SELL-SIDE] — target changes, up/downgrades
## Unreconciled            — contradictions between sources, both sides shown
## What consensus assumes  — the load-bearing belief, stated so it can be tested
```

The last section is the one that matters. Not "what nobody is talking about" —
a search cannot establish absence, and claiming it can is the failure mode of
this whole genre. State instead **the assumption the current price requires**,
which is testable against a filing later.

## Do not

- Do not resolve a contradiction by choosing. Print both.
- Do not report a price, revenue or margin figure without `[NEWS]` and a source.
- Do not claim to know what "nobody is talking about". Report what the searches
  did and did not surface, and label it as coverage, not absence.
- Do not let this output reach a memo's gate table, valuation or kill-criteria
  check. It belongs in §5 and nowhere else.
- Do not run it as a buy or sell signal. Narrative is what you are betting
  against, not with.
