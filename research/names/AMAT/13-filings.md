# AMAT — Filing Diff & Insider Timeline

**Analyst:** filing-diff agent · **Date:** 2026-09-05 · **Method:** `.claude/skills/filing-diff`
**Business type:** B · Asset-heavy operating (per `00-base-facts.md`)

**Conclusion first.** Applied Materials removed or de-quantified five separate
disclosures across the FY25 10-K and the FY26 10-Qs. Every one of them sat on top
of a metric that was deteriorating in the same period. Nothing here is a
restatement, a material weakness, or an auditor change — the accounting is clean.
The problem is the **disclosure trend and the insider tape**: **$173.2M of net
insider selling on codes P/S in the trailing six months, with zero purchases and
no Rule 10b5-1 plan disclosed at adoption on any of the 90 Form 4s reviewed.**
That trips CLAUDE.md §4 Universal by 17x.

**Documents reviewed in full** (paged to completion; character counts of extracted
text shown, no truncation):

| Filing | Period | Accession | Filed | Text chars |
| --- | --- | --- | --- | --- |
| 10-Q | Q3 FY26 (2026-07-26) | 0001628280-26-058235 | 2026-08-20 | 184,309 |
| 10-Q | Q2 FY26 (2026-04-26) | 0001628280-26-037227 | 2026-05-21 | 184,213 |
| 10-Q | Q1 FY26 (2026-01-25) | 0001628280-26-009694 | 2026-02-19 | 179,889 |
| 10-K | FY25 (2025-10-26) | 0001628280-25-056742 | 2025-12-12 | 297,913 |
| 10-Q | Q3 FY25 (2025-07-27) | 0000006951-25-000037 | 2025-08-21 | 198,899 |
| 10-Q | Q2 FY25 (2025-04-27) | 0000006951-25-000024 | 2025-05-22 | 193,011 |
| 10-K | FY24 (2024-10-27) | 0000006951-24-000044 | 2024-12-13 | 300,470 |

Source: EDGAR primary documents, HTML normalised to text and compared with `diff`
plus a sentence-level orphan matcher. Working files under the session scratchpad.

---

## 1. The three changes that matter

### #1 — Backlog: the prior-year comparative column was deleted in the year Semiconductor Systems backlog fell 14%

**Before** [10-K FY24, Item 1 "Backlog", acc 0000006951-24-000044]:

> "Backlog by reportable segment as of October 27, 2024 and October 29, 2023 was as follows:"
>
> | | 2024 | | 2023 | |
> | --- | --- | --- | --- | --- |
> | Semiconductor Systems | $8,259 | 52% | $11,127 | 65% |
> | Applied Global Services | 6,767 | 43% | 5,162 | 30% |
> | Display | 827 | 5% | 833 | 5% |
> | Corporate and Other | 20 | —% | 49 | —% |
> | **Total** | **$15,873** | 100% | **$17,171** | 100% |

**After** [10-K FY25, Item 1 "Backlog", acc 0001628280-25-056742]:

> "Backlog by reportable segment as of October 26, 2025 was as follows:"
>
> | | 2025 | |
> | --- | --- | --- |
> | Semiconductor Systems | $7,105 | 47% |
> | Applied Global Services | 7,141 | 48% |
> | Corporate and Other | 756 | 5% |
> | **Total** | **15,002** | 100% |

**Type:** Removed (comparative period) + de-segmented (Display folded into
Corporate and Other).

**Read.** A reader holding only the FY25 10-K cannot compute the change in
backlog. Splicing the two filings: total backlog $17,171M → $15,873M → $15,002M,
and **Semiconductor Systems backlog $11,127M → $8,259M → $7,105M, −36.1% over two
years**. In FY25 AGS backlog ($7,141M) exceeded Semiconductor Systems backlog
($7,105M) for the first time. Semiconductor Systems *revenue* over the same two
years went $19,698M → $19,911M → $20,798M. The systems order book has been
shrinking for two consecutive years while shipments rose — a sub-1.0 book-to-bill
run — and the column that showed it was removed. This is the single highest-signal
edit in the set.

Also removed with it, without replacement:

> "As a result of new export rules and regulations issued in December 2024, backlog as of October 27, 2024 is expected to be reduced by approximately $549 million. This reduction would have resulted in total backlog as of October 27, 2024 of $15.3 billion, of which approximately 31% would not have been reasonably expected to be filled within 12 months." [10-K FY24]

