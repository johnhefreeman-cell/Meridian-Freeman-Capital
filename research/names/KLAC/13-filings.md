# KLAC — Filing Diff & Insider Timeline

**Analyst:** filing-diff agent · **Date:** 2026-09-05 · **Method:** `.claude/skills/filing-diff/SKILL.md`

**Documents compared (all paged to completion; raw HTML retained for table verification):**

| Doc | Period | Accession | Filed | Extracted chars |
| --- | --- | --- | --- | --- |
| 10-K FY26 | FYE 2026-06-30 | `0000319201-26-000027` | 2026-08-06 | 456,901 |
| 10-K FY25 | FYE 2025-06-30 | `0000319201-25-000024` | 2025-08-08 | 456,757 |
| 10-K FY24 | FYE 2024-06-30 | `0000319201-24-000021` | 2024-08-05 | 474,278 |
| 10-Q 3Q26 | 2026-03-31 | `0000319201-26-000016` | 2026-04-30 | 196,546 |
| 10-Q 2Q26 | 2025-12-31 | `0000319201-26-000008` | 2026-01-30 | 186,352 |
| 10-Q 1Q26 | 2025-09-30 | `0000319201-25-000034` | 2025-10-31 | 161,251 |
| 10-Q 3Q25 | 2025-03-31 | `0000319201-25-000012` | 2025-05-01 | 319,640 |
| 10-Q 2Q25 | 2024-12-31 | `0000319201-25-000006` | 2025-01-31 | 309,869 |
| 10-Q 1Q25 | 2024-09-30 | `0000319201-24-000027` | 2024-10-31 | 284,884 |

Source row: SEC EDGAR primary documents, fetched 2026-09-05. Each document's terminal signature
block and page number were verified present, so no diff below rests on a truncated read. Item 1
customer tables, the segment note and the revenue note were re-verified cell-by-cell against raw
HTML, not only against extracted text.

Fiscal year ends 30 June; FY26 = 2025-07-01 → 2026-06-30. Business type **B · Asset-heavy
operating** (per base facts). Currency USD millions.

---

## Conclusion first

One disclosure was removed and it is the one that matters. In the fiscal year backlog rose
**60% to $12.57bn**, KLA deleted the ASC 606 *Remaining Performance Obligations* note from the
financial statements — the note that had, for at least three years, given the RPO dollar amount,
the customer-deposit component inside it, and the percentage expected to convert to revenue in
the next 12 and 24 months. It was replaced by a table covering only **$1.78bn of contract
liabilities**, 14% of the stated backlog. The backlog number survives in Item 1; its **duration
and its cash backing do not**. That change is not boilerplate and it has no stated reason.

Everything else is intelligible and mostly favourable: segments unchanged, region-by-region MD&A
*expanded* (China 42.8% → 33.3% → 29.8%), factoring still fully quantified, customer names still
disclosed, PwC retained, ICFR effective, no material weakness, no restatement, no related-party
transactions. Insider selling is large — **$84.2M net sold, zero purchases, trailing 6 months** —
but **$82.6M of it was executed under Rule 10b5-1 plans disclosed at adoption**, confirmed three
ways. Only **$1.59M** of discretionary non-plan selling. **No kill criterion is tripped.**

---

## The three changes that matter

### 1. The Remaining Performance Obligations note was deleted in the year backlog rose 60%

**FY25 10-K, Note 2 — Revenue (verbatim, entire subsection):**

> **Remaining Performance Obligations**
> As of June 30, 2025, we had $7.86 billion of remaining performance obligations ("RPO"), which
> represents our obligation to deliver products and services, and primarily consists of sales
> orders where written customer requests have been received. This amount includes customer
> deposits of $643.2 million as disclosed in Note 4 "Financial Statement Components" and excludes
> contract liabilities of $1.71 billion as disclosed above. **We expect to recognize approximately
> 71% to 76% of these performance obligations as revenue in the next 12 months, 20% to 25% in the
> subsequent 12 months and the remainder thereafter, but this estimate is subject to constant
> change.**
> The amount of our RPO and timing of revenue recognition of our RPO are evaluated quarterly and
> are largely driven by multiple variables, many of which are beyond our control...

**FY26 10-K, Note 2 — Revenue (verbatim, what stands in its place):**

> The following table represents the transaction price for contracts that have not yet been
> recognized as revenue as of June 30, 2026, **which equals our contract liabilities**, and when
> the Company expects to recognize the amounts as revenue:
>
> | (In thousands) | Less than 12 months | 12 to 24 months | 24 months or greater | Total |
> | --- | --- | --- | --- | --- |
> | Contract liabilities | $1,537,028 | $163,356 | $74,755 | $1,775,139 |

