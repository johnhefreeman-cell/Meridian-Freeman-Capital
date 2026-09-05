# MRVL — Filing Diff & Insider Timeline

**Analyst:** filing-analyst · **Date:** 2026-09-05 · **Output format:** `/filing-diff`
**Reads:** `CLAUDE.md`, `research/names/MRVL/00-base-facts.md`, `.claude/skills/filing-diff/SKILL.md`

---

## 0. Conclusion first

The Q2 FY27 10-Q is where the disclosure changed, and it changed in one direction.
In a single quarter Marvell **admitted sole-source dependence on TSMC for every
advanced-node wafer**, **tripled unconditional foundry purchase commitments to
$8,518.9M**, and **deleted the paragraph that had quantified those capacity-reservation
commitments in each of the prior five quarters**. Three weeks after quarter-end it
issued a warrant for **58,970,907 shares** — 6.4% of diluted shares — to a single
unnamed customer, and disclosed **no fair value for it**, though it disclosed a fair
value for both smaller predecessor warrants.

Meanwhile revenue concentration through one channel counterparty went from 34% to
**45%**, against a customer book the company says runs on purchase orders, not
long-term commitments. That trips a CLAUDE.md §4 kill criterion.

Insiders sold **$47.3M net** (codes P/S only) over the trailing six months and bought
nothing. **$42.7M of that was under 10b5-1 plans** adopted before the disclosure changes,
so the §4 insider criterion is **not** tripped on its own terms.

**Filings reviewed in full — every document paged to `truncated: false`.**

| Filing | Period | Accession | Chars | Complete |
| --- | --- | --- | --- | --- |
| 10-Q | Q2 FY27 (2026-08-01) | `0001835632-26-000025` | 335,833 | yes |
| 10-Q | Q1 FY27 (2026-05-02) | `0001835632-26-000019` | 319,036 | yes |
| 10-K | FY26 (2026-01-31) | `0001835632-26-000011` | 491,099 | yes |
| 10-Q | Q3 FY26 (2025-11-01) | `0001835632-25-000197` | 304,139 | yes |
| 10-Q | Q2 FY26 (2025-08-02) | `0001835632-25-000189` | 297,641 | yes |
| 10-K | FY25 (2025-02-01) | `0001835632-25-000057` | 460,730 | yes |
| EX-99.1 | Q2 FY27 earnings release | `0001835632-26-000022` | 31,585 | yes |
| 8-K | CFO transition | `0001193125-26-267688` | — | yes |
| Form 4 | 123 filings, 2025-01-06 → 2026-09-02 | various | 601 txns parsed | 0 parse errors |

*Method note.* Texts were written to files and diffed with `diff`, per the skill. A
positional diff produced false "removals" caused by risk-factor **reordering** (the ESG
and "scale our business" risk factors appear moved, not deleted). All removals below were
re-tested with a number-blind set-difference + token-containment test and are confirmed
absent from the later document. One working copy of the FY26 10-K was corrupted
mid-session; all six documents were re-fetched, two consecutive fetches confirmed
byte-identical, and both 10-Qs were verified md5-identical to the copies the findings
were drawn from.

---

## 1. The three changes that matter

### 1.1 Sole-source TSMC dependence admitted; diversification claim withdrawn

Present in Q2 FY26 10-Q **and still in the FY26 10-K filed 2026-03-11**:

> "Most of our products are manufactured by third-party foundries located in Taiwan, and
> other sources are located in China, Germany, South Korea, Singapore and the United
> States."

Replaced in the Q2 FY27 10-Q (filed 2026-08-28):

> "Taiwan Semiconductor Manufacturing Company Limited ("TSMC") is currently our sole
> source foundry for all of our advanced process-node wafers."

> "In particular, TSMC is currently the sole wafer supplier for our advanced node
> products, including our 3nm products."

And newly added:

> "In particular, we have entered into a capacity reservation agreement with TSMC
> pursuant to which we agreed to make substantial advance payments in exchange for wafer
> capacity over a multi-year period. Under this arrangement, we are required to purchase
> specified target quantities of wafers during the term, and if we do not meet such target
> quantities, we may forfeit a proportional portion of our advance payments."

**Type: Removed + Added + De-quantified.** "TSMC" appears **0 times** in the FY25 10-K,
**0 times** in the FY26 10-K, **0 times** in the Q1 FY27 10-Q, and **5 times** in the Q2
FY27 10-Q. The assembly/test geography list also dropped China: "China, Malaysia,
Singapore, Taiwan and Canada" → "Malaysia, Singapore, Taiwan and Canada."

**Read.** A five-country supply diversification claim was withdrawn and replaced with a
single-supplier admission plus a take-or-pay forfeiture clause, in the same document. This
is not a boilerplate refresh; the earlier sentence was an affirmative statement of
diversification and it is gone.