The FY25 10-K gives no equivalent quantification of export-rule backlog impact.

---

### #2 — Named ≥10% customers were de-named in the year the top customer went from 12% to 19% of revenue

**Before** [10-K FY24, Item 1 and Note 14, acc 0000006951-24-000044] — disclosed
twice, once in Business and once in the segment note:

> "The following customers accounted for at least 10 percent of our Net revenue in each fiscal year, which were for products and services in multiple reportable segments:"
>
> | | 2024 | 2023 | 2022 |
> | --- | --- | --- | --- |
> | Samsung Electronics Co., Ltd. | 12% | 15% | 12% |
> | Taiwan Semiconductor Manufacturing Company Limited | 11% | 19% | 20% |
> | Intel Corporation | * | * | 10% |
>
> "*Less than 10%"

**After** [10-K FY25, Item 1 and Note 15, acc 0001628280-25-056742]:

> "During fiscal 2025, two customers accounted for approximately 19% and 15%, respectively, of our net revenue. During fiscal 2024, two customers accounted for approximately 12% and 11%, respectively, of our net revenue."

**Type:** Removed (customer identity) — the percentages survive, the names do not.

**Verification.** The strings "Samsung" and "Taiwan Semiconductor" appear 5 and 2
times respectively in the FY24 10-K raw HTML and **zero times in the FY25 10-K raw
HTML** and zero times in all three FY26 10-Qs. This was checked against the raw
source document, not the extracted text.

**Read.** Concentration jumped hard in the year the names were pulled: top
customer 12% → 19% (+700bps, a 58% relative increase); top two combined 23% → 34%.
The Q3 FY26 10-Q updates it to **"Two customers accounted for approximately 20%
and 14%, respectively, of our revenue for the nine months ended July 26, 2026"**
[Note 14, acc 0001628280-26-058235]. Top customer is now 20% and still rising.

**Kill-criterion proximity.** CLAUDE.md §4 Types A/B kills at ">25% from one
customer with no multi-year contract." At 20% this is **not tripped**, but it is
five points away, moving one direction, and — see #3 — essentially none of it is
under multi-year contract. Losing the identity also removes the ability to check
whether the concentration is a foundry or a memory customer, which is the whole
question in a WFE cycle.

---

### #3 — Long-duration contracted backlog fell 73% and shortened; disclosure retained but the number collapsed

Not a removal — a quantified deterioration that is easy to miss because it sits in
one sentence of Note 7 in each filing. Verbatim, same sentence, six periods:

| Filing | Quote |
| --- | --- |
| 10-K FY24 | "...with an original estimated duration of one year or more was approximately **$3.7 billion**, of which approximately **62%** is expected to be recognized within 12 months" |
| 10-Q Q3 FY25 | "...approximately **$2.0 billion**, of which approximately **50%**..." |
| 10-K FY25 | "...approximately **$1.7 billion**, of which approximately **53%**..." |
| 10-Q Q1 FY26 | "...approximately **$1.4 billion**, of which approximately **66%**..." |
| 10-Q Q2 FY26 | "...approximately **$1.2 billion**, of which approximately **77%**..." |
| 10-Q Q3 FY26 | "...approximately **$1.0 billion**, of which approximately **73%**..." |

Source: Note 7 "Contract Balances and Performance Obligations" in each filing.

**Read.** Remaining unsatisfied performance obligations on contracts with original
duration ≥1 year fell from $3.7B to $1.0B in 21 months (−73%) while quarterly
revenue rose 25% YoY. The portion recognisable beyond 12 months fell from ~$1.4B
to ~$0.27B. Against 9M FY26 revenue of $24,037M, **roughly 4% of the business sits
under contracts of original duration one year or more.** That is the direct answer
to Type B gate 1 and to the customer-concentration carve-out: the 20% customer is
not contracted multi-year in any way the filings evidence.

**Counterweight, stated fairly.** Contract liabilities (advance payments and
billings ahead of revenue) rose $2,566M → $3,271M (+27.5%) over the same nine
months [Note 7, Q3 FY26]. Short-cycle demand is real and being prepaid. The point
is not that demand is weak; it is that visibility has shifted from contracted to
short-cycle, which is a different risk shape and is not being narrated.