**Verification.** The string "remaining performance obligation" occurs **3 times in the FY24 10-K,
2 times in the FY25 10-K, 3 times in the 3Q25 10-Q, and 0 times in the FY26 10-K and in all three
FY26 10-Qs.** The abbreviation "RPO" occurs 0 times in the FY26 10-K body. Confirmed by
case-insensitive occurrence count on raw HTML and on extracted text.

**Read.** The FY25 note said explicitly that RPO of $7.86bn **excludes** contract liabilities of
$1.71bn. The FY26 note asserts the unrecognized transaction price **equals** contract liabilities
of $1.78bn. The scope of the ASC 606 disclosure therefore narrowed by ~86%, from $7.86bn to
$1.78bn, in the same year Item 1 backlog went $7.86bn → $12.57bn. An investor can no longer
compute how much of a $12.57bn backlog converts inside twelve months. That is exactly the ratio
you need to underwrite a WFE cycle. There is no stated reason for the change, and the
practical-expedient list in Note 1 was not amended to explain it.

**Corroborating divergence, same filing:** customer deposits **fell 32%**, from $636.4M to
$430.1M, while backlog rose 60%. Deposits as a share of backlog went **5.1% → 3.4%**. Backlog
grew faster than the cash customers put behind it.
`[10-K FY26 0000319201-26-000027, Item 1 "Backlog" and Note 4; 10-K FY25 0000319201-25-000024, Note 2 and Note 4]`

### 2. The backlog conversion schedule was also stripped from Item 1, and the reason narrative changed direction

**FY25 10-K, Item 1 — Backlog (verbatim):**

> Our backlog, primarily consisting of sales orders where written customer requests have been
> received, decreased from $9.83 billion as of June 30, 2024, to $7.86 billion as of June 30,
> 2025, as many of our capacity constrained suppliers made new investments to meet our growing
> needs, enabling us to deliver products more quickly than in the pandemic and early post-pandemic
> periods. Lead-time expectations, particularly from our largest customers, reverted to historical
> levels from the elevated lead times driven by the post-pandemic induced supply chain
> disruptions, and demands from a large number of new fabs in Asia normalized following multiple
> years of strong deliveries. **We expect to recognize approximately 71% to 76% of this amount as
> revenue in the next 12 months, 20% to 25% in the subsequent 12 months and the remainder
> thereafter, but this estimate is subject to constant change.** The amount of backlog and timing
> of revenue recognition is driven by multiple variables...

**FY26 10-K, Item 1 — Backlog (verbatim, in full):**

> Our backlog, primarily consisting of sales orders where written customer requests have been
> received, increased from $7.86 billion as of June 30, 2025, to $12.57 billion as of June 30,
> 2026, due to strong demand driven by the AI infrastructure buildout. The amount of backlog and
> timing of revenue recognition are driven by multiple variables, many of which are beyond our
> control, such as lead-time expectations, changes in government regulations, the readiness of
> customer fabs, end market needs for capacity, changes in the estimated versus actual start time
> of customers' projects, timing of delivery and installation dates and supply chain constraints.
> As customers try to balance the evolution of their technological, production or market needs
> with the timing and content of orders placed with us, there is increased risk of order
> modifications, pushouts or cancellations. Our backlog on any particular date does not provide
> meaningful information about the timing of future revenue recognition.

**Read.** Both the ASC 606 note and the Item 1 narrative lost the conversion percentages in the
same filing. The retained sentence — "Our backlog on any particular date does not provide
meaningful information about the timing of future revenue recognition" — was previously accompanied
by a quantified estimate that did provide exactly that information. FY24 disclosed 59%–64% in 12
months; FY25 disclosed 71%–76%; FY26 discloses nothing. Backlog is now **0.93x revenue** versus
0.65x in FY25, so the duration question is materially larger and the answer is materially smaller.

### 3. The tariff materiality qualifier was dropped, and the DRAM cost warning was extended a full year

**FY25 10-K, Item 1 — Government Regulations (verbatim):**

> The recent imposition of tariffs by the U.S. government ("U.S. Tariffs"), along with
> countermeasures taken by foreign countries, have had an adverse impact on our results of
> operations, **although the impact was not material in fiscal year 2025.** There is uncertainty
> around the ultimate duration, size and substance of the tariffs, including reciprocal actions
> against the U.S. by other countries.

