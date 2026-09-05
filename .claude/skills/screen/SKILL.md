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
   hard bounds (market cap, geography, sector in/out) *before* anything else.
   State explicitly how many names you started from and how you got the list.
   If the starting list came from the user, say so — do not imply breadth you
   do not have.

2. **Pull the data.** `market.comps_table` for the candidate symbols, in
   batches of ≤15. For any metric that will drive an include/exclude decision,
   verify against `edgar.xbrl_concept` before relying on it — yfinance is
   secondary (CLAUDE.md §7).

3. **Apply criteria in cost order.** Cheap numeric filters first, then the
   gates that need a filing read. Record the count surviving each step so the
   funnel is auditable.

4. **Apply the cheap kill criteria.** From CLAUDE.md §4, two are checkable
   without a full read and should run here:
   - net insider selling > $10M trailing 6 months → `edgar.insider_transactions`,
     count only transaction codes **P** and **S**
   - share count growing >4%/yr → `edgar.xbrl_concept` on
     `CommonStockSharesOutstanding` or `dei:EntityCommonStockSharesOutstanding`

5. **Rank** by the criterion the user actually cares about. If they did not
   say, rank by 3-year revenue CAGR × gross margin and say that is what you did.

## Output

A table, then the funnel, then next steps:

| # | Ticker | Name | Mkt cap | EV/NTM Rev | Rev growth | GM | FCF margin | Net debt/EBITDA | Insider % | Flags |

- **Funnel:** `342 in universe → 88 pass sector/size → 31 pass growth+margin → 12 pass leverage → 9 clear cheap kills`
- **Flags:** any `UNKNOWN` gate or tripped kill criterion, named.
- **Next:** the 3 you would take to `/diligence-checklist` and one sentence each on why.
- **Source row** on every table (CLAUDE.md §8).

Append the run to `universe/coverage.md` under "Screen history" with the date,
criteria, and surviving names, so repeat screens are diffable.

## Do not

- Do not present a screen as a recommendation. It is a candidate list.
- Do not silently drop a name that errored. List it under `errors`.
- Do not extend beyond the mandate because a name looks good.