---

## 2. Two further removals

### #4 — Receivables-factoring disclosure was de-quantified, then deleted, while AR consumed $2.5B of cash

**Present through Q1 FY26. Absent from Q2 FY26 onward.**

10-K FY25 [Note 6, acc 0001628280-25-056742]:
> "We sold **$501 million, $444 million and $679 million** of accounts receivable during fiscal 2025, 2024 and 2023, respectively."

10-Q Q3 FY25 [Note 6, acc 0000006951-25-000037]:
> "We have agreements with various financial institutions to sell accounts receivable and discount promissory notes from selected customers. We sell our accounts receivable generally without recourse... We sold **$215 million and $324 million** of account receivables during the three and nine months ended July 27, 2025, respectively."

10-Q Q1 FY26 [Note 6, acc 0001628280-26-009694] — *de-quantified and narrowed*:
> "We have **an agreement with a financial institution** to sell accounts receivable from selected customers... Accounts receivable sold during the three months ended January 25, 2026 and January 26, 2025 **were not material**."

10-Q Q2 FY26 and Q3 FY26 [Note 6] — *the entire paragraph is gone*. Note 6 now
opens directly at "We maintain an allowance for credit losses..." The string "sell
accounts receivable" returns 0 hits in both filings.

**Type:** De-quantified (Q1 FY26), then Removed (Q2 FY26).

**Read.** In the same nine months, accounts receivable went from $5,185M at FY25
year-end to **$7,691M** at Q3 FY26 (+48%) against 9M revenue growth of 11%. The
cash-flow statement shows AR consuming **$2,508M** in 9M FY26 versus **$538M** in
9M FY25 — 4.7x [Q3 FY26 10-Q, Consolidated Condensed Statements of Cash Flows].
DSO moved from ~72 days to ~77 days. Whether the AR build is a customer-payment
problem or simply the cessation of ~$500M/yr of factoring is now unanswerable from
the filings. The disclosure that would settle it was deleted mid-build. This is
the clearest example in the set of a removal landing exactly where the number was
moving.

### #5 — Geographic MD&A commentary was deleted in the year China revenue fell 15.7%

**Before** [10-Q Q3 FY25, MD&A, acc 0000006951-25-000037] — five paragraphs:
> "Net revenue increased from customers in China in the three months ended July 27, 2025 compared to the same period in the prior year primarily due to higher investments in semiconductor equipment and display fabrication equipment."
>
> "Net revenue decreased from customers in China in the nine months ended July 27, 2025 compared to the same period in the prior year primarily due to lower investments in semiconductor equipment, partially offset by higher customer spending on spares and services and display fabrication equipment."
>
> (plus Korea, United States/Southeast Asia, and all-other-regions paragraphs)

**After** [10-K FY25, MD&A] — collapsed to a single sentence:
> "The changes in net revenue from customers in all regions for fiscal 2025 primarily reflected changes in investments in semiconductor equipment."

**After** [10-Q Q1, Q2, Q3 FY26, MD&A] — **nothing**. The regex
`revenue (increased|decreased) from customers in` returns 4 hits in the Q3 FY25
10-Q and **0 hits in all three FY26 10-Qs**.

**Read.** China revenue fell $10,117M → $8,529M in FY25, **−15.7%**, while total
revenue rose 4.4% [Note 15, FY25 10-K]. In Q3 FY26 China revenue was $2,506M,
**−2% YoY**, and China's share of revenue fell from 35% to 28% while total revenue
rose 25% [Note 14, Q3 FY26 10-Q]. The single largest geographic mix shift in the
company's recent history is now presented as a table with no narrative. The
geographic table itself survives — this is a removal of *explanation*, not of data,
which is a lower-grade finding than #1, #2 and #4, but it is on the same theme and
it happened in the same filings.

---

## 3. Full change table