**FY26 10-K, Item 1 — Government Regulations (verbatim):**

> Regulations that impact trade, including the imposition of export controls and tariffs, have had
> an adverse impact on our results of operations. Such actions by the U.S. government or another
> country could significantly impact our ability to provide products and services to existing and
> potential customers, especially in China, and adversely affect our business, financial condition
> and results of operations.

The same qualifier was dropped in MD&A. FY25 Executive Summary: *"...have had an adverse impact on
our results of operations, **though the impact was not material in fiscal year 2025**."* FY26:
*"geopolitical factors, including government regulations and tariffs, have impacted our results of
operations and may continue to do so."* **KLA no longer states that the tariff impact is
immaterial.** It also does not state that it is material. The FY26 gross-margin bridge does confirm
tariffs are now a named negative: *"Other service and manufacturing costs included higher
installation and warranty costs and increased costs due to tariffs, partially offset by lower
inventory-related charges."*

**And the DRAM escalation, quarter by quarter (verbatim, same risk factor):**

- 2Q26 10-Q (2026-01-30): *"Our efforts to procure these chips also contributed to an increase in
  purchase commitments in the second quarter of fiscal 2026. We estimate that the additional costs
  to procure these DRAM chips will have an adverse impact on our gross margin in **calendar
  2026**."*
- 3Q26 10-Q (2026-04-30): *"Our efforts to procure these chips have contributed to an increase in
  purchase commitments in fiscal 2026. We estimate that the additional costs to procure these DRAM
  chips will **continue to** have an adverse impact on our gross margin in **calendar 2026**."*
- FY26 10-K (2026-08-06): *"Our efforts to procure these chips contributed to an increase in
  purchase commitments in fiscal 2026. We estimate that the additional costs to procure these DRAM
  chips will continue to have an adverse impact on our gross margin in **fiscal 2027**."*

**Read.** The horizon moved from calendar 2026 to fiscal 2027 (through 2027-06-30) between the
January filing and the August filing. Corroborated by purchase commitments: **$2.29bn → $2.31bn →
$2.38bn → $2.42bn → $2.50bn → $2.75bn → $4.83bn → $5.97bn** across 1Q25 through FY26 year-end
(+147% YoY, with the step change in 3Q26). MD&A adds the new sentence: *"We have also increased our
purchase commitments, in part to secure the supply of key components, which may affect the timing
and magnitude of our costs and working capital requirements."*

---

## Full change table

