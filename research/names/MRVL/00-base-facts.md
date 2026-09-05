# MRVL — Base Facts

**Established once. Every agent reads this file before starting and uses these
figures.** Do not re-derive them; if you believe one is wrong, say so rather
than silently substituting your own.

Marvell Technology, Inc. · CIK `0001835632` · Nasdaq · SIC 3674 Semiconductors
& Related Devices · incorporated Delaware · **fiscal year ends ~31 January**,
so FY2027 ends Jan 2027 and Q2 FY27 ran 2026-05-03 to 2026-08-01.

All figures from EDGAR XBRL as reported, with accession numbers. USD millions.

## Business type — UNRESOLVED, flag for doctrine

MRVL fits **no CLAUDE.md §3.0 type cleanly**, and the real numbers confirm it:

- **Type A** (recurring) requires GM ≥50% *and* ≥70% recurring or contracted
  revenue. Gross margin **clears at 53.1%**; the revenue test almost certainly
  fails — fabless semiconductor design-win revenue is sticky across product
  cycles but is not contracted recurring. **Requires the 10-K to settle.**
- **Type B** (asset-heavy) is wrong on its face: fabless outsources fabrication.
- **C and D** do not apply.

Working assumption: **test against Type A, the stricter**, per the §3.0 rule for
names fitting two types — noting it fits one and a half. Gate 1 is the open
question and is the reason this name is worth the workup.

## Revenue

| Period | Revenue | YoY | Accession |
| --- | --- | --- | --- |
| FY2025 (to 2025-02-01) | 5,767.3 | — | 0001835632-25-000057 |
| FY2026 (to 2026-01-31) | **8,194.6** | **+42.1%** | 0001835632-26-000011 |
| Q2 FY26 (2025-05-04→2025-08-02) | 2,006.1 | — | 0001835632-25-000189 |
| Q2 FY27 (2026-05-03→2026-08-01) | **2,739.3** | **+36.5%** | 0001835632-26-000025 |
| H1 FY26 | 3,901.4 | — | 0001835632-25-000189 |
| H1 FY27 | 5,157.1 | +32.2% | 0001835632-26-000025 |
| **TTM** (Q3 FY26 + Q4 FY26 + Q1 FY27 + Q2 FY27) | **9,450.3** | — | derived, components cited below |

TTM components: Q3 FY26 2,074.5 · Q4 FY26 2,218.7 *(= FY26 8,194.6 less 9M
5,975.9)* · Q1 FY27 2,417.8 · Q2 FY27 2,739.3.

## Gross profit and margin

| Period | Gross profit | Margin |
| --- | --- | --- |
| FY2026 | 4,180.7 | 51.0% |
| Q2 FY26 | 1,010.6 | 50.4% |
| Q2 FY27 | **1,455.6** | **53.1%** |
| H1 FY27 | 2,716.4 | 52.7% |

Margin is rising: +270bps YoY in Q2. `[10-Q 0001835632-26-000025]`

## Net income — READ THE WARNING

| Period | Net income |
| --- | --- |
| FY2026 | 2,670.1 |
| — of which **Q3 FY26 alone** | **1,901.3** |
| Q2 FY26 | 194.8 |
| Q2 FY27 | **308.0** (+58.1% YoY) |
| H1 FY26 | 372.7 |
| H1 FY27 | **342.5** (−8.1% YoY) |

**71% of FY2026 GAAP net income landed in a single quarter (Q3 FY26,
$1,901.3M), against $194.8M in Q2 FY26 and ~$396.1M in Q4 FY26.**

FY2026 net income is therefore **not a usable base for earnings power**, and any
multiple computed on it is meaningless. The pattern is a fact from XBRL; the
*cause* is not established here — a one-time gain, most plausibly a divestiture,
is the obvious candidate. **`filing-analyst` and `bear-case`: confirm the cause
from the 10-K and quantify the clean number. Do not assume.**

Note also the divergence: Q2 earnings **+58%** YoY while H1 earnings are
**−8%** YoY, because Q1 FY27 net income was only $34.5M against ~$177.9M in
Q1 FY26. Whatever hit Q1 needs explaining.

## Cash flow

| Period | Operating cash flow | OCF / net income |
| --- | --- | --- |
| FY2026 | 1,750.5 | 0.66 *(distorted by the Q3 gain)* |
| H1 FY26 | 794.5 | 2.13 |
| H1 FY27 | **1,244.3** | **3.63** |

Gate 3 wants FCF/NI ≥0.8. **Capex has not been pulled — FCF is UNKNOWN.**
`revenue-quality`: pull `PaymentsToAcquirePropertyPlantAndEquipment` and
complete this.

## Balance sheet, as of 2026-08-01

| | Amount |
| --- | --- |
| Cash and equivalents | 3,932.8 |
| Long-term debt (noncurrent) | 4,962.9 |
| **Net debt (approximate)** | **1,030.1** |

Excludes current maturities and short-term investments — **approximate**.
Debt rose from 3,970.8 at 2026-01-31 to 4,962.9 at 2026-08-01, roughly **+$992M
in six months**, while cash rose from 2,638.8 to 3,932.8. `bear-case`: find what
the raise funded and whether there is a maturity wall inside 24 months.

EBITDA not computed (no D&A or operating income pulled), so net debt/EBITDA is
**UNKNOWN**. At any plausible EBITDA on $9.45B TTM revenue the gate 4 threshold
of 3.0x clears comfortably, but state the computed figure, not this inference.

## Share count and dilution

| Period | Diluted WA shares | Revenue / share |
| --- | --- | --- |
| Q2 FY26 | 870.4M | $2.305 |
| Q2 FY27 | **921.2M** (+5.84%) | **$2.974** (+29.0%) |
| FY2026 | 869.7M | — |

**Kill criterion §4 — dilution: NOT TRIPPED.** Share count grew 5.84% YoY,
above the 4% threshold, **but revenue per share grew 29.0%**, which is the
"corresponding revenue-per-share growth" the criterion requires. The dilution
bought growth. Note it, do not kill on it.

## Price and valuation inputs

**The market MCP server is down** (yfinance host not in the network allowlist),
so price is taken from the holder's workbook and market cap is **derived, not
vendor-supplied**. Label it that way in any output.

| | Value | Source |
| --- | --- | --- |
| Price | $223.55 | IRA_Portfolio.v2.0.xlsx, as of 2026-09-05 |
| Diluted shares | 921.2M | 10-Q 0001835632-26-000025 |
| **Market cap (derived)** | **~$205,955M** | price × diluted shares |
| **EV (derived)** | **~$206,985M** | market cap + net debt 1,030.1 |
| **EV / TTM revenue** | **~21.9x** | 206,985 / 9,450.3 |

## The holder's position

$25,365 — 25.3% of the Brokerage Link (401K) account and **23.1% of that
account's risk**. Cost basis $264.45 against $223.55, **down 15.5%**. 32% below
the 52-week high of $329.88. 13-week realized volatility **71%**. The account is
tax-deferred, so rebalancing costs nothing.

## Open items for the team

1. **Gate 1** — what share of revenue is recurring or contracted? This decides
   the business type and is the whole reason for the workup.
2. **The Q3 FY26 gain** — cause, amount, and the clean earnings base.
3. **Q1 FY27 collapse** to $34.5M net income — cause.
4. **Capex** — to complete FCF and gate 3.
5. **EBITDA and the maturity schedule** — to complete gate 4.
6. **Customer concentration** — §4 kills above 25% from one customer without a
   multi-year contract. Hyperscaler custom-silicon revenue is exactly where this
   risk lives.