| Section | Type | Before | After | Read |
| --- | --- | --- | --- | --- |
| 10-K Item 1 Backlog | **Removed** | FY24 table, two years: total $15,873M / $17,171M | FY25 table, one year: total $15,002M | YoY change no longer computable; Semi Systems backlog −14% hidden |
| 10-K Item 1 Backlog | **Removed** | "$549 million" export-rule backlog reduction quantified | No equivalent | Export-rule impact on orders no longer sized |
| 10-K Item 1 + segment note | **Removed** | "Samsung Electronics Co., Ltd. 12% / Taiwan Semiconductor Manufacturing Company Limited 11%" | "two customers accounted for approximately 19% and 15%" | Customer identity gone in the year concentration jumped 700bps |
| 10-Q Note 6 | **De-quantified → Removed** | "We sold $215 million and $324 million of account receivables" | Paragraph absent from Q2 FY26 | Factoring unknowable while AR consumed $2,508M of cash |
| 10-Q Note 6 | **Hedged** | "agreements with various financial institutions" | "an agreement with a financial institution" | Facility count reduced before the paragraph was deleted |
| MD&A geographic | **Removed** | 5 region paragraphs incl. two on China | Nothing (FY26 10-Qs) | China −15.7% FY25, −2% Q3 FY26 unnarrated |
| Segment reporting | **Removed** | Display a separate reportable segment: Q3 FY25 rev $263M, OI $62M | "management no longer considers Display a significant operating segment for separate reporting purposes"; prior years recast | Disaggregation lost; small ($705M 9M FY25 rev) but a real reduction |
| Segment reporting | **Reclassified** | AGS incl. 200mm equipment; corporate costs unallocated | 200mm moved AGS→Semi Systems and corporate costs fully allocated, effective Q1 FY26; prior periods recast | Q3 FY25 AGS revenue restated $1,600M → $1,463M (−$137M); 9M FY25 $4,760M → $4,236M (−$524M, −11.0%). **Any AGS comparison spanning FY25 10-K and FY26 10-Qs is apples-to-oranges.** |
| 10-Q Note 13 Legal | **Removed, with disclosed resolution** | "Since 2022, we have received multiple subpoenas from government authorities... including from the U.S. Department of Justice, the U.S. Commerce Department Bureau of Industry and Security, and the U.S. Securities and Exchange Commission." (last in FY25 10-K) | Q1 FY26 states DOJ and SEC "have closed their respective inquiries, and no enforcement action has been taken by either agency"; from Q2 FY26 all references absent | Legitimate resolution, properly disclosed. **But** the separately-described "subpoenas from the U.S. Department of Justice requesting information related to certain federal award applications" were never explicitly resolved before the reference vanished. Open item. |
| 10-K Note 14 contingencies | **Superseded by events** | FY25 10-K (2025-12-12): "we cannot predict the outcome, nor reasonably estimate a range of loss or penalties, if any, relating to these matters." | 61 days later a $253M BIS settlement was signed and charged in full to Q1 FY26 | A loss deemed not reasonably estimable in December was fully accrued in January. Not a kill; a calibration datapoint on management's contingency estimates. |
| Risk factors, all | **Boilerplate rewrite (flagged, not a finding)** | — | — | Q2 FY26 → Q3 FY26 risk factors were copy-edited nearly wholesale (~60% of paragraphs reworded with no change in substance). This makes machine diffing noisy. Substantive changes were isolated by heading-level and sentence-orphan matching. No risk factor was added or deleted at the heading level. |
| Risk factor: customer concentration | **Hedged + reordered** | Q1 FY26: "Our customer base is geographically concentrated, particularly in China, Taiwan and Korea, and export regulations that apply to customers in certain countries, such as those in China, **have exposed and can further expose us to greater volatility**." — sentence #3 of the paragraph | Q2/Q3 FY26: "In addition, our customers are geographically concentrated, particularly in China, Taiwan and Korea, and export regulations that apply to customers in certain countries, such as China, **have previously and may in the future adversely affect our business**." — demoted to sentence #5 | China/export exposure moved down the paragraph and softened from "expose us to greater volatility" to "adversely affect our business", in the quarter the $253M BIS penalty was paid |
| Risk factor: customer concentration | **Removed** | Q3 FY25: "To the extent our customers experience liquidity constraints, we may incur bad debt expense, which may have a significant impact on our results of operations." | Absent from FY25 10-K onward | Removed one year before AR grew 48% in nine months. Allowance for credit losses is still stated "not material." |
| Risk factor: global operations | **Quantified, updated** | Q2 FY26: "approximately 88% of our revenue was from customers in regions outside the United States" | Q3 FY26: "approximately 85% of our revenue was from customers outside the United States" | Routine period update, not a finding |
| Risk factor: export controls | **Added** | — | "On February 11, 2026, we entered into a settlement agreement with... BIS... and agreed to pay BIS $253 million... Our failure to comply with the terms of the settlement agreement could result in significant penalties, including the loss of the suspension of the denial order which would prohibit us from exporting certain of our products outside of the United States." | New, material, properly added. A suspended denial order is a live tail risk for three years. |
| Note 13 Legal | **Hedged** | Q1 FY26: denial order "will be waived three years after the date of the order... provided that we have **made full and timely payments under the settlement agreement and** timely completed the audit requirements." | Q2/Q3 FY26: "...provided that we have timely completed the audit requirements." | Payment condition dropped after the $253M was paid in full in Q2 FY26. Mechanically correct. |
| Risk factor: Singapore tax | **Added / reversed** | FY24: "Our conditional reduced tax rates in Singapore **will expire in fiscal 2025**... There is risk our conditional reduced tax rates may not be renewed." | FY25: "We have been **granted additional conditional reduced tax rates in Singapore that expire beginning in fiscal 2030.**" | Positive and material. Drives the ETR collapse below. |
| Critical accounting estimates | **Added** | — | "The acceleration of tax deductions for U.S. tax purposes, under the One Big Beautiful Bill Act, limits our ability to use our corporate minimum tax credits. As a result, we have recorded a full valuation allowance against this deferred tax asset." | New estimate, adequately explained |
| MD&A framing | **Hedged** | Q3 FY25: "customer spending... to support key technology transitions or **to increase** production volume in response to worldwide demand for semiconductors **and displays**." | Q3 FY26: "...or **changes in** production volume in response to worldwide demand for semiconductors." | Directional framing made symmetric. One word, and it is the word that matters. |
| Note 1 accounting policies | **Boilerplate** | — | — | ASU adoption housekeeping only. No change to revenue recognition. |
| Auditor / ICFR | **No change** | KPMG LLP, auditor since 2004 | KPMG LLP, auditor since 2004 | Critical audit matter identical both years ("Evaluation of sufficiency of audit evidence over revenue"). ICFR effective. Grep for "material weakness" returns 1 hit in each 10-K, in KPMG's standard scope paragraph. |