| # | Section | Type | Before (FY25 / prior 10-Q) | After (FY26 / current) | Read |
| --- | --- | --- | --- | --- | --- |
| 1 | Note 2 Revenue | **Removed** | "Remaining Performance Obligations … $7.86 billion … includes customer deposits of $643.2 million … and excludes contract liabilities of $1.71 billion … approximately 71% to 76% … in the next 12 months, 20% to 25% in the subsequent 12 months" | Subsection absent. Replaced by contract-liability timing table totalling $1,775,139 thousand | **Highest signal.** Disclosed unsatisfied obligation narrowed 86% ($7.86bn → $1.78bn) as backlog rose 60% |
| 2 | Item 1 Backlog | **De-quantified** | "We expect to recognize approximately 71% to 76% of this amount as revenue in the next 12 months, 20% to 25% in the subsequent 12 months and the remainder thereafter" | Sentence deleted | Backlog duration unknowable at 0.93x revenue |
| 3 | Note 4 Financial Statement Components | Quantified (adverse) | Customer deposits $636,369 | Customer deposits $430,128 | −32% deposits against +60% backlog; deposits/backlog 5.1% → 3.4% |
| 4 | Item 1 Government Regulations; MD&A Exec Summary | **Hedged** | "although the impact was not material in fiscal year 2025" | Qualifier deleted; "have had an adverse impact on our results of operations" | Materiality assertion withdrawn without replacement |
| 5 | Item 1A supply risk | Quantified (adverse) | 2Q26: "adverse impact on our gross margin in calendar 2026" | FY26 10-K: "will continue to have an adverse impact on our gross margin in fiscal 2027" | Cost headwind extended ~12 months |
| 6 | MD&A Material Cash Requirements | Quantified (adverse) | Purchase commitments $2.42bn | $5.97bn, "a majority of which will be due within the next 12 months" | +147%; DRAM pre-buy; working-capital and obsolescence exposure |
| 7 | MD&A Factoring | Quantified (adverse) | Receivables sold under factoring $230,552; LC proceeds $55,525 | $515,480; $86,020 | +124% factoring. **Still fully disclosed** — not de-quantified |
| 8 | Schedule II | Quantified (adverse) | Allowance additions $11,494; write-offs $(10,261) | Additions $28,398; write-offs $(31,383) | Provision +147%, write-offs +206%. Ties to MD&A "provision for credit losses of $22.7 million" in SG&A |
| 9 | Note 2 Revenue table | **Added** | Long-term accounts receivable, net: $0 (FY25 and FY24) | $180,729 | New line item. AR extended beyond one year for the first time in three years |
| 10 | Item 1 Industry | **Removed** | Full paragraph: "Regionalization of semiconductors has become a trend as access to semiconductors is viewed from the lens of national security. China remains as a major region for the manufacturing of legacy node logic and memory chips… Although China is currently seen as an important long-term growth region…" | Paragraph deleted; replaced with AI/HPC demand paragraph | China narrative removed from Item 1. **But** see "What did not change" — China detail was *expanded* in MD&A and Item 1A |
| 11 | MD&A Exec Summary | **Removed** | Paragraph incl. "The inability to obtain export licenses has resulted in a reduction to our backlog and required us to return some deposits received from customers in China for purchase orders…" | Deleted from MD&A | Survives verbatim in Item 1A risk factors — presentational, not a net removal, but note the deposit/backlog link disappeared from MD&A in the year deposits fell 32% |
| 12 | Item 1A (new) | **Added** | — | "AI-driven design, verification, testing, process-node development, chip-based architectures, advanced packaging and novel materials science may compress semiconductor development cycles, lower barriers to entry, accelerate vertical integration or insourcing by customers or other technology companies, change inspection and metrology requirements, shorten the useful commercial life of existing products, reduce returns on our R&D investments, or render certain product lines, manufacturing processes or IP less valuable or obsolete" | First time KLA names AI as a threat to its own moat, not only a demand driver. Directly relevant to gate 6 |
| 13 | Item 1A (new) | **Added** | — | "Heavy investments in the capacity and infrastructure needed to support AI-driven semiconductor growth have elevated our customers' capital spending. While AI adoption is likely to continue and grow, the sustainability of such elevated investments cannot be assured." + "we may purchase or commit to purchase inventory, manufacturing capacity or other resources that do not materialize" | Management's own framing of the backlog/purchase-commitment risk |
| 14 | Item 1A (new) | **Added** | — | "Changes in demand for semiconductor chips due to changes in the timing, level of investment in, or technologies used in the buildout of data centers" | AI-capex concentration named as a distinct risk |
| 15 | 3Q26 10-Q Item 1A | **Added** | — | "Recently, some of our products destined for China have been held up by U.S. Customs and Border Protection due to questions about the nature of the customer or about the capabilities of our products. We cannot make any assurance that products that have been held up will be cleared for shipment in a timely manner or without a license." | New in 3Q26, absent from 1Q26/2Q26. Physical shipment interdiction, not just licensing |
| 16 | Item 1A / Item 9A | **Added** | ERP mentioned only as generic system risk | "We are currently upgrading our ERP system, with implementation expected to be completed in the first quarter of fiscal year 2027." New summary bullet: "System failures, **ERP system implementation risks**…could disrupt our operations and financial reporting processes" | ICFR watch item for FY27 Q1. Item 9A reports **no change** in ICFR in 4Q26 |
| 17 | Note 15 Commitments (new) | **Added** | — | "We have a duty drawback program… Our accounting policy is to recognize a receivable for a tariff refund upon submission of a qualifying claim to U.S. Customs and Border Protection… we do not expect the impact to be material." | New policy following the Feb-2026 Supreme Court IEEPA ruling. Refund receivable recognised on *submission*, not on approval. Unquantified — monitor |
| 18 | Item 1A tariffs | **Added** | — | "In February 2026, the U.S. Supreme Court ruled that tariffs imposed under the International Emergency Economic Powers Act were not authorized, creating uncertainty around the status of prior tariffs, potential refund processes and the scope of future presidential tariff authority." | First appears 3Q26 10-Q |
| 19 | Item 1 Manufacturing | **De-specified** | "Our principal manufacturing activities occur in the U.S., Singapore, Israel, Germany, U.K., Italy and China." | "…occur in the U.S., Singapore, Israel, China and various locations throughout Europe." | Country-level footprint replaced by "Europe". Same de-specification repeated in the segment note |
| 20 | Item 1 Sales offices | **De-specified** | "…subsidiaries or branches in many regions; some of the largest include China, Germany, Israel, Japan, Korea, Singapore, Taiwan and the U.K." | "…in major semiconductor manufacturing regions around the world to support our global customer base." | Named jurisdictions deleted |
| 21 | MD&A Liquidity | **De-quantified** | "$1.11 billion of our $4.49 billion … held by our foreign subsidiaries. We currently intend to indefinitely reinvest $66.6 million … we would be required to accrue and pay state and foreign taxes of approximately **1%-22%** of the funds repatriated … We have accrued state and foreign tax on the remaining cash of $1.04 billion of the $1.11 billion" | "$735.1 million of our $4.90 billion … held by our foreign subsidiaries and branch offices. We have recorded appropriate provisions for income or withholding taxes that may result from future repatriations of this balance." | Repatriation tax-rate range and indefinite-reinvestment split removed. Modest signal; the balance itself is still given |
| 22 | Item 1A / 10-Q format | Structural | 10-Qs reprinted full risk factors (~123,000 chars in 1Q25–3Q25) | 10-Qs carry only changed risks (17,303 / 18,007 / 26,477 chars in 1Q26–3Q26) | Changed with 1Q26. Permitted under Part II Item 1A. **Materially helpful**: what remains is the delta, and the delta is where findings 15, 16, 18 came from |
| 23 | MD&A / Note 7 | **Added** | — | "$2.00 billion in fixed-rate debt that was swapped to floating-rate debt"; new summary bullet "Our interest rate hedging activities expose us to risks related to changes in floating interest rates" | New in FY26. 100bp move = $20.0M annual interest expense |
| 24 | MD&A Exec Summary | **Added** | — | "On June 11, 2026, the Company effected a ten-for-one stock split… Share and per share information throughout this Annual Report on Form 10-K have been retroactively adjusted" | **Base-facts implication:** all per-share data in FY26 filings is post-split. FY26 diluted EPS $3.66 vs FY25 $3.04 as restated (FY25 10-K reported $30.37) |
| 25 | Notes 6 and 10 | Roll-off (not a removal) | FY25 Note 6 "Business Combinations and Dispositions" (all FY2023 content); 12 mentions of "non-controlling interest" (Orbograph, FY2023) | Note absent; 0 mentions of NCI | Both relate solely to FY2023, which drops out of the three-year presentation. **Not** a quiet deletion — stated here so the note renumbering (20 notes → 19) is not misread |
| 26 | Item 1 / MD&A customer table | Roll-off (not a removal) | FY25 table: TSMC in 2025, 2024, 2023 columns; Samsung Electronics Co., Ltd. in the **2023** column only | FY26 table: TSMC in 2026, 2025, 2024. No Samsung | Verified cell-by-cell in raw HTML across FY24/FY25/FY26. FY24 10-K shows Samsung last exceeded 10% in FY2023. FY26 simply drops the FY2023 column. **Not** a deleted customer name |

