---
name: earnings-delta
description: Compare the latest quarter against the prior quarter and the year-ago quarter to isolate what actually changed. Use when the user asks what changed this quarter, to analyze an earnings print, quarter-over-quarter deltas, or says "/earnings-delta".
---

# Earnings Delta

What changed, by how much, and does it change the thesis. Three questions,
in that order.

## Procedure

1. **Identify the periods.** `edgar.list_filings` for the two most recent
   10-Qs (or 10-K if Q4) plus the year-ago comparable. Note fiscal-vs-calendar
   offset (CLAUDE.md §8).

2. **Pull the line items** via `edgar.xbrl_concept` for each of: revenue by
   segment where tagged, gross profit, operating expense lines, operating
   income, net income, operating cash flow, capex, share count, deferred
   revenue / RPO where applicable.

3. **Build the delta table** — sequential and YoY, in both dollars and
   percentage points for margins.

4. **Separate mix from rate.** A margin move is either price, mix, or cost.
   Say which. This is the step that produces insight; skipping it produces a
   variance table nobody can act on.

5. **Read the language.** `edgar.get_filing_text` on the MD&A. Compare the
   risk factors and MD&A framing against the prior quarter — new language is
   signal. Hand off to `/filing-diff` if the text comparison is the main event.

6. **Check cash conversion.** FCF/NI for the quarter and TTM against the
   CLAUDE.md §3 gate of ≥0.8. A widening gap is the single most common early
   warning; if it widened, find the working-capital line responsible.

## Output

- **Verdict first:** thesis intact / thesis damaged / thesis broken, in one sentence.
- **Delta table:** line item | prior Q | this Q | Δ | YoY Δ | driver
- **The three things that actually changed**, ranked by thesis relevance.
- **What did not change** that the market appears to think did (or vice versa).
- **Gate re-check:** any of the six gates whose status moved.
- **Kill criteria check:** explicitly, did this print trip any of CLAUDE.md §4.
- Every figure cited `[10-Q 2025-Q3, p.14]`.

## Do not

- Do not lead with the headline beat/miss. Consensus is not the thesis.
- Do not adopt management's non-GAAP framing; show the GAAP bridge (CLAUDE.md §7).
