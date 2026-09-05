# MRVL — Bear Case

**Author:** bear-case agent · **Date:** 2026-09-05 · **Price used:** $223.55
(IRA_Portfolio.v2.0.xlsx as of 2026-09-05, per `00-base-facts.md`; market MCP
server down, so price is holder-workbook sourced and market cap is **derived**)

**Business type (working):** **A · Recurring**, per the `00-base-facts.md`
instruction to test against the stricter type. This memo shows Gate 1 fails
decisively on the Type A test, which matters for how the name is underwritten.

---

## Conclusion first

The bear case loses **64%** in the central path and **35%–84%** across the
range. **CLAUDE.md §5 requires a bear case that loses <25%. MRVL fails that
test by a factor of 2.6x.** That is the finding that drives sizing, and it is
not a close call.

Three facts do the work:

1. **FY2026 reported earnings are fiction.** $1,830.4M of the $3,046.6M FY26
   pre-tax income was a one-time gain on the sale of the automotive ethernet
   business to Infineon. The clean FY26 net income is **$1,106.5M [EST]**, not
   $2,670.1M — a **13.5% clean net margin, not 32.6%**. Clean trailing GAAP EPS
   is **$1.27**, not the reported $3.07. `[10-K FY26, acc 0001835632-26-000011]`
2. **The multiple, not the business, is the position.** On 2026-02-05 this same
   company, with the same order book and management already guiding to
   accelerating growth every quarter of FY27, closed at **$74.21** —
   **7.9x EV/trailing revenue**. Today it is **21.9x**. The stock tripled in
   seven months on two announcements (NVIDIA's $2.0B preferred, the Google
   commercial agreement) neither of which has yet produced revenue.
   `[424B7 2026-02-06, acc 0001193125-26-040188]`
3. **Marvell is now paying for its growth in equity, and disclosing it.** On
   2026-08-18 it issued Google a warrant for **58,970,907 shares** at $206.58 —
   **6.4% of diluted shares** — vesting one tranche per $500M of Google custom
   revenue. Warrant fair value is recognised **as a reduction of revenue**, not
   as an expense. `[8-K 2026-08-19, acc 0001193125-26-356217; 10-Q Q2 FY27
   Note 15, acc 0001835632-26-000025]`

**Two kill criteria are tripped** (customer concentration; non-GAAP add-backs on
the literal reading) and **Gates 1, 3 and 5 fail**.

---

## 1 · Compression bear vs. impairment bear

These are different risks with different sizes. Both are live here; that is
unusual and it is why the loss is large.

### 1a · Compression bear — the business is fine, the price was wrong

| Date | Price | Source | Shares o/s | Net debt | EV | EV / trailing rev |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-02-05 | $74.21 | 424B7 cover | 847.3M | 1,831.8 | 64,707 | **7.90x** |
| 2026-02-17 | $79.01 | 424B7 cover | 871.2M | 1,831.8 | 70,671 | 8.62x |
| 2026-03-18 | $87.62 | 424B7 cover | 874.5M | 1,831.8 | 78,453 | 9.57x |
| 2026-07-08 | $231.71 | 424B7 cover | 875.8M | 1,030.1 | 203,932 | 21.58x |
| 2026-09-05 | $223.55 | workbook | 921.2M dil. | 1,030.1 | 206,985 | **21.90x** |

Source: 424B7 accessions 0001193125-26-040188, -055916, -115973,
0001193125-26-299840 (each states the prior-day Nasdaq close and shares
outstanding); net debt from 10-K FY26 and 10-Q Q2 FY27; revenue from
`00-base-facts.md`.

Trailing revenue rose **15.3%** between 2026-02-05 and today (FY26 $8,194.6M →
TTM $9,450.3M). The share price rose **201%**. **Roughly 93% of the realised
return since February is multiple.** CLAUDE.md §5 caps multiple expansion at 40%
of base-case return; the market has already spent 2.3x the fund's entire budget
for it, and any position taken today inherits that.

The 5-year median EV/revenue is **UNVERIFIED** (market MCP down; no price
history tool available). The best primary-source anchor available is MRVL's own
7.9x seven months ago. Compression to 6–8x forward revenue in three years loses
**14%–35%** with the business delivering 20%+ growth throughout.

### 1b · Impairment bear — the earnings power is lower than reported

This is the one that causes permanent loss, and there are four independent
mechanisms, each tied to a specific disclosure:

| # | Mechanism | The disclosure |
| --- | --- | --- |
| I | Reported gross-margin improvement is **entirely** purchase-amortisation roll-off; underlying margin is falling | Non-GAAP GM 59.4% (Q2 FY26) → 58.9% (Q2 FY27) → **57.5–58.5% guided Q3 FY27**, while GAAP GM rose 50.4% → 53.1% purely because acquired-intangible amortisation fell from 8.3% to 5.2% of revenue `[8-K 2026-08-27, acc 0001835632-26-000022]` |
| II | Management is **deliberately buying data-center share with price** | "The lower gross margin target as compared to the prior year reflected the expected near-term product mix shift… A decrease in the gross margin target was expected to increase overall financial performance by supporting **competitive pricing**, volume commitments, and start-up investments to capture share in the data center AI market" `[DEF 14A 2026-05-13, acc 0001104659-26-060253]` |
| III | Growth revenue is bought with warrants recorded as **contra-revenue** | 58.97M-share Google warrant, plus 4.2M (FY25) and 1.0M (FY26) customer warrants; "recognized as a reduction to revenue as qualifying revenues are recognized" `[10-Q Q2 FY27, acc 0001835632-26-000025]` |
| IV | **$8,518.9M of unconditional foundry take-or-pay** entered in six months against a demand forecast that has not been realised | Purchase commitments to foundries: $1,638.4M (2025-02-01) → $2,665.8M (2026-01-31) → **$8,518.9M (2026-08-01)**, +219% in one half-year `[10-K FY25, 10-K FY26, 10-Q Q2 FY27]` |

---

## 2 · Revenue quality

### 2.1 Gate 1 (Type A: ≥70% recurring or contracted) — **FAIL, definitively**

- Revenue is recognised **at a point in time on shipment**, including to
  distributors: "Control passes to the distributor upon shipment, and terms and
  payment by our distributors is not contingent on resale of the product."
  `[10-K FY26, Note 2]`