---

## What did *not* change, where the market might expect it to have

- **Customer names are still disclosed.** Taiwan Semiconductor Manufacturing Company Limited is
  named in Item 1 and in MD&A for all three years presented. This is the opposite of the AMAT
  pattern.
- **Customer concentration is still quantified and it is flat.** *"In each of the fiscal years
  ended June 30, 2026 and 2025, one customer accounted for approximately 19% of total revenues. In
  the fiscal year ended June 30, 2024, one customer accounted for approximately 13% of total
  revenues."* 19% in both FY26 and FY25 — **below the 25% §4 kill threshold and not rising.**
- **Region-by-region MD&A was expanded, not deleted.** FY25 gave one narrative paragraph and
  whole-number percentages. FY26 gives one-decimal percentages plus four separate region
  paragraphs: China $4,048.4 / 29.8% (FY25 33.3%, FY24 42.8%), Taiwan +13.7%, Korea +26.2%, North
  America +29.0%. China is explained verbatim: *"Revenue in China was comparable to the prior
  fiscal year, as continued investments in legacy-node technologies by domestic semiconductor
  companies were largely offset by export control restrictions affecting certain advanced
  technology transactions."*
- **Receivables factoring is fully quantified in every period.** 10-K FY26 gives $515,480 vs
  $230,552 vs $254,889; every FY26 10-Q gives the quarterly and nine-month figures. No
  de-quantification, no deletion.
