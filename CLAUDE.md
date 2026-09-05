# Meridian Freeman Capital — Diligence Brain

This file is read before every task. It encodes *how this fund thinks*, so every
output — screen, memo, model, scenario — comes out in the same shape.

---

## 1. Mandate & Edge

- **Strategy:** fundamental, concentrated long book of quality compounders.
- **Holding period:** 2–4 years. Underwriting is done to a 3-year forward IRR.
- **Position count:** 12–18 longs. Top 5 carry ~50% of gross.
- **Edge claim:** *time arbitrage on business quality* — the market discounts
  durable compounding when the near-term print is noisy. Our work is to
  separate a bad quarter from a broken business.
- **What we are not:** not a macro fund, not a quant fund, not an event-driven
  fund. If a thesis depends on rates, an election, or a deal closing, it is
  out of mandate regardless of how good it looks.

**Every thesis must name its edge explicitly as one of:**

| Edge type | What it claims | How we prove it |
| --- | --- | --- |
| Time arbitrage | Market is right, but early | Show the cash-flow inflection and why consensus can't underwrite it yet |
| Analytical | We know the unit economics better | Segment/cohort math the sell-side does not publish |
| Structural | Forced sellers, index events, coverage gaps | Show who is selling and why they must |

A thesis with no nameable edge is a coin flip. Kill it.

---

## 2. Coverage Universe

Working record in `universe/coverage.md`.

**Size: all caps.** There is no market-cap band. Size discipline comes from
liquidity math computed per name, not from a universe rule — see §2.1.

**Geography:** US and Canada primary listings. ADRs only with a domestic comp
and a 20-F we can reconcile.

**Sectors: all in scope**, classified into the four business types in §3. The
type determines which version of the gates applies. Classify before you
diligence; the wrong type applies the wrong tests and produces a confident
wrong answer.

**Still out of mandate** — excluded by the strategy, not by sector. Each of
these has no compounding to underwrite or no verifiable earnings power:

- Pre-revenue and pre-earnings-power: clinical-stage biotech, pre-production
  mining and development-stage E&P, pre-deal SPACs.
- Businesses whose economics cannot be tied to filings: opaque holdcos,
  structures where unconsolidated JVs carry the majority of earnings.
- Anything where the thesis requires trusting a number we cannot verify.

Out-of-mandate names are not researched. Say so and stop.

### 2.1 Liquidity gate — replaces the old size band

Because there is no cap floor, liquidity is checked per name and it binds
hardest exactly where it should:

```
max position ($) = 10 trading days × 25% × 20-day median daily dollar volume
```

A name passes only if the intended position fits inside that. If the target
weight exceeds it, cut the weight or pass — never assume you can exit faster
than a quarter of the tape for two weeks. Record ADDV and the implied max
position in the memo's sizing section. On a micro cap this gate is the binding
constraint; on a mega cap it is non-binding and costs one line to confirm.

---

## 3. Quality Bar — the six gates

### 3.0 Classify the business type first

Every name is assigned one of four types before any gate is scored. Record it
in the memo header.

| Type | Covers | Economic shape |
| --- | --- | --- |
| **A · Recurring** | Software, vertical SaaS, tech-enabled services, subscription consumer/healthcare | Contracted revenue, asset-light, gross margin is the unit economics |
| **B · Asset-heavy operating** | Industrials, business services, distribution, consumer goods, healthcare services | Repeat/aftermarket revenue, capital in the ground, ROIC is the unit economics |
| **C · Financial** | Banks, insurers, asset managers, specialty lenders | Balance sheet *is* the business; leverage is the product, not a risk metric |
| **D · Resource & cyclical** | Energy, materials, mining, shipping | Price-taker on a commodity; cost-curve position is the only durable edge |

Rules for the edges:
- A name that plausibly fits two types is tested against the **stricter** of the two.
- For a multi-segment business, every segment above 25% of earnings is scored
  against **its own** type. A conglomerate does not get one blended gate table.

### 3.1 The gates

A name must pass **all six** to earn a full diligence workup. Score each
`PASS / FAIL / UNKNOWN`. `UNKNOWN` is not a pass — it is an open work item.