- Deferred revenue is **$63.7M** (2026-05-02) against $2,417.8M of quarterly
  revenue — **2.6%**. It was $40.1M at 2026-01-31 and $41.3M at 2025-08-02.
  `[10-Q Q1 FY27 acc 0001835632-26-000019; 10-Q Q2 FY26 acc 0001835632-25-000189]`
- There is no renewal, retention or backlog metric disclosed anywhere in the
  10-K or 10-Qs.

Contracted or recurring revenue is **near zero**. This is design-win revenue
that is sticky across a product cycle and gone at the next socket decision.
Testing MRVL against Type A, as instructed, Gate 1 fails outright.

### 2.2 Customer concentration — **KILL CRITERION TRIPPED**

| Period | Customer A (direct) | Distributor A | Top 10 |
| --- | --- | --- | --- |
| FY2024 | <10% | 24% | — |
| FY2025 | 13% | 34% | — |
| FY2026 | 14% | **37%** | **82%** |
| Q2 FY26 | 16% | 34% | — |
| **Q2 FY27** | **16%** | **44%** | — |
| H1 FY27 | 16% | **45%** | — |

Source: 10-K FY26 Item 1 and Note 2; 10-Q Q2 FY27 MD&A "Sales and Customer
Composition".

**Distributor A is 44% of Q2 FY27 revenue and rising 10 points a year.** Four
customers are **72% of gross accounts receivable** at 2026-08-01. Asia is **84%**
of revenue, up from 76%. `[10-Q Q2 FY27]`

CLAUDE.md §4 (Types A and B): *customer concentration >25% from one customer with
no multi-year contract.* No multi-year contract with Distributor A is disclosed.
The opposite is disclosed: distributors "may terminate their relationships with
us at any time," sales are on stock-rotation and price-protection terms, and
"with certain exceptions our partners are not obligated to perform services or
supply products to us for any specific period, in any specific quantities, or at
any specific price, except as may be provided in a particular purchase order."
`[10-K FY26 risk factors; 10-Q Q2 FY27 risk factors]`

**Tripped.** The Google commercial agreement of 2026-07-29 is a genuine
multi-year contract and partially answers the *direct* customer question, but
Distributor A — the larger and faster-growing exposure — is untouched by it.

### 2.3 Receivables and reserve divergence

| | Q2 FY26 | Q4 FY26 | Q2 FY27 |
| --- | --- | --- | --- |
| Revenue | 2,006.1 | 2,218.7 | 2,739.3 |
| Accounts receivable, net | 1,451.7 | 2,186.6 | 2,218.4 |
| **DSO (91-day)** | **65.9** | **89.7** | **73.7** |
| Variable consideration (ship & debit) accrual | 632.7 | 713.8 | 777.7 |
| **Accrual / quarterly revenue** | **31.5%** | 32.2% | **28.4%** |
| Prepaid ship and debits (asset) | 498.1 | 584.2 | 588.0 |

Source: XBRL `AccountsReceivableNetCurrent`, `RevenueFromContractWithCustomer…`;
balance-sheet detail notes in 10-Q Q2 FY26, 10-K FY26, 10-Q Q2 FY27.

Three observations, stated as observations:

- **AR grew 52.8% YoY against revenue +36.5%.** DSO is up 7.8 days (+11.9%).
- **Q4 FY26 DSO spiked to 89.7 days**, and the 10-K explains it: "The increase
  in accounts receivable was primarily due to **higher sales in the last two
  months of fiscal 2026**." That is a back-end-loaded quarter, disclosed.
- **The variable-consideration reserve fell from 31.5% to 28.4% of quarterly
  revenue.** Holding the prior-year ratio would require a reserve of $863.9M
  rather than $777.7M — an **$86.2M difference, 3.1% of Q2 FY27 revenue [EST]**.
  I am not asserting this is deliberate; I am stating that the reserve ratio
  declined while distributor concentration rose 10 points, and that is the line
  item to watch.

**Disconfirming this bear:** prepaid ship and debits (the distributor-inventory
proxy) grew only 18.0% YoY (498.1 → 588.0) against revenue +36.5%. That argues
**against** channel stuffing. I record it as such.

### 2.4 Acquisition accounting flattering organic growth — it does not

Celestial AI ($3.5B, closed 2026-02-02) and XConn (closed 2026-02-10) contributed
revenue that was **"not material"** `[10-Q Q2 FY27 Note 4]`. Reported Q2 FY27
growth of 36.5% is therefore organic, and is in fact understated because the
prior-year comparison includes automotive ethernet revenue that was divested on
2025-08-14. **The revenue growth is real.** This bear case is not about the
top line being fake; it is about what that top line costs and what it is worth.

### 2.5 Removed disclosure — the highest-signal finding in this section

The FY2025 10-K disaggregated revenue into **five end markets**: Data center,
Enterprise networking, Carrier infrastructure, Consumer, and Automotive/
industrial. The FY2026 10-K collapses this to **two**: "Data center" and
"Communications and other."

| End market | FY2023 | FY2024 | FY2025 | FY2026 |
| --- | --- | --- | --- | --- |
| Data center | 2,408.8 (41%) | 2,216.7 (40%) | 4,164.2 (72%) | 6,100.3 (74%) |
| Enterprise networking | 1,369.2 (23%) | 1,228.4 (22%) | 626.4 (11%) | *no longer disclosed* |
| Carrier infrastructure | 1,084.0 (18%) | 1,051.9 (19%) | 338.2 (6%) | *no longer disclosed* |
| Consumer | — | 622.4 (11%) | 316.1 (5%) | *no longer disclosed* |
| "Communications and other" | — | 3,291.0 (60%) | 1,603.1 (28%) | 2,094.3 (26%) |

Source: 10-K FY25 (acc 0001835632-25-000057) Note 3; 10-K FY26
(acc 0001835632-26-000011) Note 3.