### 1.2 The capacity-reservation quantification was deleted in the same quarter the commitment tripled

Present in Q2 FY26 10-Q and in the **Q1 FY27 10-Q** (filed 2026-05-28), verbatim from Q1 FY27:

> "The Company entered into manufacturing supply capacity reservation agreements with
> foundries and test and assembly suppliers in prior fiscal years. Under these
> arrangements, the Company agreed to pay capacity fees or refundable deposits to the
> suppliers in exchange for reserved manufacturing production capacity over the term of the
> agreements, which ranges from 4 to 10 years. In addition, the Company committed to
> certain purchase levels that were in line with the capacity reserved. The Company
> currently estimates that it has agreed to purchase level commitments of **at least $448.1
> million** of wafers, substrates, and other manufacturing products for the remainder of
> fiscal 2027 through fiscal 2033 under the capacity reservation agreements. In addition,
> total fees and refundable deposits payable under these arrangements are **$11.5 million**
> through fiscal 2028."

In the Q2 FY27 10-Q this paragraph **does not appear**. The phrase "agreed to purchase
level commitments of at least" returns 1 hit in Q2 FY26, 1 in Q1 FY27, **0 in Q2 FY27**.
The only surviving reference is the unquantified risk-factor phrase "substantial advance
payments."

What it was replaced by — the commitments table, which moved as follows:

| As of | Foundry & test/assembly purchase commitments | Prepayments on supply capacity reservation agreements |
| --- | --- | --- |
| 2025-08-02 (Q2 FY26) | $1,508.1M | $302.2M |
| 2026-01-31 (FY26 10-K) | $2,665.8M | $278.8M |
| 2026-05-02 (Q1 FY27) | $2,756.8M | $263.1M |
| **2026-08-01 (Q2 FY27)** | **$8,518.9M** | **$487.0M** |

*Source: 10-Q `0001835632-25-000189`; 10-K `0001835632-26-000011`; 10-Q `0001835632-26-000019`; 10-Q `0001835632-26-000025`.*

Forward tenor as of 2026-08-01: remainder FY27 $1,829.3M · FY28 $2,125.4M · FY29
$2,178.3M · FY30 $2,201.8M · FY31 $66.0M · thereafter $118.1M.

**Type: Removed / De-quantified.** The commitment rose **+$5,762.1M (+209%) in one
quarter** and the sentence that put a number on it was taken out in that same quarter.
There is no MD&A discussion of the increase; the only narrative reference is
"purchase commitments, see 'Note 7 – Debt,' and 'Note 9 – Commitments and Contingencies'."

**Read.** This is the highest-signal edit in the set. Marvell has locked ~$2.1–2.2B/yr of
unconditional supply purchases through FY30 against a demand book that the same 10-K
describes as: *"We typically sell products pursuant to purchase orders rather than
long-term purchase commitments. Some of our customers have, and others may in the future,
cancel or defer purchase orders on short notice without incurring a significant penalty."*
Committed on the supply side, uncommitted on the demand side, and the disclosure that let
you size it was withdrawn.

### 1.3 Customer concentration: 34% → 45%, and the sentence explaining it was deleted

FY25 10-K (filed 2025-03-12), immediately below the concentration table:

> "Net revenue attributable to Distributor A increased in fiscal 2025 and 2024 as they
> support customers in the data center end market, which has continued to experience robust
> demand."

FY26 10-K (filed 2026-03-11): **that sentence is gone.** The table remains; the
explanation does not.

Trajectory, as reported:

| Period | Customer A | Customer B | Distributor A |
| --- | --- | --- | --- |
| FY23 | <10% | — | 20% |
| FY24 | <10% | — | 24% |
| FY25 | 13% | — | 34% |
| FY26 | 14% | — | **37%** |
| Q1 FY27 (3 mo) | 16% | — | **45%** |
| Q2 FY27 (3 mo / 6 mo) | 16% / 16% | *(row removed)* | **44% / 45%** |

*Source: 10-K `0001835632-25-000057` p.8; 10-K `0001835632-26-000011`; 10-Q `0001835632-26-000019`; 10-Q `0001835632-26-000025`.*

Also removed from the Q2 FY27 table: the **entire "Customer B" row** and the
**"*Less than 10% of net revenue." footnote**. Customer B was 10% of revenue in Q2 FY25
and has fallen below the disclosure threshold.

**Read.** Nearly half of revenue now routes through one distributor. No multi-year
contract with Distributor A is disclosed anywhere in any of the six filings, and the
company's own language is that it sells on purchase orders. Marvell's own table is titled
"Net revenue attributable to **significant customers** including both distributor and
direct customers," so the company treats Distributor A as a customer. See §5 kill check.

---

## 2. Full change table

