---
name: filing-diff
description: Diff a filing against the prior period word by word to surface changed risk factors, accounting language, and quietly removed disclosures. Use when the user asks to compare filings, diff a 10-Q or 10-K, find changed language or removed disclosure, or says "/filing-diff".
---

# Filing Diff

Companies rarely announce bad news. They edit it into the risk factors. This
skill finds the edits.

## Procedure

1. **Fetch both filings.** `edgar.list_filings` for the two periods, then
   `edgar.get_filing_text` on each `url`. Long documents page — loop on
   `next_offset` until `truncated` is false. Do not analyze a partial document
   and do not pretend you did.

2. **Section the text** before diffing. Compare like against like:
   - Item 1A Risk Factors
   - Item 7 / MD&A
   - Critical accounting estimates
   - Revenue recognition and segment notes
   - Commitments, contingencies, legal proceedings
   - Related-party transactions

3. **Diff each section.** Write both texts to files under the scratchpad and
   use `diff` / `git diff --no-index --word-diff` — do not eyeball two long
   documents and do not summarize from memory.

4. **Classify every change** as one of:
   - **Added** — new risk, new contingency, new accounting policy
   - **Removed** — a disclosure that existed and now does not *(highest signal)*
   - **Hedged** — "will" → "may", "expects" → "believes", a number → a range
   - **Quantified/de-quantified** — a specific figure gained or lost
   - **Boilerplate** — counsel's annual refresh, no information

5. **Rank by information content.** Removals and de-quantifications first,
   boilerplate last or omitted entirely.

## Output

- **The three changes that matter**, quoted verbatim, before/after, with a
  sentence on what each implies.
- **Full change table:** section | type | before | after | read
- **Explicit statement of what did *not* change** where the market expected it to.
- **Kill-criteria trip check** (CLAUDE.md §4) — material weakness language,
  auditor change, restatement, related-party additions.
- Accession numbers for both filings so the diff is reproducible.

## Do not

- Do not report boilerplate as a finding. It destroys the signal.
- Do not paraphrase changed language — quote it. The wording is the evidence.