Visibility into the four non-data-center businesses was withdrawn in the same
year the company became a single-story name. We can no longer verify whether
"Communications and other +10% YoY" in Q2 FY27 is broad recovery or one bucket.
Note also that the aggregate non-data-center business **halved** from $3,291.0M
(FY24) to $1,603.1M (FY25) — MRVL has already lived through a 51% collapse in
half its revenue base inside 24 months, and took ~$716M of impairments in a
single quarter doing so (§4.3). Q2 FY27 comms-and-other of $567.8M annualises to
$2.27B, essentially flat to FY26. **100% of growth is data center.**

---

## 3 · Earnings quality (Type A test: FCF/NI ≥0.8, 3-yr avg)

### 3.1 The Q3 FY26 gain — cause, amount, and the clean base

**Cause:** sale of the automotive ethernet business to Infineon Technologies AG
for $2.5B in cash, completed **2025-08-14** (start of Q3 FY26).

| Item | Amount | Source |
| --- | --- | --- |
| Cash proceeds, net of cash divested | 2,478.6 | XBRL `ProceedsFromDivestitureOfBusinessesNetOfCashDivested`, 10-K FY26 |
| **Pre-tax gain on sale** | **1,830.4** | XBRL `GainLossOnSaleOfBusiness`, 10-K FY26 and 10-Q Q3 FY26 |
| Location in P&L | "interest income and other, net" | 10-K FY26 MD&A |
| Tax reconciliation line "Sale of business" | **(117.6)** / (3.9)pp | 10-K FY26 tax note |
| **Tax attributable to the gain [EST]** | **266.8** | 21% × 1,830.4 − 117.6 |
| **After-tax gain [EST]** | **1,563.6** | |

**The clean FY2026 base:**

| | Reported | Clean [EST] |
| --- | --- | --- |
| Pre-tax income | 3,046.6 | 1,216.2 |
| Tax | 376.5 | 109.7 |
| **Net income** | **2,670.1** | **1,106.5** |
| **Net margin** | **32.6%** | **13.5%** |
| **Diluted EPS** | **$3.07** | **$1.27** |

Cross-check by quarter: Q1 177.9 + Q2 194.8 + Q3 (1,901.3 − 1,563.6 = 337.7) +
Q4 396.1 = **1,106.5**. Ties exactly.
[EST] method: statutory 21% on the gain less the disclosed $117.6M "Sale of
business" reconciling benefit. The 10-K does not disclose the tax on the gain
directly.

**Clean TTM GAAP net income = $1,076.3M** (2,639.9 reported less 1,563.6).
At $223.55 × 921.2M = $205,934M derived market cap, that is **191x clean
trailing GAAP earnings**, against **70x trailing non-GAAP** and **21.9x
EV/trailing revenue**.

Note also: FY26 **GAAP EPS ($3.07) exceeded non-GAAP EPS ($2.84)** — only
because of the divestiture. The proxy's defence of the CEO/Chairman structure
cites *"expanded gross margin on a GAAP basis"* and *"outsized **non-GAAP** EPS
growth"* in the same sentence — switching basis per metric, each time to the
flattering one. `[DEF 14A 2026-05-13]`

### 3.2 Q1 FY27 collapse to $34.5M — cause

Not operational. Q1 FY27 operating income was **$339.4M**, up 25.4% YoY.
The entire gap sits below the line:

| Q1 FY27 | Amount |
| --- | --- |
| Operating income | 339.4 |
| Interest expense | (52.8) |
| **Other expense, net** | **(203.3)** |
| Pre-tax income | 83.3 |
| Tax | (48.8) |
| **Net income** | **34.5** |

The driver, quoted: *"a **$331.8 million increase in fair value of the
contingent consideration liability** associated with the Celestial acquisition,
partially offset by an unrealized gain of $81.1 million from the forward stock
purchase contract."* `[10-Q Q1 FY27 MD&A, acc 0001835632-26-000019]`

Q2 FY27 took a further **$101.9M** earnout mark; H1 FY27 total **$433.7M**,
offset by **$131.0M** of forward-contract gain. `[10-Q Q2 FY27]`

**This is not a one-off.** It is a Level 3 mark-to-market on MRVL's own share
price that will recur every quarter until FY2029, and it moves **against** the
company when the stock rises. The company says so: *"significant changes in any
of these assumptions or inputs could materially affect the fair value of the
earnout and result in material non-cash gains or losses and **increased
volatility in our reported financial results**."* `[10-Q Q2 FY27 risk factors]`
The Q1/Q2 divergence the base facts flagged is fully explained: Q2's earnout
mark was one-third the size of Q1's.

### 3.3 Stock-based compensation — the core Type A earnings-quality failure

| | Q2 FY26 | Q2 FY27 | YoY |
| --- | --- | --- | --- |
| Revenue | 2,006.1 | 2,739.3 | +36.5% |
| **Total SBC** | **153.6** | **326.2** | **+112.4%** |
| SBC % of revenue | 7.7% | **11.9%** | +420bps |
| SBC in opex | 140.2 | 310.3 | +121.3% |
| GAAP operating income | 290.1 | 459.7 | +58.5% |
| Non-GAAP operating income | 698.8 | 1,003.2 | +43.6% |
| **GAAP vs non-GAAP op margin gap** | 2,030bps | **1,980bps** | |

Source: 8-K 2026-08-27 (acc 0001835632-26-000022) GAAP-to-non-GAAP
reconciliation, alongside GAAP from 10-Q Q2 FY27.

SBC is growing **3.1x faster than revenue**. H1 FY27 SBC of **$533.8M** is
**55.8% of H1 FY27 FCF** ($956.9M). Add the **$365.2M** of cash paid for tax
withholding on net share settlement (a financing outflow that is economically a
buyback) and H1 FY27 FCF after employee-equity cash cost is **$591.7M**, against
reported OCF of $1,244.3M.

Celestial adds **$190.1M** of post-acquisition SBC still to be recognised on
assumed options alone. `[10-Q Q2 FY27 Note 11]`

### 3.4 FCF/NI — Gate 3 is not passable

| FY | OCF | Capex (PP&E) | Intangibles | **FCF** | GAAP NI | FCF/NI |
| --- | --- | --- | --- | --- | --- | --- |
| FY2024 | 1,370.5 | 336.3 | 13.9 | 1,020.3 | **(933.4)** | n/m |
| FY2025 | 1,681.2 | 284.6 | 7.0 | 1,389.6 | **(885.0)** | n/m |
| FY2026 | 1,750.5 | 354.1 | 4.5 | **1,391.9** | 2,670.1 | 0.52 |
| FY2026 clean | 1,750.5 | 354.1 | 4.5 | 1,391.9 | 1,106.5 [EST] | 1.26 |
| H1 FY27 | 1,244.3 | 282.4 | 5.0 | 956.9 | 342.5 | 2.79 |