Ranked by information content. Boilerplate refreshes are excluded, not listed.

| # | Section | Type | Before | After | Read |
| --- | --- | --- | --- | --- | --- |
| 1 | 10-Q Item 1A, supply chain | Removed + Added | "Most of our products are manufactured by third-party foundries located in Taiwan, and other sources are located in China, Germany, South Korea, Singapore and the United States." | "TSMC is currently our sole source foundry for all of our advanced process-node wafers." + new take-or-pay forfeiture paragraph | Diversification claim withdrawn; single point of failure named for the first time |
| 2 | Note 9 Commitments | **Removed / de-quantified** | "...purchase level commitments of at least $448.1 million...total fees and refundable deposits...are $11.5 million through fiscal 2028." (Q1 FY27) | Paragraph absent | Commitment tripled to $8,518.9M in the same quarter the number was withdrawn |
| 3 | 10-K MD&A, concentration | **Removed** | "Net revenue attributable to Distributor A increased in fiscal 2025 and 2024 as they support customers in the data center end market..." | Sentence absent | Explanation deleted as concentration rose 34%→37%→45% |
| 4 | MD&A concentration table | **Removed** | "Customer B" row (10% of net revenue) + "*Less than 10% of net revenue." footnote | Rows absent | Second 10% customer fell below threshold; base narrows to one distributor |
| 5 | Note 3 Revenue / Item 1 | **Removed (granularity)** | Five end markets: Data center / Enterprise networking / Carrier infrastructure / Consumer / Automotive-industrial | Two: Data center / "Communications and other" | 28% of FY25 revenue collapsed into one line; change is disclosed (see below), not hidden |
| 6 | Note 15 Subsequent Event | **Added, not quantified** | n/a | Warrant for up to 58,970,907 shares at $206.58, 7-yr term, revenue-milestone vesting | Prior two customer warrants both disclosed grant-date fair value; this one — 11x larger — does not |
| 7 | Note 10 Stockholders' Equity | Added | n/a | NVIDIA $2.0B Series A Convertible Preferred, 21.8M as-converted at ~$91.84 | Competitor named in the 10-K 20 days earlier becomes a 2.4% as-converted holder |
| 8 | Item 1A, new risk factor | Added | n/a | "Advances in artificial intelligence could disrupt our business model..." (~22 sentences) | Company now warns AI may enable hyperscaler insourcing — the exact demand base it sells into |
| 9 | Item 1A, new risk factor | Added | n/a | "The rights, preferences and privileges of our preferred stock may adversely affect holders of our common stock..." | Dilution and NVIDIA influence acknowledged |
| 10 | Note 6 Fair Value | Added | n/a | Celestial contingent consideration, Level 3 Monte Carlo; $315.8M → $749.5M; max settlement ~$233.0M cash + ~22.4M shares | $433.7M H1 charge; this is what broke Q1 FY27 |
| 11 | Note 6 Fair Value | Added | n/a | $300.0M notional cash-settled forward stock purchase contract, entered April 2026 | Company now holds a derivative on its own stock to hedge an earnout |
| 12 | MD&A, geography | Quantified (worse) | Asia = 76% / 75% of net revenue (3mo/6mo FY26) | **Asia = 84%** (3mo and 6mo FY27) | +8pts in one year |
| 13 | Critical accounting estimates | Added | Estimate list omitted business combinations, government incentives | Both added; contingent-consideration inputs enumerated | Appropriate expansion, not a weakening |
| 14 | Note 7 Debt | Changed | $4,499.9M total borrowings (2026-01-31) | $4,999.9M; 1.650% 2026 Notes retired, new $1,000M 5.300% 2036 Notes | Cost of new money 5.30% vs 1.65% retired |
| 15 | MD&A, buyback | Changed | H1 FY26: 8.3M shares for $540.0M; $2.0B remaining | H1 FY27: 2.5M shares for $400.0M; $5.1B remaining | Authorization up 2.5x, execution down 26%, with $3.9B cash |
| 16 | Item 1A, government incentives | Hedged / de-quantified | "On May 1, 2025, we received notification that our application for government incentives...had been approved...from February 2, 2025, through February 1, 2030, qualifying expenditures...will result in the generation of credits..." | "certain jurisdictions...have enacted alternative incentive programs...We have entered into agreements with governmental agencies to secure such incentives" | Specific approved incentive, dated term, and mechanism replaced with generic plural language |

