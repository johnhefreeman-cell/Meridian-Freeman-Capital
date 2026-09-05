# MRVL — Bull Case

**Author:** bull-case agent · **Date:** 2026-09-05 · **Price:** $223.55
(IRA_Portfolio.v2.0.xlsx, as of 2026-09-05 — holder's workbook, not vendor)

**Conclusion first.** The bull case on Marvell is worth ~15.7% three-year IRR,
not a multiple of today. It clears the §5 hurdle by a hair, it requires the exit
multiple to *contract* from 66x to 40x forward non-GAAP EPS, and it rests on one
number no filing supports: FY28 revenue growth near 40%. Anyone underwriting
multiples of today's price is underwriting sentiment. This memo is the strongest
honest version, and the honest version is a 15–20% IRR with wide error bars.

**Two doctrine findings up front, both adverse, both resolved from the 10-K:**

1. **Gate 1 under Type A: FAIL, definitively.** The base-facts file left this
   open. It is now closed. Marvell has **zero** contracted recurring revenue.
   "We typically sell products pursuant to purchase orders rather than long-term
   purchase commitments. Some of our customers have, and others may in the
   future, cancel or defer purchase orders on short notice without incurring a
   significant penalty." `[10-K FY26, 0001835632-26-000011, Item 1A]` Deferred
   revenue included in FY26 revenue was "not material," and the company elects
   the ASC 606 practical expedient because contracts have "an original expected
   duration of one year or less" — so there is no RPO, no backlog, and no
   disclosed renewal metric. `[10-K FY26, Note 3]`
2. **Gate 5: FAIL.** The annual incentive plan is 50% revenue, **15% non-GAAP
   gross margin, 35% non-GAAP operating margin**; the PSUs multiply relative TSR
   by a **non-GAAP EPS CAGR** modifier. `[DEF 14A 2026-05-13,
   0001104659-26-060253, CD&A]` CLAUDE.md §3.1: "Comp tied to 'adjusted'
   anything is a gate 5 failure regardless of type." All current directors and
   executive officers as a group (13 persons) own **1,046,798 shares = 0.12%**
   of the 847,287,680 shares outstanding — against a 3% threshold.
   `[DEF 14A 2026-05-13, Security Ownership table]`

MRVL therefore does not earn a full Type A compounder workup on the letter of
the doctrine. What follows is underwritten as a growth-duration position, not a
compounder, and is priced accordingly.

---

## 1. Mechanism

**One sentence:** Marvell now converts each incremental revenue dollar into
~50 cents of GAAP and ~41 cents of non-GAAP operating income, so a data-center
franchise growing 46% YoY compounds non-GAAP EPS at ~35–37% a year and produces
the entire return from earnings, with the multiple working against it.

That is one mechanism — incremental-margin capture on data-center scale. It is
not TAM narrative, not amortization optics, not a re-rating. The proof is in
company guidance, one quarter forward:

| | Q2 FY27 actual | Q3 FY27 guide (mid) | Δ |
| --- | --- | --- | --- |
| Net revenue | 2,739.3 | 3,150.0 | +410.7 |
| GAAP gross profit @ 53.4% mid | 1,455.6 | 1,682.1 | +226.5 |
| GAAP operating expenses | 995.9 | ~1,015.0 | +19.1 |
| **GAAP operating income** | **459.7** | **667.1** | **+207.4** |
| GAAP operating margin | 16.8% | 21.2% | +440bps |
| Non-GAAP operating income | 1,003.2 | 1,172.0 | +168.8 |
| Non-GAAP operating margin | 36.6% | 37.2% | +60bps |

Source: Q2 FY27 actuals `[10-Q 0001835632-26-000025]` and non-GAAP
reconciliation `[8-K 2026-08-27, 0001835632-26-000022, Ex-99.1]`; Q3 guidance
from the same exhibit; Q3 GAAP/non-GAAP operating income derived from guided
revenue × guided margin less guided opex.

**Incremental GAAP operating margin: 50.5%. Incremental non-GAAP operating
margin: 41.1%**, against a 36.6% running average. Opex grows 2.0% sequentially
against revenue +15.0%. That is the whole mechanism.

Decomposition of the +$207.4M GAAP step, so nobody mistakes it for accounting:
$168.8M (81%) is real non-GAAP operating income growth; $35.4M (17%) is
shrinking special items (SBC + amortization as fixed dollars diluted by
revenue). The leverage is mostly real.

**Edge type (§1): Analytical, narrow and decaying.** The claim is not that we
know the TAM. It is that the operating-leverage path has to be netted against
two disclosures filed eight days ago that most models have not yet absorbed:
the **59.0 million-share customer warrant** (Note 15, subsequent event) which is
contra-revenue, and the **$1,049.6M amortization runoff schedule**. Section 5
quantifies both. This edge has a shelf life measured in weeks and expires at the
October 6, 2026 Investor Day.

---

## 2. The math

### 2.1 Starting point (all from filings)

| Metric | Value | Source |
| --- | --- | --- |
| TTM revenue (Q3 FY26 + Q4 FY26 + Q1 FY27 + Q2 FY27) | 9,450.3 | base-facts, derived |
| TTM GAAP operating income (357.8 + 404.4 + 339.4 + 459.7) | 1,561.3 | XBRL `OperatingIncomeLoss`, 10-K/10-Qs |
| TTM amortization of acquired intangibles (229.0+223.6+225.2+214.9) | 892.7 | XBRL `AmortizationOfIntangibleAssets` |
| TTM non-GAAP operating income | 3,395.2 | derived from disclosed non-GAAP margins × quarterly revenue |
| TTM non-GAAP operating margin | 35.9% | derived |
| TTM operating cash flow (1,750.5 − 794.5 + 1,244.3) | 2,200.3 | `[10-K FY26]`, `[10-Q Q2 FY27]` |
| TTM capex (354.1 − 166.3 + 282.4) | 470.2 | XBRL `PaymentsToAcquirePropertyPlantAndEquipment` |
| **TTM FCF (OCF − capex)** | **1,730.1** | derived |
| TTM tech-license payments (financing-classified) | 130.6 | `[8-K Ex-99.1 cash-flow statements]` |
| TTM RSU tax-withholding cash (financing-classified) | 471.0 | same |
| **TTM owner FCF (FCF − licenses − RSU withholding)** | **1,128.5** | derived |
| Net debt at 2026-08-01 | 1,030.1 | base-facts |
| EV (derived, market data unavailable) | 206,985 | base-facts |

**What the stock costs today, stated plainly:** EV/TTM revenue **21.9x**;
EV/TTM non-GAAP operating income **61.0x**; EV/TTM FCF **119.6x**;
EV/TTM owner FCF **183x**, i.e. a **0.55% owner-FCF yield**. There is no
version of this that is cheap on current cash flow. The bull case is entirely a
statement about the next three years of revenue.

### 2.2 Revenue path

| Fiscal year | Revenue | Growth | Basis |
| --- | --- | --- | --- |
| FY26 actual | 8,194.6 | +42.1% | `[10-K 0001835632-26-000011]` |
| H1 FY27 actual | 5,157.1 | +32.2% | `[10-Q 0001835632-26-000025]` |
| Q3 FY27 guided | 3,150.0 | +51.9% | `[8-K 0001835632-26-000022 Ex-99.1]` |
| Q4 FY27 | 3,465.0 `[EST]` | +56.2% | `[EST]`: Q3 guide × 1.10 sequential (Q3 sequential is +15.0%; assumes half that rate carries) |
| **FY27E** | **11,772.1** | **+43.7%** | derived |
| **FY28E** | **16,481.0** | **+40.0%** | `[EST]` — see §3 |
| **FY29E** | **21,425.3** | **+30.0%** | `[EST]` |
| **FY30E** | **26,781.6** | **+25.0%** | `[EST]` |

FY27E→FY30E CAGR: **31.5%**. Sanity check on FY28E: it implies average quarterly
revenue of $4,120M against a Q4 FY27E exit rate of $3,465M — i.e. ~4.4%
sequential growth per quarter, versus the +15.0% sequential currently guided.
The FY28 number is a deceleration assumption, not an extrapolation.

### 2.3 Margin and EPS path — including the customer-warrant charge

On 2026-08-28 Marvell disclosed that **subsequent to quarter end it issued a
warrant to a customer for up to 59.0 million shares at $206.58, seven-year term
to August 2033, vesting from Q3 FY27 through FY2033 on revenue-milestone or
time-based conditions.** `[10-Q 0001835632-26-000025, Note 15]` Marvell's
accounting policy for customer warrants is explicit: they "vest primarily based
on the customer's achievement of qualifying product revenue milestones **and are
recognized as a reduction to revenue** as qualifying revenues are recognized."
`[10-K FY26, 0001835632-26-000011, Note 3]`

Sizing it `[EST]`: the FY2025 warrant carried a grant-date fair value of
$54.44 per share against an $87.77 strike — a 62.0% ratio `[10-K FY26, Note 3]`.
Applying that ratio to the $206.58 strike gives ~$128.13/share × 59.0M shares =
**~$7,560M of maximum contra-revenue**, ~$1,163M/yr straight-lined over the
6.5-year vesting window. The vesting *shape* is not disclosed; straight-line is
an assumption, and the FY27 half-year charge may already sit inside the Q3
guide. This charge is included in the numbers below. It is the single largest
adjustment in this memo and I have not seen it modelled anywhere.

| | FY27E | FY28E | FY29E | FY30E |
| --- | --- | --- | --- | --- |
| Gross revenue | 11,772 | 16,481 | 21,425 | 26,782 |
| Warrant contra-revenue `[EST]` | (582) | (1,163) | (1,163) | (1,163) |
| **Net revenue** | **11,191** | **15,318** | **20,262** | **25,619** |
| Non-GAAP op margin (pre-warrant) `[EST]` | 36.5% | 38.0% | 39.0% | 40.0% |
| Non-GAAP operating income | 3,715 | 5,100 | 7,193 | 9,550 |
| Non-GAAP op margin (post-warrant) | 33.2% | 33.3% | 35.5% | 37.3% |
| Non-GAAP interest & other `[EST]` | (150) | (150) | (150) | (150) |
| Non-GAAP tax @ 13% `[EST]` | (464) | (644) | (915) | (1,222) |
| **Non-GAAP net income** | **3,101** | **4,306** | **6,128** | **8,178** |
| Diluted shares (M) `[EST]` | 921.2 | 930.0 | 938.0 | 945.0 |
| **Non-GAAP diluted EPS** | **$3.37** | **$4.63** | **$6.53** | **$8.65** |
| Free cash flow (OCF − capex − licenses) `[EST]` | 2,060 | 3,131 | 4,392 | 5,892 |

Source row: FY27E built from H1 FY27 actuals `[10-Q 0001835632-26-000025]` plus
Q3 FY27 guidance `[8-K 0001835632-26-000022 Ex-99.1]`; all FY28–FY30 figures are
`[EST]` per §3. Non-GAAP tax of 13% versus the 11.0% rate the company used for
Q2 FY27 `[8-K 0001835632-26-000022 Ex-99.1, footnote (c)]`.

Non-GAAP EPS CAGR FY27E→FY30E: **37.0%**. Today's price is **66.4x FY27E**
non-GAAP EPS.

### 2.4 Exit and IRR

**Terminal multiple discipline (§5).** The trailing five-year median EV/revenue
and P/E are **UNVERIFIED** — the market MCP server is down and no price history
is available this session. I therefore refuse to set a terminal multiple by
reference to history and instead set it *below the multiple the stock trades at
today*, which I can compute. Every exit below 66.4x is multiple compression.

| Exit multiple on FY30E non-GAAP EPS $8.65 | Exit price | 3-yr total return | **3-yr IRR** |
| --- | --- | --- | --- |
| 30x | $260 | +16.2% | **5.1%** |
| 35x | $303 | +35.5% | **10.7%** |
| **40x (bull)** | **$346** | **+54.8%** | **15.7%** |
| 45x | $389 | +74.1% | **20.3%** |
| 40x, warrant charge excluded | $389 | +74.0% | 20.3% |

Source row: price $223.55 (IRA_Portfolio.v2.0.xlsx 2026-09-05); EPS from §2.3;
dividend of $0.24/yr `[10-Q 0001835632-26-000025, statement of stockholders'
equity]` adds ~0.11%/yr and is ignored.

**Bull case: 40x exit, $346, 15.7% three-year IRR.** Excluding the warrant
charge the same exit multiple gives 20.3%. The honest bull range is
**15.7%–20.3%**.

**Multiple-expansion test (§5).** Return decomposition at the 40x exit:
EPS growth contributes **+157%**, the multiple contributes **−40%**
(66.4x → 40x), net +54.8%. **Multiple expansion is negative — it is a headwind,
not 40% of the return.** The §5 constraint is satisfied decisively. This is the
strongest structural feature of the case: it does not need the market to like
Marvell more than it does today; it needs the market to like it 40% less and
still work.

**Cross-check on cash.** At the 40x exit, market cap is $327,000M; against FY30E
FCF of $5,892M that is **55x EV/FCF**, versus 119.6x today. Compression again,
but 55x FCF is an expensive absolute exit and I say so. An investor who insists
on a 30x-FCF exit gets $177,000M of EV — below today's $206,985M — and loses
money in the bull case. **The exit multiple is the weakest joint in this case.**

---

## 3. Evidence per assumption

| # | Assumption | Evidence | Verdict |
| --- | --- | --- | --- |
| 1 | Q3 FY27 revenue $3,150M, +51.9% YoY | Company guidance `[8-K 0001835632-26-000022 Ex-99.1]` | **Supported**, guidance tier (below filing tier) |
| 2 | Incremental non-GAAP op margin ~41% | Q2 actual 1,003.2 on 2,739.3 vs Q3 guide 1,172.0 on 3,150.0 `[same]` | **Supported**, arithmetic on guidance |
| 3 | Data center is the growth engine, 79% of revenue | Q2 FY27 DC $2,171.5 (79%) vs $1,490.5 (74%), **+45.7% YoY**; FY24 2,216.7 → FY25 4,164.2 → FY26 6,100.3 `[10-Q Note 3; 10-K Note 3]` | **Supported**, filing tier |
| 4 | FY28E revenue +40% | Management "raising our revenue outlook for both fiscal 2027 and fiscal 2028"; "significant acceleration in our Custom business beginning in the second half of fiscal 2027"; FY26 design wins "hit an all-time record" `[8-K 0001835632-26-000022 Ex-99.1; 8-K 0001835632-26-000006 Ex-99.1]` | **UNSUPPORTED as a number.** No FY28 figure is disclosed. This is a qualitative statement converted into a quantitative assumption. It is the load-bearing assumption and it is the weakest-evidenced one. |
| 5 | Multi-year forward volume visibility | Unconditional foundry / test-and-assembly purchase commitments as of 2026-08-01: rem-FY27 $1,829.3M, FY28 $2,125.4M, **FY29 $2,178.3M, FY30 $2,201.8M**, total $8,518.9M `[10-Q 0001835632-26-000025, Note 9]` | **Partially supported.** Marvell has unconditionally committed ~$2.2B/yr of capacity out to FY30. But at ~47% COGS/revenue that only underwrites ~$4.7B of annual revenue — a floor at roughly 40% of FY26, not a forecast. It is evidence of intent, not of demand. |
| 6 | A very large customer program exists | 59.0M-share warrant at $206.58, vesting on revenue milestones through FY2033 `[10-Q 0001835632-26-000025, Note 15]`; predecessor FY2025 warrant (4.2M shares, $87.77) had 0.7M shares already vested at 2026-01-31, i.e. the milestone structure is working `[10-K FY26, Note 3]` | **Supported, and it is the best gate-1 substitute in the filings.** A company does not hand a customer 6.4% of itself for a small program. It is also a ~$7.6B cost — see §5. |
| 7 | Gross margin holds ≥57.5% non-GAAP | Q3 FY27 guide 57.5%–58.5% `[8-K Ex-99.1]`. But the trend is **down**: 59.4% (Q2 FY26) → 59.0% (H1 FY27) → 58.9% (Q2 FY27) → 57.5–58.5% guided | **Contradicted in direction.** Model holds margin at the guided floor and takes zero gross-margin help. |
| 8 | Balance sheet supports the plan | Net debt $1,030.1M; TTM EBITDA (GAAP op income 1,561.3 + amortization 892.7 + PP&E D&A ~380 `[EST]`) = $2,834.0M → **net debt/EBITDA 0.36x**. Undrawn $1.5B revolver, in covenant compliance `[10-Q Note 7]` | **PASS, comfortably** (gate 4 threshold 3.0x) |
| 9 | No maturity wall | Next maturities: $750.0M 2.450% notes due **April 15, 2028** and $499.9M 4.875% MTI notes due **June 22, 2028** = $1,249.9M `[10-K FY26 debt note; 10-Q Note 7]`. That is ~19–22 months out, i.e. **inside** the 24-month window, but covered 3.1x by $3,932.8M cash | **PASS with a named exception.** It is a maturity, not a wall. |
| 10 | Earnings quality | H1 FY27 FCF $961.9M (OCF 1,244.3 − capex 282.4) vs GAAP NI $342.5M = **2.81x**. FY26 ratio of 0.52 is meaningless: net income contains a **$1,830.4M non-cash gain on sale of the automotive ethernet business to Infineon for $2.5B, closed 2025-08-14** `[10-K FY26, Item 1 Recent Developments; 8-K 0001835632-26-000006 Ex-99.1 cash-flow statement]`. Base-facts open item #2 is closed. | **PASS**, gate 3 threshold 0.8 |
| 11 | Q1 FY27's $34.5M net income was not operational | Q1 FY27 GAAP operating income was **$339.4M**, up 25.4% YoY. Net income was destroyed below the line by a **$250.7M non-cash charge for change in fair value of contingent consideration liability, net of forward stock purchase contract** — the Celestial earnout marked up because the stock rose `[8-K 0001835632-26-000022 Ex-99.1 reconciliation]`. Base-facts open item #3 is closed. | **Supported.** Not an operating problem. |
| 12 | The FY27 capital raise is understood | Q1 FY27: $2,000.0M Series A Convertible Preferred issued 2026-03-31, $998.9M of 5.300% 2036 notes issued 2026-04-15, $500.0M 2026 notes repaid. Uses: Celestial cash consideration $1,276.0M and XConn $469.0M `[10-Q Note 4, Note 7, statement of cash flows]`. Base-facts open item on the +$992M debt is closed. | **Supported** |
| 13 | Share count is controlled | Diluted 870.4M (Q2 FY26) → 921.2M (Q2 FY27), +5.84%, of which **26.8M shares were acquisition consideration** and ~20.6M is the preferred on an as-converted basis. Organic H1: 5.2M issued under plans less 2.5M repurchased = **+2.7M net, +0.31% on 876.8M common** `[10-Q statement of stockholders' equity]` | **Supported for organic dilution.** Not supported for total: the Celestial earnout can issue **24.4M more shares through FY2029** `[10-K FY26, Item 1A]` and the customer warrant up to 59.0M more. |
| 14 | Amortization runoff closes the GAAP/cash gap | Disclosed schedule as of 2026-08-01: rem-FY27 $385.3M, FY28 $292.7M, FY29 $139.6M, FY30 $117.2M, FY31 $60.8M, thereafter $54.0M, total $1,049.6M `[10-Q 0001835632-26-000025, Note 5]`. FY27 total = H1 actual 440.1 + 385.3 = **$825.4M → $292.7M in FY28**, a **$532.7M** non-cash GAAP relief. The schedule is reliable: the FY25 10-K predicted $941.7M for FY26 and actual was $942.0M. | **Supported, and immaterial to value.** It raises GAAP EPS and does nothing to cash. Offset: **$1,297.0M of indefinite-lived IPR&D** begins amortizing over 6–13 years when placed in service `[10-Q Note 5]` — roughly $100–215M/yr `[EST]` back. I do not count amortization runoff in the IRR. |

---

## 4. Preconditions — what must be observably true within 12 months

Each is a number in a filing. If any two fail, the case is off track.

| # | Precondition | Falsifying observation | Filing / date |
| --- | --- | --- | --- |
| P1 | Q3 FY27 net revenue ≥ $3,000M **and** GAAP operating margin ≥ 20.0% | Either misses | 10-Q Q3 FY27, ~Dec 2026 |
| P2 | Q4 FY27 sequential revenue growth ≥ +8% | Q4 revenue < $3,400M | 8-K Q4 FY27, ~Mar 2027 |
| P3 | FY27 total net revenue ≥ $11,400M | Below | 10-K FY27, ~Mar 2027 |
| P4 | Data center ≥ 80% of revenue and growing ≥ 40% YoY in Q4 FY27 | Below either | 10-K FY27 Note 3 |
| P5 | Non-GAAP gross margin ≥ 57.5% in **each** of Q3 and Q4 FY27 | Any quarter below | 8-K Ex-99.1 reconciliations |
| P6 | SBC ≤ 11.0% of net revenue for FY27 (H1 was 10.4%, Q2 was 11.9%) | Above 12.0% | 10-K FY27 cash-flow statement |
| P7 | Cumulative FY27 contra-revenue from the FY2027 customer warrant ≤ $700M, and the vesting schedule quantified | Above, or still undisclosed | 10-K FY27 revenue note |
| P8 | FY29 foundry purchase commitment ≥ $2,178.3M (no cut vs the 2026-08-01 disclosure) | Reduced | 10-K FY27 commitments note |
| P9 | Diluted WA shares ≤ 950M at Q2 FY28 | Above | 10-Q Q2 FY28, ~Aug 2027 |
| P10 | Non-10b5-1 insider open-market selling < $10M cumulative over any trailing 6 months | Above | Forms 4 |
| P11 | Investor Day (2026-10-06) produces a **numeric** FY28+ revenue or model target | No number given, or a number below $15B for FY28 | 8-K, Oct 2026 |

P11 is the fastest resolution of the load-bearing assumption and it lands in
31 days.

---

## 5. Steelmanned bear points and responses

### Bear point 1 — "The margin expansion is an accounting artifact; the real unit economics are getting worse."

**The bear's evidence, which is correct.** GAAP gross margin rose 270bps YoY in
Q2 FY27 (50.4% → 53.1%). Every basis point of that and more came from
amortization inside COGS falling from **8.3% to 5.2% of revenue**. Non-GAAP gross
margin **fell**, 59.4% → 58.9%, and is guided to 57.5%–58.5% for Q3.
`[8-K 0001835632-26-000022 Ex-99.1]` Custom silicon is structurally
lower-margin than the connectivity business it is displacing, and mix is
getting worse, not better. Meanwhile SBC has gone from $153.6M (Q2 FY26) to
**$326.2M (Q2 FY27), +112% YoY against revenue +37%**, and now runs at **11.9%
of revenue** versus 7.2% for FY26. The bear says: strip the accounting and
Marvell's margins are deteriorating while it pays employees an ever-larger share
of the business.

**Response — I concede the gross-margin half and answer the operating half.**
The gross-margin criticism is right and I have taken it out of the model: §2.3
holds gross margin at the guided floor and assumes **zero** gross-margin help
for three years. All 350bps of assumed operating-margin improvement comes from
opex leverage, which is the part the guidance actually evidences: non-GAAP
operating margin 34.8% (Q2 FY26) → 36.6% (Q2 FY27) → 37.2% (Q3 guide), with
non-GAAP opex guided at $655M on $3,150M of revenue (20.8%) versus $610.8M on
$2,739.3M (22.3%). Getting to a 40.0% non-GAAP operating margin at FY30E
revenue requires opex to grow +92% while revenue grows +144% — versus R&D
currently growing +35.7% YoY `[10-Q 0001835632-26-000025]`. That is a real
assumption but it is inside the observed trend.

On SBC I have a partial answer only. The **expense** doubled; the **dilution**
did not. In H1 FY27 Marvell recognised $533.8M of SBC but issued only 5.2M net
shares under equity plans, repurchased 2.5M, and paid **$365.2M of cash** to
withhold shares on net settlement — organic dilution of **+0.31% on 876.8M
common shares**, roughly 0.6%/yr `[10-Q, statement of stockholders' equity and
cash-flow statement]`. The correct economic charge is that $365.2M of cash plus
~0.6%/yr of shares, not the $533.8M non-GAAP add-back. That is why §2.1 carries
an **owner-FCF** line that deducts the withholding: $1,128.5M TTM, a 0.55%
yield. I have not hidden it.

What I **cannot** answer: why SBC dollars doubled in two quarters. Celestial's
assumed awards were only $190.1M of post-acquisition fair value spread over 3–4
years, ~$50M/yr `[10-Q Note 10]` — nowhere near the $172.6M/quarter increase.
The rest is new grants at a high stock price, and the filings do not break it
out. **P6 is the monitoring line; if SBC/revenue passes 12% for FY27 the bear
wins this point outright.**

### Bear point 2 — "There is no contracted revenue, one distributor is 37% of sales, and China is 42% of shipments. This is a concentrated, cancellable, geopolitically exposed order book dressed up as a franchise."

**The bear's evidence, which is correct.** Gate 1 fails on the letter (§0).
Distributor A was **37% of FY26 net revenue** (34% FY25, 24% FY24) and Direct
Customer A 14% `[10-K FY26, Note 3]`. China rose to **42% of Q2 FY27 shipments**
from 29% `[10-Q Note 3]`. Direct customers fell from 59% to 50% of revenue YoY
while distributors rose from 41% to 50% — visibility into the end customer is
getting worse, not better. Sales are on purchase orders cancellable on short
notice without significant penalty.

**Response — partial, and I flag the unanswered half as the most dangerous open
item in the name.**

Answered: the §4 Type A/B kill ("customer concentration >25% from one customer
with no multi-year contract") is **not tripped as filed**. Distributor A is a
distributor, and the company states that "these distributors' sales to diverse
end customers and geographies further serve to mitigate the Company's exposure"
`[10-K FY26, Note 3]`. The largest *direct* customer is 14%. On China, the 10-K
states that "a substantial majority of the product shipments the Company makes
to China are for non-China based customers that have factories or contract
manufacturing operations located within China and whose products are
subsequently shipped out of China" `[10-K FY26, Note 3]`, so 42% overstates
China end-demand exposure.

**Unanswered, and I cannot answer it from the filings:** the same note says the
concentration "presentation is at the customer consolidated level," and nothing
rules out that Distributor A fronts principally for one hyperscaler. If it does,
the kill criterion is tripped and this memo is void. The 59.0M-share warrant is
circumstantial evidence that one customer relationship is very large. **This is
a hard, unresolved kill-criterion question and it must be settled before any
sizing decision.** I am recording it as unanswered rather than arguing around
it.

Partial offset on durability: the design-win structure is Marvell's substitute
for contracts, and the 10-K describes it as genuinely sticky — "if a customer's
system designer initially chooses a competitor's product, it becomes
significantly more difficult for us to sell our products for use in that system
because changing suppliers can involve significant cost, time, effort and risk"
`[10-K FY26, Item 1A]`. That is qualitative. There is no cohort table, no
attach-rate, no renewal disclosure. **The durability assumption is
unsupported by any number in the filings. That is a finding.**

### Bear point 3 (I raise it against myself) — "The 59.0M warrant is a $7.6 billion transfer from shareholders to a customer."

At $128.13/share `[EST]`, the new warrant is worth ~$7,560M — **3.7% of today's
EV** — and it lands as contra-revenue, which means it reduces reported revenue,
gross profit and operating income dollar-for-dollar. It also adds 6.4% to the
share count at a strike **below** today's price. The bear can reasonably say
Marvell is buying its revenue.

**Response.** I have put the full charge in the headline numbers: it takes the
bull IRR from 20.3% to **15.7%**. That is the honest bull. The offsetting
argument is that the warrant is the *price* of a program whose revenue Marvell
and the customer both sized as far larger — 59.0M shares is not a discount you
grant for incremental business — and the milestone structure means the cost only
crystallises if the revenue does. The predecessor FY2025 warrant is vesting
(0.7M of 4.2M shares by 2026-01-31), which says the structure has worked once
before at 1/14th the scale. **But the milestone schedule is not disclosed, the
grant-date fair value is not yet disclosed, and my $7,560M is an estimate built
from a prior warrant's ratio.** P7 resolves it.

### Bear point 4 — "Return on the capital actually deployed is 6.4%."

Invested capital at 2026-08-01 = equity $18,531.6M + debt $4,962.9M − cash
$3,932.8M = **$19,561.7M**. TTM GAAP operating income $1,561.3M, NOPAT at a 20%
tax rate = $1,249.0M → **ROIC 6.4%**, below any plausible WACC. Goodwill is
**$13,873.9M** `[10-Q Note 5]`, and Celestial alone added $2,394.2M of goodwill
plus $951.0M of IPR&D on $3,533.7M of consideration — 95% of the price bought no
current earnings `[10-Q Note 4]`. Under Type B, gate 2 (ROIC ≥15%) **FAILS**.

**Response.** Excluding goodwill and acquired intangibles, invested capital is
$3,341.2M and ROIC is **37.4%** — the operating business earns very well; the
acquisition history is what does not. Both numbers are true and I report both.
The bull position is that the incremental capital being deployed today is R&D
(27.0% of H1 FY27 revenue, growing 35.7% YoY) rather than goodwill, and R&D
compounds at the 37.4% incremental rate, not the 6.4% blended one. That is an
argument, not a proof: gate 6 is scored **UNKNOWN** in §6 for exactly this
reason.

---

## 6. Gate scorecard (Type A, per base-facts working assumption)

| # | Gate | Score | Basis |
| --- | --- | --- | --- |
| 1 | Revenue durability ≥70% recurring/contracted | **FAIL** | Purchase-order basis, cancellable on short notice; deferred revenue immaterial; ≤1-yr contracts, practical expedient elected, no RPO `[10-K FY26 Item 1A, Note 3]` |
| 2 | GM ≥50%, stable-to-rising | **PASS on GAAP, qualified** | GAAP GM 41.3% (FY25) → 51.0% (FY26) → 52.7% (H1 FY27). Non-GAAP GM is falling: 59.6% → 59.0% → 57.5–58.5% guided |
| 3 | FCF/NI ≥0.8 | **PASS** | H1 FY27 2.81x; FY26 distorted by the $1,830.4M divestiture gain |
| 4 | Net debt/EBITDA ≤3.0x | **PASS** | 0.36x. $1,249.9M matures Apr/Jun 2028 — inside 24 months, covered 3.1x by cash |
| 5 | Insider ≥3% or named operator; comp tied to per-share value | **FAIL** | Officers+directors 0.12%; AIP 50%-weighted to non-GAAP metrics; PSUs use non-GAAP EPS CAGR |
| 6 | ≥50% of FCF redeployable at ≥ current ROIC for 3+ yrs | **UNKNOWN** | Capacity to redeploy is evident (R&D 27.0% of revenue, $4.0B of FY27 M&A); returns on it are unproven — blended ROIC 6.4% |

Two FAILs and one UNKNOWN. **Under CLAUDE.md §3.1 this name does not earn a full
compounder workup.** If the fund wants to own it, it owns it as a growth-duration
position with an explicit doctrine exception, or it passes. The bull case does
not get to wave this away.

**Kill criteria — checked, none tripped:**
- Insider selling: **$47.3M** of open-market sales in the trailing six months
  (2026-03-05 to 2026-09-05) across 22 Forms 4, **$0 of buying**. Of that,
  ~$4.6M was in filings without a 10b5-1 plan flag (Durn $0.63M; Casper $1.35M
  + $0.76M + $1.90M) — **below the $10M no-plan threshold**. Method: parsed
  every Form 4 XML from EDGAR, summed code-S non-derivative dispositions ×
  price, plan status from the `aff10b5One` flag; the plan classification is
  `[EST]`. **Not tripped, but $47.3M of net selling with zero buying is a
  signal, not a nothing.**
- Dilution: share count +5.84% YoY vs revenue/share +29.0% — **not tripped**
  (confirmed in base-facts).
- Auditor/restatement/material weakness: none found; Deloitte retained
  `[DEF 14A 2026-05-13]`.
- Related-party transactions material to earnings: none found.
- Customer concentration >25% from one customer: **not tripped as filed** —
  but see Bear Point 2. **Open.**
- Guidance misses: Q4 FY26 beat guidance midpoint by $19.0M; Q2 FY27 beat by
  $39.0M `[8-K 0001835632-26-000006; 8-K 0001835632-26-000022]`. Not tripped.

---

## 7. Sizing input

**Liquidity gate (§2.1): UNVERIFIED.** The market MCP server is down, so
20-day median daily dollar volume cannot be computed and the implied max
position cannot be stated. For a ~$205,955M derived market cap the gate is
almost certainly non-binding against the holder's $25,365 position, but
CLAUDE.md requires the number, not the inference. **Record ADDV before the memo
is finalised.**

Sizing note tied to the bear: the holder currently carries 25.3% of the
Brokerage Link account and 23.1% of that account's risk in a name that fails two
of six gates, has an unresolved customer-concentration kill question, and
carries 71% 13-week realised volatility (base-facts). Nothing in this bull case
supports that weight. A bull IRR of 15.7% at the doctrine's minimum hurdle
argues for a *position*, not a *concentration*.

---

## 8. What would change my mind

Toward the bull:
- Investor Day (2026-10-06) discloses a numeric FY28 revenue target ≥ $16B, or a
  long-term model with a stated operating-margin target ≥ 40%.
- The FY27 10-K quantifies the 59.0M warrant's grant-date fair value below
  $5,000M, or discloses milestone thresholds that make the charge back-loaded
  past FY30.
- Distributor A is disclosed, or reasonably inferred from a customer's own
  filings, to be a genuine multi-customer distributor rather than a single
  hyperscaler's procurement channel.
- SBC/revenue falls below 10% for FY27 with revenue still compounding >35%.

Toward the bear — any one of these ends the bull case:
- FY27 revenue below $11,000M, i.e. Q4 does not accelerate.
- Non-GAAP gross margin below 57.0% in any quarter — the mix headwind is
  outrunning the volume.
- The FY27 10-K cuts the FY29 or FY30 foundry purchase commitment below the
  $2,178.3M / $2,201.8M disclosed at 2026-08-01.
- Distributor A is revealed as, or consolidates to, a single end customer
  >25% of revenue → §4 kill, immediate.
- SBC/revenue exceeds 12% for FY27.
- Warrant contra-revenue disclosed above $1,500M in any single year.
- Any Celestial IPR&D write-off — $951.0M of the $3,533.7M purchase price is
  indefinite-lived IPR&D that gets written off entirely if the project is
  abandoned `[10-Q Note 5]`.

---

*This document is research, not advice and not an order. Figures are cited to
EDGAR filings and XBRL company facts retrieved 2026-09-05. Price and market cap
are derived from the holder's workbook because the market data server was
unavailable; the trailing five-year multiple history is **UNVERIFIED** for the
same reason.*