Source: XBRL `NetCashProvidedByUsedInOperatingActivities`,
`PaymentsToAcquirePropertyPlantAndEquipment`, `PaymentsToAcquireIntangibleAssets`,
`NetIncomeLoss`, all 10-K/10-Q as filed.

**Gate 3 = UNKNOWN, and UNKNOWN is not a pass.** Two of the last three fiscal
years were GAAP net losses, so a three-year FCF/NI average is not computable in
any meaningful way. MRVL first earned GAAP operating income in FY2026
(FY24 −567.7, FY25 −720.3, FY26 +1,322.9). **The "quality compounder" framing
rests on a single year of GAAP operating profitability, and that year's net
income was 59% a divestiture gain.**

Note also: FY26 OCF was flattered by roughly **$137M** of tax on the gain that
was accrued but unpaid at year end (accrued income taxes current 91.2 → 333.6 →
228.3), and the Q2 FY27 10-Q says liquidity must cover "the income tax related
to the sale of our automotive ethernet business" over the next twelve months.
That drag is being paid now (accrued income tax down to 163.7). Small — I am
sizing it at $140–240M, not thesis-changing, and I say so.

### 3.5 Non-GAAP add-backs vs GAAP opex — kill criterion, both readings

| Quarter | GAAP opex | Total opex special items | % | of which SBC + purchase amort. | "genuinely one-time" (restructuring + other) | % |
| --- | --- | --- | --- | --- | --- | --- |
| Q3 FY26 | 712.0 | 227.0 | **31.9%** | 213.6 | 13.4 | 1.9% |
| Q4 FY26 | 743.5 | 226.5 | **30.5%** | 207.3 | 19.2 | 2.6% |
| Q1 FY27 | 921.4 | 344.5 | **37.4%** | 267.8 | 76.7 | 8.3% |
| Q2 FY27 | 995.9 | 385.1 | **38.7%** | 382.5 | 2.6 | 0.3% |

Source: 8-K earnings releases acc 0001835632-25-000193, -26-000006, -26-000014,
-26-000022.

- **Literal reading of CLAUDE.md §4** ("non-GAAP add-backs >15% of GAAP opex in
  3 of the last 4 quarters"): **TRIPPED, 4 of 4.**
- **Reading to the heading's intent** ("serial *one-time* charges", i.e.
  excluding recurring SBC and purchase amortisation): **NOT tripped, 0 of 4.**

I surface both rather than resolving it silently. The criterion as written does
not carve out SBC. Either way the escalation-worthy fact is that the add-back
ratio **widened from 31.9% to 38.7% in four quarters**, and guided Q3 FY27
add-backs are $360M on $1,015M GAAP opex (**35.5%**). Non-GAAP opex is 39% below
GAAP opex and the gap is growing faster than revenue.

---

## 4 · Balance sheet

### 4.1 Gate 4 leverage — PASSES on reported debt

TTM EBITDA [EST] = TTM operating income 1,561.3 + D&A 368.8 + acquired-intangible
amortisation 892.7 = **$2,822.8M**.
(TTM operating income: Q3 FY26 357.8 + Q4 FY26 404.4 + Q1 FY27 339.4 + Q2 FY27
459.7. D&A: H2 FY26 180.3 + H1 FY27 188.5.)

**Net debt / TTM EBITDA = 0.36x.** Gate 4 threshold 3.0x: **PASS**.
EV/TTM EBITDA = **73.3x**.

### 4.2 What the $992M of new long-term debt funded — and the maturity wall

The $3,970.8M → $4,962.9M move is arithmetic, not a raise for acquisitions:

- **2026-04-15:** issued **$1.0B of 5.300% Senior Notes due 2036**.
- **Q1 FY27:** repaid the **$500.0M 1.650% 2026 Senior Notes** at maturity —
  these sat in **short-term** debt at 2026-01-31 ($499.8M current portion).
- Net face debt rose $500M (4,499.9 → 4,999.9); *long-term* debt rose $992M
  because $500M migrated out of current. `[10-Q Q2 FY27 Note 7]`

The Celestial/XConn cash ($1,270.9M, net of cash acquired) was funded by the
**$2.0B NVIDIA preferred**, not by debt (§4.4).

**Maturity schedule at 2026-08-01 (face value):**

| Fiscal year | Amount | Calendar dates |
| --- | --- | --- |
| Rem. FY2027 | — | |
| FY2028 | — | |
| **FY2029** | **1,249.9** | **$750.0M on 2028-04-15; $499.9M on 2028-06-22** |
| FY2030 | 500.0 | 2029-02-15 |
| FY2031 | 500.0 | 2030-07-15 |
| Thereafter | 2,750.0 | |

Source: 10-Q Q2 FY27 Note 7; maturity dates from 10-K FY26 Note 7.

**Strict reading of CLAUDE.md gate 4 ("no maturity wall inside 24 months"):
$1,249.9M matures on 2028-04-15 and 2028-06-22 — 19 and 21 months from today.
That is inside the window.** Mitigant, stated plainly: $3,932.8M of cash and an
undrawn $1.5B revolver (available to 2030-06-30, in compliance) cover it three
times over. I score this **PASS with a flag**, not a fail — but the base facts
asked whether there is a wall inside 24 months and the answer is yes, there is
$1.25B of it.

Covenants are modelable and light: incurrence-style limits on liens, sale-
leaseback and mergers; a 101% change-of-control put conditional on a ratings
downgrade below IG. No maintenance leverage covenant disclosed.

### 4.3 The real balance-sheet risk is off it — $9.5B of unconditional commitments