The end-market change (#5) **is** explained, and should be credited as such:

> "Beginning in the fourth quarter of fiscal 2026, the Company consolidated revenue
> previously reported separately as enterprise networking, carrier infrastructure, consumer
> and automotive/industrial end markets into a new communications and other end market...
> The composition of our data center end market remains unchanged."

Prior years were restated to the two-bucket format, so the historical series survives.
What is lost is *forward* visibility: from FY27 onward there is no way to tell from the
filings whether carrier, enterprise, or consumer is recovering or decaying.

---

## 3. The Q3 FY26 earnings anomaly — answered

Base facts flagged that 71% of FY2026 GAAP net income ($1,901.3M of $2,670.1M) landed in
Q3 FY26. The cause, verbatim from the FY26 10-K, Note 1 — Basis of Presentation:

> "On August 14, 2025, the Company completed the sale of its automotive ethernet business
> to Infineon Technologies AG for $2.5 billion in cash. During fiscal 2026, the Company
> recorded a pre-tax gain on sale of $1.8 billion, which is included in interest income and
> other, net in the Consolidated Statements of Operations."

And in MD&A:

> "We recognized interest and other income, net of $1.7 billion in fiscal 2026 as compared
> to interest and other loss, net of $174.4 million in fiscal 2025. The change was primarily
> due to the $1.8 billion gain on sale of our automotive ethernet business in the third
> quarter of fiscal 2026."

The cash flow statement carries the precise figure: **Gain on sale of business (1,830)**.
Note 5 adds that $524.7M of goodwill was derecognized on the sale.

**The clean earnings base.** Reported FY26 pre-tax income $3,046.6M; tax $376.5M; net
income $2,670.1M. Excluding the gain, **pre-tax income ex-gain = $1,216.6M (reported
$3,046.6M less reported $1,830.0M)**. The tax attributable to the gain is **not separately
disclosed**, so the after-tax clean number cannot be tied to a filing. At the reported
FY26 blended effective rate of 12.4%, clean net income ≈ **$1,066M `[EST]`**; if the gain
was taxed near the 21% statutory rate, clean net income ≈ **$1,216M `[EST]`**. Both are
estimates; the true figure sits between them. `bear-case` and `valuation` should use the
pre-tax $1,216.6M and state the tax assumption rather than adopt either point.

The gain is **below the operating line** — it is in "interest income and other, net," not
in operating income. GAAP operating income for FY26 is unaffected by it.

### And the Q1 FY27 collapse — also answered

Base facts flagged Q1 FY27 net income of only $34.5M. Cause, from the Q2 FY27 10-Q MD&A:

> "Interest and other loss, net increased by $226.4 million in the six months ended August
> 1, 2026 compared to the six months ended August 2, 2025. The increase was primarily due
> to a $433.7 million increase in fair value of the contingent consideration liability
> associated with the Celestial acquisition, partially offset by an unrealized gain of
> $131.0 million from the forward stock purchase contract..."

The Celestial earnout liability went **$315.8M at acquisition (2026-02-02) → $647.6M
(2026-05-02) → $749.5M (2026-08-01)**. Of the $433.7M H1 charge, $101.9M fell in Q2, so
**~$331.8M fell in Q1 FY27**. That is the whole of the Q1 shortfall.

This is a structural feature now, not a one-off. From Note 6:

> "Critical estimates and inputs used for the valuation of contingent consideration
> include forecasted revenue, probability of achievement, stock price volatility, the
> Company's stock price and other relevant assumptions and inputs... Under the contingent
> consideration arrangement, the maximum potential settlement is approximately $233.0
> million of undiscounted cash consideration and approximately 22.4 million shares of the
> Company's common stock."

At the $223.55 price in base facts, maximum settlement is roughly **$5.2B `[EST]`** against
a $749.5M carrying value. The better Celestial performs and the higher MRVL trades, the
larger the GAAP charge. Marvell's non-GAAP explicitly excludes it — the earnings release
defines non-GAAP to exclude "changes in fair value of contingent consideration liability
and forward stock purchase contract" — so non-GAAP EPS is blind to a liability with
several billion dollars of headroom.

---

## 4. Potential share issuance overhang (assembled from the filings)

Not disclosed anywhere as a single figure. Assembled here because base facts' share-count
work needs it.

| Instrument | Shares | Status | Source |
| --- | --- | --- | --- |
| NVIDIA Series A Preferred, as-converted | 21.8M | Issued 2026-03-31; **already in the 921.2M diluted count** | 10-Q Note 10/Note 12 |
| Celestial earnout, maximum | up to 22.4M | Contingent through FY29 | 10-Q Note 6 |
| FY25 customer warrant | 4.2M (1.2M vested) | Vesting on revenue milestones | 10-Q Note 3 |
| FY26 customer warrant | 1.0M (0 vested) | Vesting on revenue milestones | 10-Q Note 3 |
| **FY27 customer warrant** | **58,970,907** | Issued 2026-08-18, vests FY27–FY33 | 10-Q Note 15 / Item 5 |
| **Total contingent, not yet in diluted count** | **~86.6M** | ≈ **9.7%** of 897.4M basic | derived |

The FY27 warrant is the disclosure problem. Both predecessors were fully valued:

> FY25 warrant: "The grant date fair value of the warrant was determined to be **$54.44 per
> share** and a total fair value of **$227.6 million** using the Black-Scholes option pricing
> model."
> FY26 warrant: "...**$53.02 per share** and a total fair value of **$55.4 million** using the
> Black-Scholes option pricing model."

The FY27 warrant, 11x larger than both combined:

> "Subsequent to quarter end, the Company issued a warrant to a customer to purchase an
> aggregate of up to 59.0 million of the Company's common stock at an exercise price of
> $206.58 per share over a seven year term expiring in August 2033. The warrant is eligible
> for vesting from the Company's third quarter of fiscal 2027 through the end of fiscal
> 2033, upon meeting certain revenue milestone conditions or time-based conditions."

**No grant-date fair value. No total fair value. No stated accounting treatment.** The
predecessors' policy is that warrant shares "are recognized as a **reduction to revenue**
as qualifying revenues are recognized during the vesting term." If the same treatment
applies, this is a multi-billion-dollar contra-revenue item that has not been sized in any
filing. Item 5 gives the precise count and the commercial context:

> "On August 18, 2026, the Company issued a warrant...to purchase up to an aggregate of
> 58,970,907 shares of the Company's common stock at an exercise price of $206.58 per share,
> **in connection with a commercial agreement between the Company and the customer relating
> to the development of custom semiconductor products**."

**Open work item for `revenue-quality`:** obtain the Form 8-K Item 3.02 filed 2026-08-19
(`0001193125-26-356217`) and the warrant exhibit, and size the contra-revenue. Until then
gross margin trajectory is **UNVERIFIED** beyond 2Q27.

---

## 5. Kill-criteria trip check (CLAUDE.md §4)

| Criterion | Status | Evidence |
| --- | --- | --- |
| Net insider selling >$10M T6M **with no 10b5-1 plan disclosed at adoption** | **NOT TRIPPED** | $47.3M sold, but $42.7M under plans with adoption dates disclosed in the Form 4 footnotes. Non-plan portion $4.6M < $10M. See §6. |
| Auditor resignation / material weakness >2 quarters / revenue restatement | **NOT TRIPPED** | Deloitte & Touche LLP in both 10-Ks. ICFR effective at 2025-02-01 and 2026-01-31. Item 9 "Changes in and Disagreements with Accountants" is a date-refresh only. "material weakness" appears once in the FY26 10-K, inside Deloitte's standard ICFR opinion boilerplate. "going concern," "substantial doubt," "significant deficiency" = **0 occurrences across all six documents**. All "restate" hits are "Amended and Restated" agreement titles. |
| Serial "one-time" charges: non-GAAP add-backs >15% of GAAP opex in 3 of last 4 quarters | **TRIPPED on a literal read; NOT tripped on intent** | Total special items / GAAP opex: 2Q27 385.1/995.9 = **38.7%**; 1Q27 344.5/921.4 = **37.4%**; 2Q26 227.9/720.5 = **31.6%**. But the add-backs are overwhelmingly **stock-based compensation** ($310.3M of $385.1M in 2Q27) and **amortization of acquired intangibles** ($72.2M) — recurring structural items, not one-time charges. Genuinely episodic items (restructuring + "Other") were **$(2.8)M in 2Q27** and $76.7M in 1Q27, i.e. ~0.3% and 8.3% of opex. **Doctrine question for the PM:** read literally this criterion kills every large-cap semiconductor company. Recommend the criterion be scoped to episodic charges. Separately note SBC of $326.2M = **11.9% of 2Q27 revenue**, which is a genuine earnings-quality issue for gate 3. |
| Guidance missed 3+ times in 8 quarters | **NOT ASSESSED** | Requires the guidance-vs-actual series from 8-K earnings releases. Out of scope for a filing diff. Flagged to `bear-case`. |
| Related-party transactions material to earnings | **NOT TRIPPED** | "Related Party Transactions — **None.**" verbatim and unchanged in both the FY25 and FY26 10-K. No related-party note in either 10-Q. **Caveat:** NVIDIA is a strategic partner, a $2.0B preferred holder (~2.4% as-converted), and was listed as a direct competitor in the FY26 10-K 20 days before the investment. It sits below the 5% related-party threshold, so its absence is technically correct — but any commercial revenue between the two is not separately disclosed. Flag, not a trip. |
| Share count >4%/yr with no corresponding revenue-per-share growth | **NOT TRIPPED** | Confirms base facts: diluted shares +5.84% YoY, revenue/share +29.0%. The 921.2M diluted count already includes the 21.8M NVIDIA as-converted shares (two-class method). **But** ~86.6M further contingent shares are not in it — revisit when the FY27 warrant vests. |
| **Types A/B: customer concentration >25% from one customer with no multi-year contract** | **TRIPPED** | Distributor A = **44% (3 mo) / 45% (6 mo)** of net revenue, 2Q27. No multi-year contract with Distributor A is disclosed in any of the six filings. FY26 10-K: *"We typically sell products pursuant to purchase orders rather than long-term purchase commitments."* **Qualifier:** Distributor A is a channel counterparty, not necessarily one end customer; concentration of the underlying end demand is not disclosed. Marvell's own table labels it a "significant customer." Recommend the PM rule on whether a distributor counts. Under a plain reading of §4 it does. |

**Additional governance flag — not a §4 criterion, reported because it is material.**
Per the 8-K filed 2026-06-11: CFO Willem Meintjes "notified the Company on June 10, 2026 of
his decision to resign from his position effective as of June 15, 2026," having "served as
Chief Financial Officer since January 2023," with the standard statement that the
resignation "is not the result of any disagreement with the Company." He was replaced by
**Daniel Durn, who was at that moment a member of Marvell's Board and Chair of the Audit
Committee**, and who "resigned from the Board, including from all committees of the Board
on which he served, effective immediately, and was subsequently appointed...Chief Financial
Officer...effective June 15, 2026." The Audit Committee chair became the preparer of the
statements he had been overseeing. Given that Level 3 fair-value estimates now drive
reported earnings (§3), this is worth naming.

---

## 6. Insider transactions — codes P and S only

123 Form 4s parsed from XML, 601 transactions, **0 parse errors**. Codes across the full
file: M 350 (option exercise), F 161 (tax withholding), S 47, A 34 (grants), G 3, P 5,
J 1. Only **P and S** are counted below, per doctrine. Non-derivative only.

**Trailing 6 months (2026-03-05 → 2026-09-05): 23 sales, 0 purchases, net −$47.3M.**

| Insider | Title | Txns | Shares | Value | 10b5-1 | Plan adopted | Window |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bharathi Sandeep | President, Data Center Group | 4 | 122,550 | $15.6M | Yes | 2025-12-04 | 03-26 → 07-16 |
| Koopmans Chris | President and COO | 6 | 60,000 | $11.4M | Yes | 2026-01-05 | 04-06 → 09-01 |
| Murphy Matthew J | Chairman & CEO | 6 | 67,500 | $10.9M | Yes | 2025-12-16 | 03-26 → 08-17 |
| Meintjes Willem A | CFO (resigned 06-15) | 2 | 34,000 | $4.7M | Yes | 2026-01-09 | 04-15 → 05-15 |
| **Casper Mark** | **EVP & Chief Legal Officer** | **4** | **34,754** | **$4.0M** | **No** | — | **04-01 → 04-17** |
| **Durn Daniel** | **CFO (from 06-15)** | **1** | **2,250** | **$0.6M** | **No** | — | **06-23** |
| **Total** | | **23** | **321,054** | **$47.3M** | | | |

*Source: Forms 4, CIK 0001835632. 10b5-1 status from the `aff10b5One` XML element (1/0), corroborated by the footnote text on each filing. Values = shares × reported price per share.*

- **Plan-covered: $42.7M (90.3%).** Every plan carries an explicit adoption date in the
  Form 4 footnote — e.g. Murphy: *"Sales were made pursuant to a 10b5-1 Plan adopted by
  the Reporting Person on December 16, 2025."* That satisfies "disclosed at adoption."
- **Not plan-covered: $4.6M (9.7%).** Casper and Durn filed with `aff10b5One = 0` and no
  plan footnote. This is the discretionary figure, and it is below the $10M threshold.
- **Purchases: zero.** The last code-P activity was **2025-09-25**, when four officers
  reported buys at $78.03/$77.09 totalling $2.1M — same day, near-identical price,
  Section 16(b) matchability footnote. That pattern indicates plan/ESPP participation
  rather than discretionary accumulation; treat it as weak evidence either way. Trailing
  12-month net is −$45.8M.
- **Trailing 12 months: P = $2.1M, S = $47.9M, net −$45.8M.**

---

## 7. Combined filings-and-insider timeline

| Date | Event | Source |
| --- | --- | --- |
| 2025-04-07 | Definitive agreement to sell automotive ethernet to Infineon, $2.5B cash | 10-Q 2Q26 |
| 2025-08-14 | Sale completes | 10-K FY26 Note 1 |
| 2025-08-29 | **10-Q 2Q FY26.** Distributor A 34%; Customer B 10%; foundry commitments $1,508.1M; capacity-reservation paragraph quantified ($482.5M) | `0001835632-25-000189` |
| 2025-09-24 | Board authorizes +$5.0B buyback → $9.7B total | 10-Q 2Q27 Note 10 |
| 2025-09-25 | 4 officers report code-P buys, $2.1M at ~$78 | Forms 4 |
| 2025-12-02 | Celestial AI Agreement and Plan of Reorganization dated | 10-Q 2Q27 Note 4 |
| 2025-12-03 | **10-Q 3Q FY26.** $1,830.0M pre-tax gain booked — 71% of FY26 net income | `0001835632-25-000197` |
| **2025-12-04** | **Bharathi adopts 10b5-1 plan** | Form 4 footnote |
| **2025-12-16** | **Murphy (CEO) adopts 10b5-1 plan** | Form 4 footnote |
| **2026-01-05** | **Koopmans (COO) adopts 10b5-1 plan** | Form 4 footnote |
| **2026-01-09** | **Meintjes (CFO) adopts 10b5-1 plan** | Form 4 footnote |
| 2026-02-02 | Celestial closes, $3,533.7M total consideration incl. $315.8M contingent | 10-Q 2Q27 Note 4 |
| 2026-02-10 | XConn closes, ~$280M cash + 2.1M shares | 10-K FY26 |
| **2026-03-11** | **10-K FY26.** End markets 5→2. Distributor A 37%, **explanatory sentence removed**. NVIDIA listed as a direct competitor. Commitments $2,665.8M. ICFR effective; Deloitte unchanged | `0001835632-26-000011` |
| 2026-03-26/27 | Murphy and Bharathi begin selling under plans, ~$99 | Forms 4 |
| **2026-03-31** | **NVIDIA buys $2.0B Series A Preferred** (~$91.84 conv., 21.8M shares); strategic partnership announced | 10-Q 2Q27 Note 10 |
| **2026-04-01 → 04-17** | **Casper (Chief Legal Officer) sells $4.0M, no 10b5-1 plan**, $105.11–$135.50 | Forms 4 |
| 2026-04 | $300.0M notional forward stock purchase contract entered | 10-Q 2Q27 Note 6 |
| 2026-05-28 | **10-Q 1Q FY27.** AI-disruption and preferred-stock risk factors added. Distributor A **45%**. Net income $34.5M on the $331.8M earnout mark. Capacity-reservation paragraph **still present** ($448.1M) | `0001835632-26-000019` |
| 2026-06-10/15 | CFO Meintjes resigns; **Audit Committee Chair Daniel Durn leaves the Board and becomes CFO** | 8-K `0001193125-26-267688` |
| 2026-06-23 | Durn sells $0.6M, no plan | Form 4 |
| 2026-08-01 | 2Q FY27 ends. Commitments **$8,518.9M**; prepayments $487.0M; Distributor A 44%; Asia 84% | 10-Q 2Q27 |
| **2026-08-18** | **Warrant for 58,970,907 shares at $206.58 issued to a customer** | 8-K Item 3.02 / 10-Q Item 5 |
| 2026-08-27 | 2Q FY27 earnings release | `0001835632-26-000022` |
| **2026-08-28** | **10-Q 2Q FY27.** TSMC named sole-source for the first time; capacity-reservation quantification **removed** | `0001835632-26-000025` |
| 2026-09-01 | Koopmans sells $2.0M under plan | Form 4 |

### Reading the sequence — stated without overclaiming

The four most senior executives (CEO, COO, President of Data Center Group, CFO) all
adopted 10b5-1 plans inside a **five-week window, 2025-12-04 to 2026-01-09**. That window
opens the day after the Q3 FY26 10-Q that booked the $1.83B gain, and it straddles the
Celestial merger agreement. Selling under those plans began 2026-03-26 and has run
continuously since, into a share price that went from ~$99 to ~$299 and back to ~$203.

**The exculpatory facts, stated plainly.** Every plan observed a cooling-off period far
longer than the 90-day minimum (Bharathi: 112 days; Murphy: 100 days; Koopmans: 91 days;
Meintjes: 96 days). Adoption immediately after a Q3 print is the ordinary time to adopt.
Sales executed on fixed monthly schedules, including into weakness at $180 and $199. The
disclosure changes that matter most (§1.1, §1.2) appeared in the **Q2 FY27 10-Q filed
2026-08-28**, eight months after the plans were adopted — the executives could not
plausibly have been pricing an August 2026 disclosure change in December 2025. **No
inference of informed selling is drawn, and none is supported.**

**The one genuinely discretionary block.** Mark Casper, EVP & Chief Legal Officer, sold
34,754 shares for $4.0M on **2026-04-01, 04-02, 04-06 and 04-17** — the seventeen days
immediately following the NVIDIA preferred issuance on 2026-03-31 — with `aff10b5One = 0`
and no plan footnote on any of the four filings. His reported holdings fell to 4,023 shares
on 2026-04-02. This is the only meaningful non-plan selling in the window, it came from the
officer with the widest view of contractual matters, and it directly followed a
market-moving transaction. It is also **$4.0M**, well inside the kill threshold, and he
sold at $105–$135 into a stock that subsequently ran to $299 — which is the opposite of
what informed selling looks like. **Recorded as a fact on the timeline. No causal claim.**

---

## 8. What did *not* change, where the market expected it to

- **Auditor.** Deloitte & Touche LLP, both years. No Item 9 disagreement. No change in
  ICFR in any quarter. Given a CFO transition, two acquisitions, a $2.0B preferred issue
  and a new Level 3 earnout, an unqualified ICFR opinion with no change disclosure is
  genuinely reassuring and should be credited.
- **Contingencies and Legal Proceedings.** The note is **verbatim identical** between the
  Q2 FY26 and Q2 FY27 10-Qs. No new litigation, no new accrual, no change to the "does not
  expect...material adverse effect" conclusion.
- **Related Party Transactions.** "None." in both 10-Ks, unchanged.
- **Revenue recognition policy.** Unchanged in substance. Critical accounting estimates
  were *expanded* (business combinations, government incentives, contingent-consideration
  inputs), not narrowed.
- **Customer identity.** Marvell has **never** named Customer A or Distributor A, in any
  of the six filings. Requested full-text searches on customer names could not be run
  because **no 10%+ customer is named in any filing**. Searches for Amazon, Microsoft,
  Alphabet/Google, Oracle, Meta, Arrow, Avnet, WPG, WT Micro and Supermicro return zero
  substantive hits across all six documents. Any attribution of Distributor A or Customer
  A to a named company would violate §7 and is not made here.
- **The "we typically sell pursuant to purchase orders" language.** Unchanged, and it is
  the sentence that turns §1.2 and §1.3 into a real asymmetry rather than a curiosity.

---

## 9. Language searches — results

| Query | Result |
| --- | --- |
| "material weakness" | 1 hit in each 10-K, both inside Deloitte's standard ICFR audit-report language ("assessing the risk that a material weakness exists"). 0 in all four 10-Qs. **No company-identified material weakness.** |
| "restatement" | 1 hit in each 10-K, the Rule 10D-1 clawback checkbox on the cover page. 0 in the 10-Qs. All "restate/restated" hits are "Amended and Restated" agreement titles. **No accounting restatement.** |
| "going concern" | **0 occurrences** across all six documents. |
| "substantial doubt" | **0 occurrences** across all six documents. |
| Auditor change / "disagreement" | Item 9 is a pure date refresh. The 3 "disagreement" hits in each 10-K refer to a **commercial** matter: *"In the third quarter of fiscal 2025, the Company reserved $50.0 million in relation to a contractual disagreement with a customer that was influenced by the restructuring actions initiated by the Fiscal 2025 Plan...In the fourth quarter of fiscal 2025, the matter was resolved for an amount that was not materially different."* Resolved; not an auditor disagreement. |
| EDGAR `full_text_search`, all four phrases | For the current registrant **CIK 0001835632**, no 10-K/10-Q hits on material weakness, going concern or substantial doubt in any period. All MRVL-family hits belong to the **predecessor entity Marvell Technology Group Ltd (CIK 0001058057), 2007–2008** — the historic stock-option backdating era, a different registrant eighteen years ago. Not relevant to the current filer. |
| Largest-customer names | Not searchable — **no 10%+ customer is named in any filing** (see §8). |

---

## 10. Open items handed back

1. **Size the 58,970,907-share customer warrant.** Pull 8-K `0001193125-26-356217` (Item
   3.02, filed 2026-08-19) and the warrant exhibit. If the FY25/FY26 contra-revenue
   treatment applies, this is the single largest unquantified item in the filings.
   → `revenue-quality`
2. **Identify Distributor A's underlying end-customer concentration.** The §4 trip in §5
   turns on whether 45% through one distributor is 45% to one end customer. Not
   determinable from the filings.
   → `bear-case`
3. **Gate 1 (recurring/contracted revenue) is settled, and it fails.** The FY26 10-K states
   Marvell "typically sell[s] products pursuant to purchase orders rather than long-term
   purchase commitments," and no contracted-revenue or backlog percentage is disclosed in
   any period. Under §3.1 Type A (≥70% recurring or contracted) this is a **FAIL**, not an
   UNKNOWN. Base facts' open item #1 can be closed.
4. **Maturity wall — clear.** Debt inside 24 months: $499.9M (4.875% 2028) + $750.0M
   (2.450% 2028) = $1,249.9M against $3,932.8M cash. No wall. Partially closes base facts
   open item #5; EBITDA still needed for the ratio.
5. **Guidance-vs-actual series** for the §4 guidance criterion — requires 8 quarters of
   8-K releases.
   → `bear-case`

---

*Research only. Not advice, not a recommendation, not an order.*