| # | Gate | A · Recurring | B · Asset-heavy | C · Financial | D · Resource |
| --- | --- | --- | --- | --- | --- |
| 1 | **Revenue durability** | ≥70% recurring or contracted | ≥50% repeat, or aftermarket attach ≥30% of gross profit | Deposit or premium persistence ≥90%; renewal retention disclosed | Reserve life ≥10 yrs, or ≥50% of volume contracted |
| 2 | **Unit economics** | GM ≥50%, stable-to-rising over 3 yrs | GM ≥30% **and** ROIC ≥15% | ROTCE ≥12% averaged over a full cycle; efficiency ratio ≤60% | 2nd cost-curve quartile or better; ROCE ≥ WACC at mid-cycle price |
| 3 | **Earnings quality** | FCF/NI ≥0.8, 3-yr avg | FCF/NI ≥0.8, 3-yr avg | No dependence on reserve releases or realized gains; provisions ≥ through-cycle net charge-offs | FCF/NI ≥0.8 **at mid-cycle price**, not spot |
| 4 | **Balance sheet** | Net debt/EBITDA ≤3.0x | Net debt/EBITDA ≤3.0x | CET1 ≥ requirement +200bps (banks); RBC/BCAR above threshold (insurers); no wholesale-funding reliance | Net debt / **mid-cycle** EBITDA ≤2.0x |
| 5 | **Incentives** | Insider ≥3% or named operator; comp tied to per-share value | Same | Same, and comp **not** tied to asset or loan growth | Same, and comp **not** tied to production volume |
| 6 | **Reinvestment runway** | ≥50% of FCF redeployable at ≥ current ROIC for 3+ yrs | Same | Can grow tangible book value per share ≥10%/yr while holding capital ratios | Reserve or capacity replacement ≥100% at ≤ mid-cycle cost |

Common to all four, and not negotiable by type:
- No maturity wall inside 24 months, and no covenant we cannot model (gate 4).
- Comp tied to "adjusted" anything is a gate 5 failure regardless of type.
- If gate 6 fails, the name is not a compounder. It may still be a
  capital-return story — but then it is underwritten as one, at a FCF yield,
  and it does not get compounder multiples.

---

## 4. Kill Criteria — walk away immediately

These are not weighed against positives. Any one of them ends the work.

### Universal

- Net insider **selling** > $10M in the trailing 6 months with no 10b5-1 plan
  disclosed at adoption.
- Auditor resignation, material weakness unremediated for >2 quarters, or a
  restatement of revenue.
- Serial "one-time" charges: non-GAAP add-backs >15% of GAAP opex in 3 of the
  last 4 quarters.
- Management has missed its own guidance 3+ times in 8 quarters and has not
  changed the guidance framework.
- Related-party transactions material to earnings.
- Share count growing >4%/yr with no corresponding revenue-per-share growth.
- The thesis requires trusting a number we cannot tie to a filing.

### Types A and B

- Customer concentration >25% from one customer with no multi-year contract.

### Type C — Financial

- Reserve releases drive >20% of pre-tax income in any year.
- Loan growth >2× deposit growth, funded wholesale.
- Regulatory consent order, MRA, or enforcement action disclosed.
- Acquisition goodwill >25% of tangible common equity.

### Type D — Resource & cyclical

- Reserve write-down >15% of prior-year stated reserves.
- Production guidance missed two consecutive years.
- Hedge book obscures realized price by >20% of spot.
- Development capex funded by equity issued below NAV.

Log every kill in `research/names/<TICKER>/KILL.md` with the trigger and date.
Kills are an asset — they are why we don't re-do the same work in 18 months.

---

## 5. Valuation Framework

Primary metric by business type — do not default to P/E:

| Type | Primary | Cross-check | Never |
| --- | --- | --- | --- |
| **A · Recurring** | EV / NTM Revenue vs. Rule of 40 | EV/FCF, net revenue retention, LTV:CAC | Never P/E on a loss-maker |
| **B · Asset-heavy** | EV / NTM EBITDA | FCF yield, ROIC vs. WACC, replacement cost | Never EV/EBITDA where maintenance capex >60% of D&A without adjusting |
| **C · Financial** | P / TBV calibrated to the ROTCE it earns | Normalized P/E on through-cycle provisions; dividend and buyback capacity under stress | Never P/E at a credit trough; never P/TBV without the ROTCE that justifies it |
| **D · Resource** | Mid-cycle EV / EBIT | NAV at a stated price deck, replacement value, tangible book | **Never underwrite at spot.** Mid-cycle only, and state the deck |
| **Capital-return story** | FCF yield | Dividend + buyback coverage | Never count buybacks as return of capital while share count rises |