| Obligation at 2026-08-01 | Rem. FY27 | FY28 | FY29 | FY30 | FY31 | Thereafter | **Total** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Foundry / test & assembly | 1,829.3 | 2,125.4 | 2,178.3 | 2,201.8 | 66.0 | 118.1 | **8,518.9** |
| Technology services & licences | 94.1 | 196.4 | 146.1 | 132.4 | 63.4 | 33.9 | **666.3** |
| Capex commitments | — | — | — | — | — | — | **351.6** |
| **Total** | | | | | | | **9,536.8** |

**The trend is the finding:**

| Foundry / test & assembly commitments | Total | FY2029 tranche | FY2030 tranche |
| --- | --- | --- | --- |
| at 2025-02-01 | 1,638.4 | 106.5 | 66.3 |
| at 2026-01-31 | 2,665.8 | 68.6 | 66.3 |
| **at 2026-08-01** | **8,518.9** | **2,178.3** | **2,201.8** |

Source: 10-K FY25 Note 8; 10-K FY26 Note 9; 10-Q Q2 FY27 Note 9.

**+219% in six months**, and the FY2029/FY2030 tranches went up **32x**. These
are unconditional: *"cancellation of outstanding purchase orders is allowed but
requires payment of all costs and expenses incurred through the date of
cancellation, and in some cases, may result in incremental fees, loss of amounts
paid in advance, or loss of priority to reserved capacity."*

The mechanic is named in the risk factors: *"we have entered into a **capacity
reservation agreement with TSMC** pursuant to which we agreed to make substantial
advance payments in exchange for wafer capacity over a multi-year period. Under
this arrangement, **we are required to purchase specified target quantities of
wafers** during the term, and **if we do not meet such target quantities, we may
forfeit a proportional portion of our advance payments**… if we are able to
secure capacity, we may be obligated to use all of that capacity or incur
penalties."* `[10-Q Q2 FY27 Item 1A]`

Prepayments already made and sitting on the balance sheet: **$487.0M** at
2026-08-01, up from $278.8M at 2026-01-31 and $302.2M at 2025-08-02.

**Adjusted leverage:** (net debt 1,030.1 + foundry commitments 8,518.9) / TTM
EBITDA 2,822.8 = **3.38x**, above the 3.0x gate. This is a stress lens, not the
gate calculation — but $8.5B of take-or-pay against a 44%-concentrated
distributor channel is the single largest number on this page, and it is
off-balance-sheet.

**There is precedent for what happens when the demand doesn't show.** In Q3
FY2025, when the non-data-center business rolled over, MRVL took **$358.3M** of
restructuring charges in opex and **$357.9M** of impairments in COGS in one
quarter — a −46.4% GAAP operating margin. `[8-K 2025-12-02 reconciliation;
10-K FY26 MD&A]` MRVL has run this exact play once already, at a fraction of
today's committed capacity.

### 4.4 Capital structure changes the base facts do not capture

| Item | Date | Terms | Dilution |
| --- | --- | --- | --- |
| **NVIDIA Series A Convertible Preferred** | 2026-03-31 | 2.0M shares, $1,000 stated value, **$2.0B**, convertible at **~$91.84**, no redemption rights, participates pro rata, dividends as-converted | **21.8M shares (2.4%)**, already in the 921.2M diluted count |
| **Celestial earnout** | through FY2029 | Max **$233.0M cash + 22.4M shares** (risk factor says **24.4M**); liability **$749.5M** at 2026-08-01, Level 3 Monte Carlo | up to **+2.6%** |
| **Google warrant** | 2026-08-18 | **58,970,907 shares @ $206.58**, 1.36M time-based, 57.61M in **240 tranches of one per $500M of Google custom revenue**, expiry 2033-08-18 | up to **+6.4%** |
| FY25 / FY26 customer warrants | Dec-24 / Dec-25 | 4.2M @ $87.77 (FV $227.6M) and 1.0M @ $87.00 (FV $55.4M); 1.2M vested | +0.6% |
| Celestial / XConn stock consideration | Q1 FY27 | 26.8M shares issued (24.6M + 2.26M) | already issued |
| Forward stock purchase contract | Apr-2026 | $300M notional, 12 months, hedges the earnout; **$131.0M asset** at 2026-08-01 | — |

Sources: 10-Q Q2 FY27 Notes 4, 6, 10, 11, 15; 8-K 2026-08-19; 10-K FY26 Note 12.

**Fully-loaded dilution overhang: 64.2M warrant shares + up to 24.4M earnout
shares = 88.6M shares, 9.6% of today's diluted count**, on top of ~5.8% YoY
share growth already recorded.

Two things about the Google warrant deserve emphasis because they change the
economics of the growth story, not just the share count:

1. **Full vesting requires $120.0B of Google custom-products revenue** (240
   tranches × $500M) by end of FY2033. That is the implied demand curve behind
   the current multiple.
2. **The warrant is contra-revenue, not an expense.** MRVL's stated policy:
   warrant shares "are recognized as a reduction to revenue as qualifying
   revenues are recognized during the vesting term." Applying the fair-value
   ratio from MRVL's own prior warrants (FV/strike = 62.0% and 60.9%) to a
   $206.58 strike implies **~$126/share [EST]**, or **~$7.3B of grant-date fair
   value on the performance tranche** — **~6.1% of the $120B of revenue it is
   earned against [EST]**. Every dollar of Google revenue arrives ~6% smaller
   than it looks, permanently, and the grant-date fair value has not yet been
   disclosed. **[EST]** method: MRVL's disclosed Black-Scholes FV/strike ratios
   on the FY25 and FY26 warrants, applied to the new strike. The 10-Q gives no
   fair value for the Google warrant; it is a subsequent event.

**Forward-contract asymmetry:** the $300M forward stock purchase contract is a
$131.0M asset today because the stock rose. The risk factor says the reverse:
*"we may be required to make a significant cash payment at settlement (or upon
early termination) **if our stock price declines** relative to the forward
price."* In the bear scenario the stock falls and MRVL writes a cheque.

---

## 5 · Disconfirming disclosures found

Ranked by signal.

1. **Revenue disaggregation collapsed from five end markets to two** between the
   FY25 and FY26 10-Ks (§2.5). Removed disclosure, in the year the business
   became a single story. Highest signal on this page.
