---
name: comps
description: Build a comparable-company table with EV/Revenue, EV/EBITDA, P/E, growth, margins and Rule of 40. Use when the user asks for comps, a comp table, relative valuation, "how does X trade vs peers", or says "/comps".
---

# Comps

A comp table is an argument about *who the peers are*, not a data dump. The
peer set is the analytical work; the multiples are arithmetic.

## Procedure

1. **Define the peer set and defend it.** For each peer, one clause on why it
   belongs: same demand driver, same business model, same margin structure.
   If the user supplied the list, still say which peers you consider weak
   comparisons and why. A peer set of convenience produces a median of nothing.

2. **Pull** `market.comps_table` with the full symbol list (≤15 per call).

3. **Verify the subject.** For the subject company, re-derive revenue, EBITDA,
   and share count from `edgar.xbrl_concept` and reconcile to the vendor
   figure. If they disagree by >2%, show both and use the filing (CLAUDE.md §7).

4. **Choose the primary multiple** by business type per CLAUDE.md §5 — do not
   default to P/E. Say which you chose and why in one line.

   | Type | Primary | Also show |
   | --- | --- | --- |
   | A · Recurring | EV/NTM Revenue vs. Rule of 40 | EV/FCF, net revenue retention |
   | B · Asset-heavy | EV/NTM EBITDA | FCF yield, ROIC vs. WACC |
   | C · Financial | P/TBV against ROTCE | Normalized P/E, CET1, dividend capacity |
   | D · Resource | Mid-cycle EV/EBIT | NAV at a stated deck, cost-curve position |

   **Peers must share the subject's type.** A comp set mixing a bank with a
   software business produces a median of nothing. For Type C, the useful
   comparison is the P/TBV-to-ROTCE relationship across the peer set, not the
   raw P/TBV — a bank at 1.0x TBV earning 6% ROTCE is expensive and one at
   1.8x earning 18% is not. For Type D, every peer must be shown at the *same*
   price deck or the multiples are not comparable.

5. **Normalize before comparing.** Note where a peer's figure is distorted by
   a large acquisition, a 53-week year, a fiscal-year offset, or SBC treatment.
   An unnormalized median is worse than no median.

## Output

Columns follow the type. For A and B:

| Ticker | Name | Mkt cap | EV | EV/NTM Rev | EV/EBITDA | FWD P/E | Rev growth | GM | EBITDA margin | FCF margin | Rule of 40 | Net debt/EBITDA |

For C: `Mkt cap | P/TBV | ROTCE | Normalized P/E | Efficiency ratio | CET1 | NPL ratio | Deposit cost`.
For D: `Mkt cap | EV | Mid-cycle EV/EBIT | NAV/share at deck | P/NAV | Cost-curve quartile | Reserve life | Net debt/mid-cycle EBITDA`.

Then:
- **Median / mean** across peers, and the subject's premium or discount to median.
- **The one-line read:** what the discount or premium is compensating for.
- **Implied value bridge:** subject at peer-median multiple → implied price →
  % from spot. Show the arithmetic.
- **Peer-set caveats:** the comparisons you consider weak.
- **Source row** and as-of date.

## Do not

- Do not report a median across fewer than 4 usable peers — say the set is too thin.
- Do not use a multiple the business type does not support (EV/EBITDA on a
  company with negative EBITDA, P/E on a loss-maker, EV/anything on a bank —
  enterprise value is not a meaningful concept where leverage is the product).
- Do not compare Type D names at different price decks.
- Do not treat "trades below peers" as a thesis. It is an observation.
