# Meridian Freeman Capital — Diligence Brain

This file is read before every task. It encodes *how this fund thinks*, so every
output — screen, memo, model, scenario — comes out in the same shape.

> Sections marked **[CALIBRATE]** are the fund's opinions, not defaults. They are
> seeded with a defensible starting position; edit them to match the actual book.

---

## 1. Mandate & Edge

**[CALIBRATE]**

- **Strategy:** fundamental, concentrated long book with opportunistic shorts.
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

**[CALIBRATE]** — maintained in `universe/coverage.md`.

- Market cap: **$300M – $25B** (below $300M the liquidity does not support sizing).
- Geography: US and Canada primary listings. ADRs only with a domestic comp.
- Sectors in scope: software & vertical SaaS, business services, industrials
  with aftermarket revenue, consumer with repeat purchase, healthcare services.
- Sectors out of scope: banks, insurers, biotech (pre-revenue), E&P, shipping,
  crypto-native, pre-revenue anything.

Out-of-scope names are not researched. Say so and stop.

---

## 3. Quality Bar — the six gates

A name must pass **all six** to earn a full diligence workup. Score each
`PASS / FAIL / UNKNOWN`. `UNKNOWN` is not a pass — it is an open work item.

1. **Revenue durability** — ≥70% of revenue is recurring, contracted, or
   demonstrably repeat. Show the disclosure that proves it.
2. **Unit economics** — gross margin ≥50% (software) or ≥30% with ≥15% ROIC
   (non-software), and stable-to-rising over 3 years.
3. **Cash conversion** — FCF / net income ≥0.8 averaged over 3 years.
   Persistent gaps mean the earnings are an accrual story.
4. **Balance sheet** — net debt / EBITDA ≤3.0x, no maturity wall inside 24
   months, no covenant we cannot model.
5. **Incentives** — insider ownership ≥3% or a named founder/operator with
   real skin. Comp tied to per-share value, not revenue or "adjusted" anything.
6. **Reinvestment runway** — management can deploy ≥50% of FCF at or above the
   current ROIC for 3+ years. If not, it is a capital-return story and must be
   underwritten as one.

---

## 4. Kill Criteria — walk away immediately

These are not weighed against positives. Any one of them ends the work.

- Net insider **selling** > $10M in the trailing 6 months with no 10b5-1 plan
  disclosed at adoption.
- Auditor resignation, material weakness unremediated for >2 quarters, or a
  restatement of revenue.
- Serial "one-time" charges: non-GAAP add-backs >15% of GAAP opex in 3 of the
  last 4 quarters.
- Customer concentration >25% from one customer with no multi-year contract.
- Management has missed its own guidance 3+ times in 8 quarters and has not
  changed the guidance framework.
- Related-party transactions material to earnings.
- Share count growing >4%/yr with no corresponding revenue-per-share growth.
- The thesis requires trusting a number we cannot tie to a filing.

Log every kill in `research/names/<TICKER>/KILL.md` with the trigger and date.
Kills are an asset — they are why we don't re-do the same work in 18 months.

---

## 5. Valuation Framework

**[CALIBRATE]**

Primary metric by business type:

| Business type | Primary | Cross-check |
| --- | --- | --- |
| Software / recurring | EV / NTM Revenue vs. Rule of 40 | EV/FCF, LTV:CAC |
| Compounders (non-SW) | EV / NTM EBITDA | FCF yield, ROIC vs. WACC |
| Cyclicals | Mid-cycle EV / EBIT | Replacement value, tangible book |
| Capital-return stories | FCF yield | Dividend + buyback coverage |

Rules:
- **Never a single point estimate.** Every valuation is a bear / base / bull
  triple with the assumption that drives each stated in one sentence.
- Discount rate: 10% nominal for the base case. **[CALIBRATE]**
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
3. **Business model** — how a dollar enters and what it costs to earn it.
4. **The six gates** — table, with PASS/FAIL/UNKNOWN and the citation for each.
5. **Variant perception** — what consensus believes, what we believe, and the
   specific disclosure that separates the two.
6. **Valuation** — bear / base / bull, with the one driving assumption each.
7. **Catalyst path** — dated, with what we expect to see and when.
8. **Risks** — ranked by probability × severity, each with a falsifying signal.
9. **Kill criteria for this name** — the specific things that end the position.
10. **Sizing** — proposed weight and the reasoning that ties it to the bear case.

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
  the method in a footnote.
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
- Never write to `research/names/<TICKER>/` for a name outside the universe
  without saying it is out of mandate first.
- Never fabricate a filing citation. Missing data is reported as missing.
- This repo produces **research**, not advice and not orders. No output here
  is a recommendation to any third party.