2. **The proxy states management deliberately lowered the gross-margin target to
   buy share with price.** *"A decrease in the gross margin target was expected
   to increase overall financial performance by supporting **competitive
   pricing**, volume commitments, and start-up investments to capture share in
   the data center AI market."* `[DEF 14A 2026-05-13]` This is the company
   confirming, in a compensation document, the margin path the bear needs.
3. **New risk factor on hyperscaler insourcing.** *"AI-driven design tools may
   lower traditional barriers to entry… enabling new market participants,
   including technology companies that have not historically engaged in chip
   design, to develop high-performance, **custom semiconductor solutions
   in-house** with reduced reliance on third-party chip suppliers. This trend
   toward **'insourcing' or 'vertical integration' could reduce demand for our
   products and erode our market share**. In particular, **large cloud computing
   providers**… have already begun investing in proprietary chip design
   capabilities."* `[10-Q Q2 FY27 Item 1A]` MRVL's entire growth thesis is
   selling custom silicon to large cloud providers. It has now written the bear
   case for that thesis into its own risk factors.
4. **The TSMC take-or-pay mechanic and the $8.5B commitment build** (§4.3).
5. **CFO resigned with five days' notice.** Willem Meintjes notified the company
   on 2026-06-10 and left on 2026-06-15, after serving since January 2023.
   `[8-K 2026-06-11, acc 0001193125-26-267688]` Not a kill criterion. It is a
   CFO leaving in the middle of the largest capital-structure rebuild in the
   company's history (NVIDIA preferred, $1B notes, $3.5B acquisition, $8.5B of
   new commitments), with a same-day "reaffirming Q2 guidance" press release
   attached — which tells you the board expected the market to read it as bad.
6. **Sole-source foundry.** *"TSMC is currently our sole source foundry for all
   of our advanced process-node wafers,"* including 3nm. `[10-Q Q2 FY27]`