- **Segment definitions are unchanged.** Three reportable segments, same names, same descriptions,
  same CODM measure ("segment profit (loss) represents segment income (loss) before income taxes,
  and excludes interest expense, other expense (income), net, restructuring costs…"). Segment
  revenue and segment profit reconciliations intact. Nothing was collapsed.
- **Product/service disaggregation is intact and expanded.** Six product categories (Wafer
  Inspection, Patterning, Specialty Semiconductor Process, PCB and Component Inspection, Services,
  Other) with dollars and percentages for three years. Services $3,125.9M, **23% of total revenues
  in FY26** vs 22% in FY25 — this is the number gate 1 needs.
- **Export-control disclosure grew.** "export control" occurrences: FY24 7 → FY25 8 → FY26 11.
  "Entity List" stable at 4–5. China revenue percentage still given in the risk factor: *"30%, 33%
  and 43% for fiscal years 2026, 2025 and 2024."*
- **Litigation note is word-for-word identical** to FY25. No new matter, no accrual disclosed.
- **Auditor unchanged.** PricewaterhouseCoopers LLP for both years; ICFR audited and effective.
  No Item 4.01 or 4.02 8-K filed since at least 2024-01-01.
- **No related-party transactions.** Zero occurrences of "related part" in the FY25 and FY26 10-Ks
  and in all FY26 10-Qs. The FY24 disclosure related to directors' other board seats and lapsed
  with board turnover.
- **Capital return was raised, not trimmed.** 8-K 2026-03-12 (`0001193125-26-102999`): dividend
  level raised 21% to $2.30/share pre-split, new $7.00bn repurchase authorisation on top of $3.94bn
  remaining. $9.74bn authority as of 2026-06-30. FY26 repurchases $2.29bn, dividends $1.06bn.
  Net leverage 0.53x against a 3.25x covenant.

---

## Combined filings + insider timeline

Insider figures parsed from **102 raw Form 3/4/5 XML documents** downloaded from EDGAR
(2025-03-01 → 2026-09-05). Codes P and S only; A/F/M/J/G excluded. The 10-for-1 split of
2026-06-11 changes share counts but not dollar values.

| Date | Event | Detail |
| --- | --- | --- |
| 2025-08-08 | **10-K FY25 filed** (`0000319201-25-000024`) | Backlog $7.86bn, RPO note present with 71–76% / 20–25% conversion schedule. Tariff impact "not material in fiscal year 2025" |
| 2025-08-12 → 09-05 | Insider sales | Lorig $7.35M, Wallace $9.87M, Higgins $2.02M, Khan $12.09M + $4.11M — **all under 10b5-1 plans**, all pre-6M window |
| 2025-10-31 | **1Q26 10-Q** (`0000319201-25-000034`) | Risk factors switch to delta-only format (123k → 17k chars). Item 408(a): *"no director or officer … adopted or terminated"* a plan. Adds Sept-2025 "Affiliates Rule" |
| 2025-11-11 | Insider sale | Wallace $13.00M @ $1,203.10, under plan |
| 2025-11-20 | **10b5-1 plan adopted** — Richard Wallace, CEO | Disclosed in 2Q26 10-Q Item 5. 392 days, max 71,398 shares (pre-split) |
| 2026-01-30 | **2Q26 10-Q** (`0000319201-26-000008`) | **First DRAM disclosure**: suppliers discontinued DRAM chips, "dramatic increase in the prices", adverse GM impact in **calendar 2026**. Affiliates Rule suspended to Nov-2026. Purchase commitments $2.75bn |
| 2026-02-02 / 02-18 | **10b5-1 plans adopted** — Wilkinson (CLO), Kirloskar (CAO) | Disclosed in 3Q26 10-Q Item 5 |
| 2026-03-11/12 | **8-K** (`0001193125-26-102999`) | Investor day. Dividend +21% to $2.30 pre-split; new $7.0bn buyback |
| 2026-04-30 | **3Q26 10-Q** (`0000319201-26-000016`) | **New:** products "held up by U.S. Customs and Border Protection"; Feb-2026 Supreme Court IEEPA ruling; ERP upgrade to complete 1Q FY27. Purchase commitments jump to **$4.83bn** (+76% QoQ). DRAM GM impact now "continue to". Factoring 9M $286.2M vs $143.4M |
| **2026-05-11** | **Discretionary sales, NO 10b5-1 plan** | **Jeneanne Hanley (Director) 550 sh @ $1,874.71 = $1.03M** and **Virendra Kirloskar (CAO) 297 sh @ $1,879.02 = $0.56M.** `aff10b5One = false`, no plan footnote on either Form 4 (acc. `0001193125-26-219897`… `-219368`, `-219364`). **Total non-plan selling: $1.59M** |
| 2026-05-11 → 05-14 | **10b5-1 plans adopted** — Higgins (CFO), Khan, Lorig | Disclosed in 10-K FY26 Item 9B. 446/285/287 days; max 202,480 / 253,159 / 122,773 shares (post-split). These plans authorise the August selling below |
| 2026-05-12 | Insider sale | Wallace $8.09M, under the Nov-2025 plan |
| 2026-06-11 | **Stock split effective** (8-K `0001193125-26-269375`, Item 5.03) | 10-for-1. Same day: Wallace $9.99M sale under plan |
| 2026-07-01/02 | Insider sales | Wilkinson $4.11M, Higgins $7.36M, Kirloskar $0.05M — under plans |
| **2026-08-06** | **10-K FY26 filed** (`0000319201-26-000027`) | Backlog $12.57bn (+60%). **RPO note removed.** Conversion schedule removed. Customer deposits −32%. Purchase commitments $5.97bn. Factoring $515.5M. Tariff materiality qualifier removed. DRAM GM impact extended to **fiscal 2027** |
| 2026-08-04 → 08-14 | **Largest insider selling cluster** | Wallace $17.42M (87,568 sh @ $198.95, 2026-08-11), Lorig $12.40M, Higgins $6.61M, Khan $6.60M, Wilkinson $8.17M across four sales, Kirloskar $1.76M across four sales. **Every one under a 10b5-1 plan** adopted 2025-11-20 or 2026-05-11/14 and disclosed at adoption |

**Trailing 6 months, 2026-03-05 → 2026-09-05, codes P and S only:**

| Insider | Role | Net |
| --- | --- | --- |
| Richard P. Wallace | President and CEO | −$35.50M |
| Bren D. Higgins | EVP and CFO | −$13.97M |
| Brian Lorig | EVP, KLA Global Services | −$12.40M |
| Mary Beth Wilkinson | EVP, CLO and Secretary | −$12.28M |
| Ahmad A. Khan | President, Semiconductor Products and Customers | −$6.60M |
| Virendra A. Kirloskar | SVP and CAO | −$2.37M |
| Jeneanne M. Hanley | Director | −$1.03M |
| **Net** | | **−$84.16M** |

**Zero open-market purchases (code P) by any insider in the entire 18-month window.** Of the
$84.16M sold, **$82.57M (98.1%) was executed under Rule 10b5-1 plans disclosed at adoption** in
Item 9B of the 10-K or Item 5 of the 10-Q, and **$1.59M was not**.

The 10b5-1 conclusion is confirmed three ways, independently:
1. **Form 4 footnote text** — e.g. Wallace's 2026-05-12 Form 4: *"This sale was effected pursuant
   to the terms of a Rule 10b5-1 trading plan adopted by the Reporting Person on November 19,
   2025."*
2. **`aff10b5One` XML checkbox** on each Form 4 — `true` on 35 filings, `false` on 63 (the false
   set being almost entirely tax-withholding and grant filings with no S transaction).
3. **Issuer disclosure at adoption** — Item 408(a) tables in 1Q26/2Q26/3Q26 10-Qs and Item 9B of
   the FY26 10-K name every officer, the adoption date, duration and maximum shares. 1Q26 states
   affirmatively that no plan was adopted or terminated that quarter.

**Timeline note, stated without causal claim.** The Higgins/Khan/Lorig plans were adopted
2026-05-11 to 2026-05-14, seven weeks before the 2026-06-30 fiscal year end and roughly three
months before the 10-K that removed the RPO disclosure. The plans were disclosed at adoption and
the sales executed mechanically under them. The sequencing is worth recording; it is not evidence
of anything on its own, and the disclosure practice here is materially better than the pattern that
was decisive on AMAT.

---

## Kill-criteria trip check (CLAUDE.md §4)

| Criterion | Finding | Status |
| --- | --- | --- |
| Net insider selling >$10M in trailing 6M **with no 10b5-1 plan disclosed at adoption** | $84.16M net sold, but $82.57M under plans disclosed at adoption; **$1.59M non-plan**, vs a $10M threshold | **NOT TRIPPED** |
| Auditor resignation | PwC retained; no Item 4.01 8-K since at least 2024-01-01 | **NOT TRIPPED** |
| Material weakness unremediated >2 quarters | Zero occurrences of "material weakness" outside the PwC boilerplate. ICFR effective at 2026-06-30, audited. Item 9A: no change in ICFR in 4Q26 | **NOT TRIPPED** |
| Restatement of revenue | "restatement" appears once per 10-K, in the unchecked cover-page Rule 10D-1(b) box. No Item 4.02 8-K | **NOT TRIPPED** |
| Serial "one-time" charges >15% of GAAP opex in 3 of last 4 quarters | FY26 restructuring $1.2M (vs $7.7M FY25); no goodwill or intangible impairment in FY26 | **NOT TRIPPED** |
| Related-party transactions material to earnings | Zero related-party disclosure in FY25 and FY26 10-Ks and all FY26 10-Qs | **NOT TRIPPED** |
| Share count >4%/yr with no revenue-per-share growth | $2.29bn repurchased; MD&A states repurchases "have reduced our basic and diluted weighted-average shares outstanding". Revenue +11.7%, diluted EPS $3.04 → $3.66 (+20.4%, split-adjusted) | **NOT TRIPPED** |
| Type A/B: customer concentration >25% with no multi-year contract | Largest customer 19% of revenue in FY26 and FY25 (13% FY24) | **NOT TRIPPED** |
| Thesis requires trusting a number we cannot tie to a filing | **Partially engaged.** The $12.57bn backlog is stated in Item 1 but its 12-month conversion is no longer disclosed anywhere. Any FY27 revenue bridge built on backlog conversion is now an unverifiable estimate | **FLAG — not a kill, but the FY27 model must label backlog conversion `[EST]`** |

**No kill criterion is tripped.**

---

## Open work items handed to the model and memo

1. **Backlog duration is now `UNVERIFIED`.** FY24 disclosed 59–64% converting in 12 months, FY25
   71–76%, FY26 nothing. Any FY27 revenue build off $12.57bn must be labelled `[EST]` with the
   method stated. Ask on the next call; if management will not give the range they gave for three
   straight years, that is itself the answer.
2. **Backlog quality.** Backlog +60% while customer deposits −32% ($636.4M → $430.1M). Deposits
   are the cash customers actually commit. Reconcile before treating backlog as revenue visibility.
3. **Receivables quality — four independent signals in one year.** AR +28% on revenue +12% (DSO
   68.0 → 77.7 days); factoring +124% to $515.5M (which *removes* receivables from the balance
   sheet, so gross deterioration is larger); new $180.7M long-term AR line where FY25 and FY24 were
   zero; credit-loss provision $11.5M → $28.4M and write-offs $10.3M → $31.4M. Operating cash flow
   was flat at $4.14bn while net income rose 19%, so **OCF/NI fell 1.00 → 0.86**. Gate 3 requires
   FCF/NI ≥0.8 on a 3-year average — this still passes, but the direction is one year of
   deterioration, not noise.
4. **Purchase commitments $5.97bn, majority due within 12 months**, against $3.65bn of inventory
   already on the balance sheet. Management's own new risk-factor language: *"we may purchase or
   commit to purchase inventory… that do not materialize"* and *"we may hold inadequate, excess or
   obsolete inventory."* Size the inventory write-down scenario for the bear case.
5. **ERP go-live in 1Q FY27** with a newly elevated risk factor referencing Section 404. Read the
   1Q FY27 10-Q Item 4 for any change in internal control.
6. **U.S. Customs holds on China-bound product** (new 3Q26). Not quantified. Ask for the dollar
   value held.
7. **Tariff refund receivable** recognised on claim submission, not approval, following the
   Feb-2026 IEEPA ruling. Unquantified and stated as immaterial. Watch for growth.
8. **AI as a threat, not only a driver.** The new risk factor naming customer insourcing and
   shortened product life is the first time KLA has written this down. It bears directly on gate 6
   (reinvestment runway) and on any terminal multiple.

---

*Reproducibility: 10-K FY26 `0000319201-26-000027`; 10-K FY25 `0000319201-25-000024`; 10-K FY24
`0000319201-24-000021`; 10-Qs `0000319201-26-000016`, `0000319201-26-000008`,
`0000319201-25-000034`, `0000319201-25-000012`, `0000319201-25-000006`, `0000319201-24-000027`;
8-K `0001193125-26-102999`; 102 Form 3/4/5 documents, 2025-03-01 → 2026-09-05. Working files under
the session scratchpad: `klac/*.htm`, `klac/*.txt`, `klac/sec/`, `klac/diff_item1.txt`,
`klac/diff_item1a.txt`, `klac/diff_item7.txt`, `klac/f4/`, `klac/f4_parsed.tsv`.*

*Research only. Not advice, not an order.*
