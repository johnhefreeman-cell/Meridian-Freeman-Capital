---
name: screen
description: Run a quantitative screen against the coverage universe using the fund's quality gates. Use when the user asks to find, screen, or filter for names matching criteria (growth, margin, leverage, valuation, insider ownership), or says "/screen".
---

# Screen

Turn a criteria sentence into a ranked candidate list that already respects
the mandate. Screening is how names *enter* the funnel; nothing leaves this
skill as a position, only as a candidate for `/diligence-checklist`.

## Inputs

Either a criteria sentence ("software, >20% growth, >70% gross margin, net
cash") or a starting ticker list. If neither is given, ask for one — do not
invent a universe.

## Procedure

1. **Bound the universe.** Read `universe/coverage.md`. Apply the CLAUDE.md §2
   bounds *before* anything else: geography, and the strategy exclusions
   (pre-revenue, unverifiable economics). **There is no market-cap band** —
   size is handled by the liquidity gate in step 4, not here.
   State explicitly how many names you started from and how you got the list.
   If the starting list came from the user, say so — do not imply breadth you
   do not have.

2. **Assign a business type to every candidate** (CLAUDE.md §3.0): A recurring,
   B asset-heavy, C financial, D resource. The type decides which gate
   thresholds apply, and screening a bank on gross margin is how you throw away
   a good name for a meaningless reason. Segment the candidate list by type and
   run each segment against its own column.

3. **Pull the data.** `market.comps_table` for the candidate symbols, in
   batches of ≤15. For any metric that will drive an include/exclude decision,
   verify against `edgar.xbrl_concept` before relying on it — yfinance is
   secondary (CLAUDE.md §7).

4. **Apply criteria in cost order**, against the type's column in the CLAUDE.md
   §3.1 matrix. Cheap numeric filters first, then the gates that need a filing
   read. Record the count surviving each step so the funnel is auditable.

5. **Apply the liquidity gate** (CLAUDE.md §2.1). Compute
   `max position = 10 days × 25% × 20-day median daily dollar volume` from
   `market.price_history`, and report it per name. This is what replaces a
   market-cap floor: a $120M name is not excluded for being small, it is
   excluded when the position you would want does not fit in the tape.

6. **Apply the cheap kill criteria.** From CLAUDE.md §4, two of the universal
   ones are checkable without a full read and should run here:
   - net insider selling > $10M trailing 6 months → `edgar.insider_transactions`,
     count only transaction codes **P** and **S**
   - share count growing >4%/yr → `edgar.xbrl_concept` on
     `CommonStockSharesOutstanding` or `dei:EntityCommonStockSharesOutstanding`

7. **Rank** by the criterion the user actually cares about. If they did not
   say, rank by 3-year revenue CAGR × gross margin for types A and B, and by
   3-year growth in tangible book value per share for types C and D — and say
   which you used. Do not rank across types on one blended metric.

## Output

A table, then the funnel, then next steps:

| # | Ticker | Name | Type | Mkt cap | ADDV | Max position | Primary multiple | Growth | Unit econ | Leverage | Insider % | Flags |

Report the **primary multiple, unit-economics and leverage columns in the
type's own terms** (CLAUDE.md §5): EV/NTM Rev and GM for A; EV/EBITDA and ROIC
for B; P/TBV and ROTCE for C; mid-cycle EV/EBIT and cost-curve quartile for D.
A single blended table across types is not comparable and should not be built.

- **Funnel:** `342 in universe → 310 in mandate → 31 pass type gates → 18 pass liquidity → 9 clear cheap kills`
- **Flags:** any `UNKNOWN` gate or tripped kill criterion, named.
- **Next:** the 3 you would take to `/diligence-checklist` and one sentence each on why.
- **Source row** on every table (CLAUDE.md §8).

Append the run to `universe/coverage.md` under "Screen history" with the date,
criteria, and surviving names, so repeat screens are diffable.

## Do not

- Do not present a screen as a recommendation. It is a candidate list.
- Do not silently drop a name that errored. List it under `errors`.
- Do not extend beyond the mandate because a name looks good.
- Do not screen a Type C or D name on Type A metrics. Gross margin on a bank
  and EV/EBITDA on an insurer are not conservative — they are meaningless.
