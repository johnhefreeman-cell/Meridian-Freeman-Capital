---
name: mgmt-scorecard
description: Score management credibility by scoring guidance against actuals over three years. Use when the user asks whether management is credible or trustworthy, to check guidance vs actuals, a management track record, or says "/mgmt-scorecard".
---

# Management Scorecard

Management quality is not a vibe from an earnings call. It is a track record
you can tabulate: what they said would happen, and what happened.

## Procedure

1. **Collect the guidance.** For each of the last 12 quarters, pull the 8-K
   earnings release (`edgar.list_filings` form `8-K`, then `get_filing_text`)
   and record every forward number given: revenue, margin, EPS, FCF, capex,
   and any operating metric they chose to guide.

2. **Collect the actuals.** `edgar.xbrl_concept` for the same lines in the
   period that was guided. Filing figures, not vendor figures.

3. **Score each pair.** Guided → actual → variance %. Classify:
   `BEAT / IN-LINE (±2%) / MISS`.

4. **Score the qualitative promises too.** Every "we expect to close X",
   "the integration will complete by Y", "we will be FCF positive in H2".
   These are where credibility is actually lost, and nobody tabulates them.

5. **Watch the framework, not just the hit rate.** A team that guides
   conservatively and beats 12 of 12 is managing the guide, not the business.
   Look for: guidance withdrawn, metric redefined, disclosure discontinued,
   segment re-cut. A changed denominator is the oldest trick in the file.

6. **Check alignment.** DEF 14A via `edgar.list_filings` form `DEF 14A`:
   what is comp actually tied to? Revenue and "adjusted EBITDA" targets pay
   for empire-building. Per-share value and ROIC do not (CLAUDE.md §3, gate 5).

7. **Check the trades.** `edgar.insider_transactions` — codes **P** and **S**
   only. Grants (A), option exercises (M), and tax withholding (F) are not
   decisions. Ownership trend over 3 years matters more than any single trade.

## Output

- **Credibility grade: A–F**, with the one sentence that justifies it.
- **Scorecard:** period | metric | guided | actual | variance | verdict
- **Hit rate** by metric, and the trend — improving or deteriorating.
- **Broken qualitative promises**, quoted with dates.
- **Framework changes:** anything redefined, withdrawn, or discontinued.
- **Alignment:** comp metrics, insider ownership %, 3-year P/S trend.
- **Kill-criteria check** — CLAUDE.md §4 covers guidance misses (3+ in 8
  quarters) and insider selling. State the result explicitly.

## Do not

- Do not grade on tone, polish, or how good the strategy sounds.
- Do not count a beat against a guide that was cut earlier the same year as a beat.
  Show the original guide too.