Rules:
- **Never a single point estimate.** Every valuation is a bear / base / bull
  triple with the assumption that drives each stated in one sentence.
- Discount rate: 10% nominal for the base case. For Type C, discount **equity**
  free cash flow (dividend capacity), not enterprise cash flow, and say so.
- For Type D, the commodity price deck is an assumption, not a fact: label it,
  source it, and show the base case at mid-cycle rather than strip.
- Terminal multiple must be **at or below** the trailing 5-year median unless
  we can name the structural change that justifies more.
- Underwrite to a **3-year IRR ≥15%** in the base case, and a bear case that
  loses **<25%**. Asymmetry is the point.
- Multiple expansion is never allowed to be more than 40% of base-case return.
  If it is, we are betting on sentiment, not the business.

---

## 6. Thesis Structure

Every memo, without exception, is written in this order:

1. **One-line thesis** — the business, the mispricing, the catalyst, in a sentence.
2. **Edge** — which of the three edge types, and why we have it.
3. **Business model** — the assigned type, and how a dollar enters and what it
   costs to earn it.
4. **The six gates** — table, scored against the type's column, with
   PASS/FAIL/UNKNOWN and the citation for each.
5. **Variant perception** — what consensus believes, what we believe, and the
   specific disclosure that separates the two.
6. **Valuation** — bear / base / bull, with the one driving assumption each.
7. **Catalyst path** — dated, with what we expect to see and when.
8. **Risks** — ranked by probability × severity, each with a falsifying signal.
9. **Kill criteria for this name** — the universal list plus the type's list,
   plus anything name-specific.
10. **Sizing** — proposed weight, the liquidity ceiling from §2.1, and the
    reasoning that ties the weight to the bear case.

Template: `research/_templates/memo.md`.

---

## 7. Evidence Standard

This is the rule that matters most.

- **Every number is cited** to a filing, transcript, or dataset — with the
  accession number or URL and the period. Format: `[10-Q 2025-Q3, p.14]`.
- **No number from memory.** Not revenue, not margins, not share count, not a
  multiple. If a tool cannot produce it, the memo says `UNVERIFIED` in bold.
- **Prefer primary source.** Filing > transcript > press release > sell-side >
  news. Never invert that order.
- **Non-GAAP is quoted, never adopted.** Every non-GAAP figure appears next to
  its GAAP counterpart with the bridge.
- **Distinguish reported from estimated.** Estimates are labeled `[EST]` with
  the method in a footnote. A mid-cycle price and a normalized provision are
  both estimates and are labeled as such.
- When sources disagree, show both and say which we use and why.

An uncited memo is not a draft. It is discarded.

---

## 8. Output Conventions

- Currency in USD millions unless noted; keep one decimal.
- Fiscal periods labeled `FY25` / `3Q25`; note when fiscal ≠ calendar.
- Growth rates: YoY unless labeled QoQ or sequential.
- Every table gets a source row.
- Write in plain declarative sentences. No hedging adverbs — say the number
  and its uncertainty, not "somewhat" or "fairly".
- Lead with the conclusion. The reader should be able to stop after paragraph one.

---

## 9. Repo Map

| Path | Layer | Purpose |
| --- | --- | --- |
| `CLAUDE.md` | 1 | This file — the diligence brain |
| `.claude/skills/` | 2 | One-command diligence workflows |
| `.mcp.json`, `mcp/` | 3 | Live data pipeline (EDGAR, FRED, fetch) |
| `.claude/agents/` | 4 | Parallel research team |
| `scripts/scenario.sh` | 5 | Worktree scenario lab |
| `research/names/<TICKER>/` | — | All work product for a name |
| `universe/coverage.md` | — | Coverage universe and screen history |

## 10. Working Agreement

- Read this file before starting any task. If a request conflicts with it,
  say so before proceeding.
- Assign the business type (§3.0) before scoring any gate. Applying Type A
  tests to a bank produces a confident wrong answer, which is worse than none.
- Never write to `research/names/<TICKER>/` for a name outside the universe
  without saying it is out of mandate first.
- Never fabricate a filing citation. Missing data is reported as missing.
- This repo produces **research**, not advice and not orders. No output here
  is a recommendation to any third party.