---

## 4. What did *not* change, where a reader would expect it to

- **Revenue recognition policy** is untouched. Semiconductor Systems at a point in
  time; AGS at a point in time for goods and over time for service agreements.
  No change in the year gross margin rose from 48.8% to 50.3%.
- **Critical audit matter** is verbatim identical FY24 and FY25 despite the
  removal of named-customer disclosure and the segment reclassification.
- **Related-party transactions:** none disclosed in any filing. Grep hits are
  false positives on "related parts and services." No kill.
- **Going concern / substantial doubt:** zero occurrences in any filing.
- **Restatement:** zero. All "restated" hits are plan and charter document titles
  in the exhibit index.
- **Allowance for credit losses** is still described as "not material" in Q3 FY26
  and "There were no credit losses recognized on our accounts receivable and
  contract assets" — unchanged language while AR rose 48% in nine months. The
  market would expect movement here and there is none. Either the receivables are
  genuinely clean or the disclosure is stale; the deleted factoring paragraph is
  what would have let us tell.
- **The 31% long-dated backlog share** is identical in both 10-Ks ("approximately
  31% is not reasonably expected to be filled within the next 12 months"), which
  is odd against a 73% collapse in ≥1-year RPO. The two metrics are defined
  differently and are not reconcilable from the filings. Flagged as unresolved.

---

## 5. Kill-criteria trip check (CLAUDE.md §4)

| Criterion | Result | Evidence |
| --- | --- | --- |
| Net insider selling >$10M in trailing 6M with no 10b5-1 plan disclosed at adoption | **TRIPPED** | **−$173,249,454** net, P/S codes only, 2026-03-05 to 2026-09-05. Zero purchases. See §6. |
| Auditor resignation / material weakness >2 quarters / revenue restatement | Not tripped | KPMG since 2004; ICFR effective as of 2025-10-26; zero material-weakness or restatement language |
| Serial "one-time" charges >15% of GAAP opex in 3 of last 4 quarters | Not tripped | 9M FY26 legal settlement $253M + restructuring $12M = $265M against GAAP opex of $4,274M (RD&E $3,055M + SG&A $1,219M) = **6.2%**, and concentrated in one quarter |
| Guidance missed 3+ times in 8 quarters | Not assessable from filings | Guidance lives in earnings releases and transcripts — out of scope for this agent, referred out |
| Related-party transactions material to earnings | Not tripped | None disclosed |
| Share count growing >4%/yr | Not tripped | Diluted shares 800M (Q3 FY26) vs 802M (Q3 FY25); shrinking |
| Thesis requires a number we cannot tie to a filing | **AT RISK** | Customer identity, factored receivables, and YoY backlog are all no longer derivable from a single filing. Reconstructible only by splicing prior filings — which this memo does, and which future filings will progressively prevent. |
| Type A/B: customer concentration >25% from one customer with no multi-year contract | Not tripped, **5pts away** | Top customer 20% of 9M FY26 revenue; ≥1-yr RPO of $1.0B is ~4% of 9M revenue, so the concentration is effectively uncontracted |

---

## 6. Insider activity — codes P and S only

**Trailing 6 months (2026-03-05 → 2026-09-05): 35 transactions, $0 bought,
$173,249,454 sold. Net −$173.2M.**

| Insider | Role | Sold ($) | Bought ($) | Txns |
| --- | --- | --- | --- | --- |
| Gary E. Dickerson | Director, President & CEO | 104,789,404 | 0 | 15 |
| Prabu G. Raja | President, Semiconductor Products Group | 31,599,497 | 0 | 5 |
| Omkaram Nalamasu | SVP, CTO | 20,754,197 | 0 | 9 |
| Thomas J. Iannotti | Director | 5,547,872 | 0 | 1 |
| Timothy M. Deane | SVP, Applied Global Services | 5,092,984 | 0 | 1 |
| Brice Hill | SVP, CFO | 4,841,530 | 0 | 2 |
| Judy Bruner | Director | 507,600 | 0 | 1 |
| Adam Sanders | Corporate Controller & CAO | 116,370 | 0 | 1 |
| **Total** | | **173,249,454** | **0** | **35** |

Source: all Form 4 XML filed by CIK 0000006951, parsed from
`nonDerivativeTransaction` elements. Trailing 12 months: −$179.8M.

### The 10b5-1 question — this is what makes the criterion bind

Three independent tests, all negative:

1. **`<aff10b5One>0</aff10b5One>` on all 90 Form 4s** filed since 2024-09-01. The
   Rule 10b5-1(c) affirmative-defence checkbox is unchecked on every one,
   including all $173.2M of 2026 selling.
2. **No footnote on any Form 4 references a 10b5-1 plan.** Footnotes are
   exclusively weighted-average-price undertakings and RSU/PSU vesting schedules.
3. **Reg S-K Item 408 disclosure is negative in seven consecutive filings** —
   FY24 10-K, Q2 FY25, Q3 FY25, FY25 10-K, Q1 FY26, Q2 FY26, Q3 FY26 all state
   verbatim: *"no director or officer, as defined in Rule 16a-1(f), adopted or
   terminated a 'Rule 10b5-1 trading arrangement' or a 'non-Rule 10b5-1 trading
   arrangement,' each as defined in Regulation S-K Item 408."*

**Residual caveat, stated honestly:** a plan adopted before Q4 FY24 would not
appear in test 3. But it would still require the Form 4 checkbox in test 1, which
is unchecked on all 90. The kill criterion as written — *"no 10b5-1 plan disclosed
at adoption"* — is satisfied on the evidence available.

### The round trip

Outside the 6-month window but load-bearing: **on 2025-04-03 the CEO made an
open-market purchase (code P) of 50,000 shares for $6,865,082 at $137.29–$137.70.**
Fourteen months later he sold 173,113 shares for $104.8M at $590.03–$736.05. That
is the only insider purchase in two years, and it was well timed. So was the exit.

---

## 7. Combined filings-and-insider timeline

| Date | Event | Detail |
| --- | --- | --- |
| 2024-12-13 | **10-K FY24** filed | Samsung 12% / TSMC 11% **named**. Backlog table shows two years ($15,873M / $17,171M). DOJ + BIS + SEC subpoenas disclosed. ≥1-yr RPO $3.7B. |
| 2025-04-03 | **Insider BUY (P)** | Dickerson (CEO) purchases 50,000 sh for **$6.87M** at ~$137.5 |
| 2025-08-21 | **10-Q Q3 FY25** filed | Three reportable segments incl. Display. AR factoring quantified ($215M/$324M). Region-by-region MD&A present (5 paragraphs incl. two on China). ≥1-yr RPO $2.0B. |
| 2025-11-19 / 11-25 | Insider sells (S) | Little (CLO) $1.89M @ $234–238 |
| 2025-12-01 | Insider sell (S) | Sanders (CAO) $0.16M @ $255 |
| **2025-12-12** | **10-K FY25 filed — 3 removals in one document** | Named-customer table **removed** (→ "two customers... 19% and 15%"). Backlog prior-year column **removed**. Display de-segmented, priors recast. Region MD&A collapsed to one sentence. Contingency: "cannot... reasonably estimate a range of loss or penalties, if any." ≥1-yr RPO $1.7B. |
| 2026-02-11 | **BIS settlement signed** | $253M, plus suspended denial order and 3 years of compliance audits — **61 days after** the "cannot reasonably estimate" statement |
| 2026-02-17 | Insider sell (S) | Hill (CFO) $1.81M @ $361 |
| **2026-02-19** | **10-Q Q1 FY26 filed** | $253M charged in full. DOJ and SEC inquiries disclosed **closed, no enforcement action** — credit to the company. AR factoring **de-quantified** ("not material") and narrowed to "an agreement with a financial institution". 200mm moved AGS→Semi Systems; corporate costs fully allocated; priors recast. ≥1-yr RPO $1.4B. |
| 2026-02-23 → 02-25 | Insider sells (S) | Bruner (Dir) $2.48M, Sanders $0.20M @ $376–392 |
| **2026-05-21** | **10-Q Q2 FY26 filed** | AR factoring paragraph **deleted entirely**. Customer-concentration risk factor reordered — China/export exposure demoted from sentence 3 to sentence 5 and softened. All DOJ/SEC references now absent. ≥1-yr RPO $1.2B. |
| 2026-05-22 → 2026-06-30 | **Insider selling wave — $169.7M** | Sanders $0.12M (5/22) · Bruner $0.51M (5/26) · Hill $1.25M (6/3) · **Raja $25.3M (6/4, 6/18)** · Deane $5.09M (6/15) · **Nalamasu $20.8M (6/15–6/16)** · Iannotti $5.55M (6/16) · **Dickerson $104.8M (6/15, 6/16, 6/29, 6/30)** — final tranches at **$700.21, $701.33, $735.22, $736.05**, against a 52-week high of $739.67 |
| Q3 FY26 (ended 7/26) | **Company buyback decelerates as price rises** | Apr 27–May 24: 0.6M sh @ $414.56 ($230M) · May 25–Jun 21: 0.2M sh @ $486.67 ($99M) · Jun 22–Jul 26: 0.1M sh @ $591.73 ($71M). 9M FY26 repurchases **$1,177M** vs 9M FY25 **$4,044M** (−71%). |
| **2026-08-20** | **10-Q Q3 FY26 filed** | ≥1-yr RPO **$1.0B** (−50% YoY). Top customer **20%**. China revenue **−2% YoY**, share 35% → 28%, **no MD&A explanation**. AR **$7,691M** (+33% YoY), consuming $2,508M of cash 9M. Risk factors copy-edited near-wholesale. ETR 12.7% vs 30.6%. |
| 2026-08-25 | Insider sell (S) | **Hill (CFO) $3.59M @ $479.25 — five days after the 10-Q** |
| 2026-08-27 / 08-31 | Form 3 + Form 4 | Akash J. Palkhiwala joins the board; 279 sh director award (code A). Not P/S. |
| 2026-09-05 | Today | Price $454.71, −39% from the $739.67 high [per `00-base-facts.md`] |

**Pattern read, without overclaiming causation.** The MRVL template — discretionary
selling immediately *preceding* a quietly weakened disclosure — does **not** hold
here in that order. The sequence at AMAT runs the other way and is, if anything,
tidier: the disclosures were thinned first (Dec 2025, Feb 2026, May 2026), the
selling followed (May–Jun 2026, $169.7M into the all-time high), and the metric
that the thinned disclosures had been covering was printed at its worst level in
the Aug 2026 10-Q. Five of eight sellers, including the CEO, the CFO, the
president of the largest segment, the CTO and the SVP running AGS, sold with no
10b5-1 plan on file. The company simultaneously slowed its own buyback as the
price rose. These are separate facts placed on one timeline; the filings do not
establish and this memo does not assert any causal link.

---

## 8. Follow-ups for the other agents

1. **Gate 1 is in trouble and the reclassification makes it worse.** AGS gross
   profit is **$634M of $4,586M total in Q3 FY26 = 13.8%**, and $1,748M of
   $11,968M = 14.6% for 9M FY26 [Note 14, Q3 FY26]. The Type B threshold is
   *aftermarket ≥30% of gross profit*. On the FY25 10-K's old basis it was
   $2,134M of $13,808M = 15.5%. **Gate 1 fails on the aftermarket test on either
   basis**, and the 200mm move shifted a further ~$137M/quarter of revenue out of
   AGS. The repeat-revenue limb of gate 1 has to carry the argument, and ≥1-yr RPO
   at ~4% of revenue does not help it. This answers open question #1 in
   `00-base-facts.md`: **AGS does not clear the aftermarket test.**
2. **Gross margin — answer the base-facts question with tax, not amortisation.**
   The margin rise is narrated as "higher revenue, increases in average selling
   prices, and lower material and manufacturing costs" [MD&A Q3 FY26] — no
   amortisation roll-off claimed, unlike MRVL. But **the earnings rise is largely
   tax**: effective tax rate **12.7% in Q3 FY26 vs 30.6% in Q3 FY25**; 12.9% vs
   27.2% for 9M, driven by "a remeasurement of deferred tax assets resulting from
   new tax incentive agreements in Singapore" plus the prior-year CAMT valuation
   allowance. At the prior-year rate, Q3 FY26 net income would be roughly $2.0B
   rather than $2,538M. Someone needs to normalise this before any multiple is set.
3. **Gate 3 earnings quality looks like a fail.** 9M FY26 operating cash flow
   $5,568M less capex $1,988M = FCF $3,580M against net income $7,370M →
   **FCF/NI ≈ 0.49**, versus the ≥0.8 threshold. Driven by the $2,508M AR build.
   Verify on a 3-year average basis before scoring.
4. **Do not compare AGS across the FY25 10-K and the FY26 10-Qs.** Two
   reclassifications hit simultaneously in Q1 FY26 (200mm transfer, full corporate
   cost allocation). Q3 FY25 AGS was restated from $1,600M/$445M to $1,463M/$400M;
   9M FY25 from $4,760M/$1,338M to $4,236M/$1,114M. The FY25 10-K is on the old
   basis.
5. **Open item:** the DOJ subpoenas concerning "certain federal award applications
   and information submitted to the federal government" — a matter distinct from
   export controls — were last disclosed in the FY25 10-K and were never
   explicitly stated to be resolved before all references disappeared in Q2 FY26.
   Worth a direct question to IR.

---

## 9. Confidence

**High on the removals, high on the insider figure, medium on interpretation.**

- The five removals were each verified against the raw source HTML, not only the
  extracted text. The named-customer removal was confirmed by grepping the raw
  `.htm` for "Samsung" and "Taiwan Semiconductor" (5 and 2 hits in FY24; 0 and 0
  in FY25 and all three FY26 10-Qs).
- All seven documents were paged to completion. No finding rests on a truncated
  read.
- The $173.2M insider figure is computed from parsed Form 4 XML, codes P and S
  only, tax-withholding (F), grants (A), option exercises (M) and gifts (G)
  excluded. Reproducible.
- **Medium on interpretation** because the disclosure removals have an innocent
  joint explanation: the FY25 10-K was a broad drafting overhaul (Display
  de-segmented, ASU 2023-07 segment disclosures adopted, risk factors condensed
  ~18%), and companies routinely stop naming customers once contracts or
  relationships change. The FY25 10-K also *added* real disclosure — expanded
  segment expense detail under ASU 2023-07, the Singapore tax reversal, the OBBBA
  valuation allowance. That is not the profile of a company hiding. What is not
  innocent is the coincidence: three of the five removals landed in the exact
  reporting period in which the underlying metric turned, and the insider tape
  ran $173M net short with no plan on file.

*This is research, not advice and not an order.*