7. **"We are currently in a supply constrained environment."** `[10-Q Q2 FY27]`
   Revenue is supply-limited, which means bookings commentary ("AI-related
   bookings remain exceptionally robust") is not a revenue forecast, and the
   $8.5B of capacity was bought to relieve that constraint at exactly the moment
   the constraint is most likely to be a peak-cycle artefact.
8. **Competitive consolidation in custom silicon:** *"in August 2026 AMD
   announced its intent to acquire Taalas Inc."* `[10-Q Q2 FY27]`
9. **Fabless cost rigidity in a downturn:** *"because we do not operate our own
   manufacturing… **we are not able to reduce our costs as rapidly** as
   companies that operate their own facilities and our costs may even
   increase."* `[10-Q Q2 FY27]`

**Disconfirming the bear** (recorded honestly):
- Related-party transactions: **"None."** `[10-K FY26 Item 7]`
- Auditor **Deloitte**, unqualified opinion on financials and ICFR; disclosure
  controls concluded **effective** at 2026-01-31 and 2026-08-01; no material
  weakness, no restatement. `[10-K FY26 Item 9A; 10-Q Q2 FY27 Item 4]`
- Revenue guidance beaten **five consecutive quarters** (+0.3% to +1.5% over the
  midpoint each time). Non-GAAP EPS beaten every quarter.
- Prepaid ship and debits grew far slower than revenue (§2.3) — argues against
  channel stuffing.
- Celestial contributed no material revenue, so reported growth is organic.
- Google signed a real multi-year commercial agreement on 2026-07-29.

---

## 6 · Bear math

### 6.1 Starting point

FY27E revenue = Q1 2,417.8 + Q2 2,739.3 + Q3 guide 3,150.0 (midpoint,
`[8-K 2026-08-27]`) + Q4 **[EST]** 3,439 = **$11,746M**. Q4 [EST] method:
+55% YoY on Q4 FY26 of $2,218.7M, consistent with management's stated
"growth accelerates each quarter."

| Metric today | Value |
| --- | --- |
| Derived market cap | $205,934M (921.2M diluted × $223.55) |
| Derived EV | $206,964M |
| EV / TTM revenue | **21.9x** |
| EV / FY27E revenue | 17.6x |
| EV / TTM EBITDA | 73.3x |
| P / TTM non-GAAP net income ($2,924.0M) | 70.4x |
| **P / clean TTM GAAP net income ($1,076.3M)** | **191.3x** |

### 6.2 Three bear paths, 3-year (to FY2030, exit Sept 2029)

Exit multiple discipline: CLAUDE.md requires terminal multiple ≤ trailing 5-year
median. **The 5-year median is UNVERIFIED** (no price-history tool). The
substitute anchor is MRVL's own **7.9x EV/trailing revenue on 2026-02-05**, a
primary-source figure from a 424B7 cover. All exit multiples below are at or
below that.

| | **A · Compression** | **B′ · Moderate impairment (central bear)** | **B · Severe impairment** |
| --- | --- | --- | --- |
| One-sentence driver | Business delivers; multiple normalises to where it traded seven months ago | AI capex digests; custom mix + Google warrant contra-revenue compress margin; growth falls to mid-single digits | Hyperscaler insourcing takes one program; Distributor A cuts orders; $8.5B take-or-pay is eaten |
| FY28 revenue | 15,200 (+29%) | 12,500 (+6%) | 9,400 (−20%) |
| FY30 revenue | 21,000 | 14,000 | 10,400 |
| Exit NTM (FY31E) revenue | 23,600 | 14,700 | 10,900 |
| Non-GAAP gross margin at exit | 58% | 55% | 54% |
| Non-GAAP opex | 3,400 | 3,000 | 2,700 |
| Non-GAAP operating income | 8,780 | 4,700 | 2,916 |
| FCF (reported) | ~5,900 | ~3,210 | ~1,730 |
| FCF less SBC (economic) | ~4,000 | ~1,610 | ~330 |
| **Exit EV / NTM revenue** | **6.0x** | **5.0x** | **3.0x** |
| Exit EV | 141,600 | 73,500 | 32,700 |
| Net cash at exit [EST] | 4,000 | 6,000 | 1,500 |
| Equity value | 145,600 | 79,500 | 34,200 |
| Diluted shares at exit [EST] | 999M | 990M | 981M |
| **Price / share** | **$145.75** | **$80.30** | **$34.86** |
| **3-year total return** | **−34.8%** | **−64.1%** | **−84.4%** |
| **3-year IRR** | **−13.3%/yr** | **−28.9%/yr** | **−46.2%/yr** |

Share-count method: 921.2M today (includes the NVIDIA preferred as-converted)
+ Google warrant vesting proportional to assumed Google revenue + Celestial
earnout (A: full 24.4M; B′: partial; B: zero) + net SBC dilution of ~1.5–2.0%/yr
less buybacks. Cross-check on B′: exit EV/FCF = 22.9x, which is not a distressed
multiple.

**The central bear (B′) loses 64.1%.** Even the pure compression bear (A), in
which the business compounds 21%/yr for three years, loses **34.8%** at 6.0x and
**13.7%** at 8.0x.

**CLAUDE.md §5 requires a bear case that loses <25%. The central bear loses
64%. Only the most generous version of the compression bear — business delivers
21% CAGR *and* still holds 8x forward revenue in 2029 — clears the threshold.
The name fails the §5 asymmetry test.**

### 6.3 The base case is the finding too

To hit CLAUDE.md's **15% base-case IRR**, MRVL must reach $339.94/share by
Sept 2029 → equity $336.5B → EV ~$332.5B. Against FY31E revenue of $23.2B
(20% CAGR for three years, then 15%), that is **14.3x EV/NTM revenue at exit**.

Today's forward multiple (EV / FY28E revenue of ~$15.2B) is **13.6x**.

**So the base case requires 20% compounding for three years with essentially
zero multiple compression off an already-13.6x forward multiple.** Decomposed:
at 20% CAGR and an 11x exit, the total return is **−1.8%**. The revenue growth
is worth roughly +125% over three years; everything else is the multiple. Under
CLAUDE.md's 40% cap on multiple contribution, this thesis cannot be written as a
business-quality thesis. It is a multiple-persistence thesis.

---

## 7 · Kill criteria results — every one, tripped or not

### Universal

| # | Criterion | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Net insider selling >$10M in trailing 6 months **with no 10b5-1 plan disclosed at adoption** | **NOT TRIPPED** (flag) | Gross sales 2026-03-05→2026-09-05: **$47,294,754** across 23 Form 4 code-S transactions. **Zero code-P purchases.** But **$42.65M was under 10b5-1 plans with adoption dates disclosed** (e.g. Murphy: "10b5-1 Plan adopted… on December 16, 2025"; Bharathi: "10b5-1 Plan dated December 4, 2025"). Non-plan sales total **$4.64M** (Casper $4.01M across four April 2026 open-market sales; Durn $0.63M) — below $10M. Sellers: Murphy (CEO) $10.88M, Bharathi (Pres. Data Center) $15.61M, Koopmans (COO) $11.45M, Meintjes (former CFO) $4.72M, Casper (CLO) $4.01M, Durn (CFO) $0.63M. `[Forms 4, CIK 1835632]` |
| 2 | Auditor resignation / unremediated material weakness >2 quarters / revenue restatement | **NOT TRIPPED** | Deloitte, unqualified on financials and ICFR; disclosure controls effective at 2026-01-31 and 2026-08-01. `[10-K FY26 Item 9A; 10-Q Q2 FY27 Item 4]` |
| 3 | Serial "one-time" charges: non-GAAP add-backs >15% of GAAP opex in 3 of last 4 quarters | **TRIPPED on the literal reading (4 of 4: 31.9%, 30.5%, 37.4%, 38.7%). NOT tripped on the heading's intent (0 of 4: 1.9%, 2.6%, 8.3%, 0.3%).** | §3.5. Escalating to PM — the criterion as written does not carve out SBC, and SBC is the add-back that grew 112% YoY. |
| 4 | Missed own guidance 3+ times in 8 quarters with no framework change | **NOT TRIPPED** | Revenue beaten 5 of 5 quarters checked (Q2 FY26 → Q2 FY27). Non-GAAP EPS beaten every quarter. **One** GAAP EPS miss: Q1 FY27 guided $0.31 ±$0.05, actual **$0.04**. `[8-Ks 2025-05-29 through 2026-08-27]` |
| 5 | Related-party transactions material to earnings | **NOT TRIPPED** | 10-K FY26 Item 7: "Related Party Transactions — **None.**" NVIDIA holds 2.4% as-converted, below the 5% "related person" threshold, so its $2.0B purchase plus commercial partnership is not a disclosable RPT. Noted, not counted. |
| 6 | Share count growing >4%/yr with no corresponding revenue-per-share growth | **NOT TRIPPED** (confirms base facts) | Diluted shares +5.84% YoY; revenue/share +29.0%. But note **9.6% of additional dilution overhang** is contracted (64.2M warrant + 24.4M earnout shares), and $400M of H1 buybacks did not prevent the share count from rising — CLAUDE.md §5 forbids counting those as return of capital. |
| 7 | Thesis requires trusting a number we cannot tie to a filing | **NOT TRIPPED for this memo.** Every figure above is filing-sourced. **Flag:** the Google warrant's grant-date fair value — the number that determines how much contra-revenue the largest growth driver carries — **has not been disclosed**. It is a subsequent event with no valuation given. Any bull model of FY28–FY33 revenue that ignores it is trusting a number that does not exist yet. |

### Types A and B

| # | Criterion | Result | Evidence |
| --- | --- | --- | --- |
| 8 | Customer concentration >25% from one customer with no multi-year contract | **TRIPPED** | Distributor A = **44% of Q2 FY27 revenue, 45% of H1 FY27, 37% of FY26**, up from 24% in FY24. No multi-year contract with Distributor A is disclosed; distributor terms include stock rotation, price protection and termination at will. Four customers = 72% of gross AR. `[10-Q Q2 FY27 MD&A; 10-K FY26 Note 2 and Item 1A]` |

### Types C and D
Not applicable — MRVL is not a financial or a resource business. Recorded for
completeness per the working agreement.

### Gate scoring implied by this work (for the memo's gate table)

| Gate | Type A test | Score | Basis |
| --- | --- | --- | --- |
| 1 Revenue durability | ≥70% recurring/contracted | **FAIL** | Point-in-time revenue on shipment; deferred revenue 2.6% of a quarter; no retention metric (§2.1) |
| 2 Unit economics | GM ≥50%, stable-to-rising 3 yrs | **PASS on GAAP, FAIL on trend** | GAAP GM 53.1% clears; but the rise is amortisation roll-off and underlying non-GAAP GM fell 59.4% → 58.9% → 58.0% guided (§1b-I) |
| 3 Earnings quality | FCF/NI ≥0.8, 3-yr avg | **UNKNOWN** — not a pass | Two of three years GAAP net losses; ratio not computable (§3.4) |
| 4 Balance sheet | Net debt/EBITDA ≤3.0x, no wall in 24m | **PASS (0.36x) with flag** | $1,249.9M matures Apr/Jun 2028, inside 24 months, covered 3x by cash. Adjusted for $8.5B foundry take-or-pay: 3.38x (§4) |
| 5 Incentives | Insider ≥3% or named operator; comp tied to per-share value | **FAIL, twice** | All directors and executive officers = **1,046,798 shares = 0.12%** of 847.3M; CEO 412,871 = 0.05%. AIP weighted **50% revenue / 15% non-GAAP gross margin / 35% non-GAAP operating margin**; PSUs use a **non-GAAP EPS CAGR** multiplier. CLAUDE.md: "Comp tied to 'adjusted' anything is a gate 5 failure regardless of type." `[DEF 14A 2026-05-13]` |
| 6 Reinvestment runway | ≥50% of FCF redeployable at ≥ current ROIC for 3+ yrs | **UNKNOWN** | Goodwill $13,873.9M against total equity $18,531.6M; **tangible common equity ≈ $311M** after removing $13,873.9M goodwill, $2,346.6M acquired intangibles and the $2,000M preferred. Redeployment to date is $3.5B for a business with immaterial revenue |

---

## 8 · What would change my mind

Ordered by how much each would move the bear case, with the specific disclosure
that would settle it.

1. **The Google warrant's grant-date fair value, and where it lands.** If MRVL
   discloses in the Q3 FY27 10-Q that the performance-tranche fair value is well
   below my ~$7.3B [EST] — say under $3B — the contra-revenue drag drops to
   ~2.5% of Google revenue and mechanism III largely goes away. **Date: Q3 FY27
   10-Q, ~early December 2026.**
2. **Distributor A falling below 30% of revenue while total revenue still grows.**
   That would mean the growth has broadened and the kill criterion clears. The
   opposite — Distributor A above 50% — makes the impairment bear the base case.
   **Date: quarterly, 10-Q MD&A "Sales and Customer Composition."**
3. **Non-GAAP gross margin stabilising above 58% for two consecutive quarters
   with custom revenue growing.** That would falsify mechanisms I and II
   together. Guided Q3 FY27 is 57.5–58.5%; a print at 58.5%+ with custom
   accelerating would be a genuine surprise. **Date: 2026-12 and 2027-03 8-Ks.**
4. **Foundry commitments flattening rather than compounding.** If the total
   holds near $8.5B and the FY29–FY30 tranches convert to revenue on schedule,
   the take-or-pay is a competitive moat rather than a liability. If it goes to
   $12B+ while revenue growth decelerates, mechanism IV becomes the story.
   **Date: quarterly, Note 9.**
5. **SBC growth converging to revenue growth.** SBC at 11.9% of revenue and
   growing 112% YoY against revenue +36.5% is the Type A quality failure. Two
   quarters of SBC growing slower than revenue would restore the FCF bridge.
   **Date: quarterly cash-flow statement.**
6. **Any insider buying at all.** Zero code-P purchases in six months while the
   stock tripled, against $47.3M of sales and 0.12% aggregate insider ownership,
   is the cleanest available read on how the people with the information value
   the multiple. A single meaningful open-market purchase would be evidence
   against me. **Date: any Form 4.**
7. **The October 6, 2026 Investor Day.** Management has pre-committed to
   "sharing Marvell's long-term strategy" there. A multi-year revenue target
   that is *net* of warrant contra-revenue, with a gross-margin bridge and a
   custom-vs-connectivity mix disclosure, would restore the segment visibility
   removed in the FY26 10-K. A target stated gross of the warrant would confirm
   the bear. **Date: 2026-10-06.**

**What would not change my mind:** another quarter of revenue beating guidance
by 1%. At 21.9x EV/trailing revenue and 191x clean trailing GAAP earnings, the
compression bear does not require the business to disappoint. It only requires
the market to stop paying 2.8x what it paid for the same order book in February.

---

## 9 · Sizing implication (for the PM, not a recommendation)

The holder carries **$25,365 — 25.3% of the Brokerage Link account and 23.1% of
that account's risk** `[00-base-facts.md]`. At the central bear of −64.1%, that
position alone costs **16.2% of the account**. At the severe bear, **21.4%**.

The liquidity ceiling under CLAUDE.md §2.1 cannot be computed: 20-day median
dollar volume is **UNVERIFIED** (market MCP server down). At MRVL's scale the
gate is almost certainly non-binding for a $25K position, but it is recorded as
unverified rather than assumed.

CLAUDE.md §5 states the bear case must lose <25%. It loses 64%. Under the
fund's own doctrine that is a sizing constraint before it is anything else.

---

### Sources used

10-K FY2026 `0001835632-26-000011` · 10-K FY2025 `0001835632-25-000057` ·
10-Q Q2 FY27 `0001835632-26-000025` · 10-Q Q1 FY27 `0001835632-26-000019` ·
10-Q Q3 FY26 `0001835632-25-000197` · 10-Q Q2 FY26 `0001835632-25-000189` ·
10-Q Q1 FY26 `0001835632-25-000117` · DEF 14A `0001104659-26-060253` ·
8-K earnings `0001835632-25-000115`, `-25-000187`, `-25-000193`,
`0001835632-26-000006`, `-26-000014`, `-26-000022` ·
8-K Google warrant `0001193125-26-356217` · 8-K CFO transition
`0001193125-26-267688` · 424B7 `0001193125-26-040188`, `-26-055916`,
`-26-115973`, `0001193125-26-299840` · Forms 4, CIK 1835632, 2026-03-26 to
2026-09-02 · XBRL companyfacts, CIK 0001835632.

All figures USD millions unless noted. Fiscal year ends ~31 January; FY2027 ends
January 2027. `[EST]` marks estimates with method stated inline.
