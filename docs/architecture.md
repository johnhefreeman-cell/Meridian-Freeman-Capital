# Architecture

Five layers. The point of the separation is that each one changes at a
different rate: the brain rarely, the workflows occasionally, the data
pipeline when a source breaks, the agents per workup, the worktrees per idea.

```
                    ┌──────────────────┐
                    │    CLAUDE.md     │  Layer 1
                    │  diligence brain │  mandate · gates · kills · evidence
                    └────────┬─────────┘
                             │ read before every task
                    ┌────────▼─────────┐
                    │      Skills      │  Layer 2
                    │    workflows     │  /screen /comps /diligence-checklist …
                    └───┬──────────┬───┘
              calls     │          │     dispatches
          ┌─────────────▼──┐    ┌──▼──────────────┐
          │  MCP Servers   │    │   Sub-Agents    │
          │  Layer 3       │◄───┤   Layer 4       │
          │  edgar market  │    │  bull bear mgmt │
          │  fred  fetch   │    │  filings revqual│
          └────────────────┘    └──┬──────────────┘
                                   │ converge
                          ┌────────▼─────────┐
                          │    Worktrees     │  Layer 5
                          │  scenario lab    │  bear · base · bull
                          └──────────────────┘
```

## Layer 1 — CLAUDE.md

Read before every task. It answers the questions that would otherwise be
re-litigated in every session: what we own, what we refuse to own, what makes
a business good, what ends the work, how we value, how we cite.

The two sections that carry the weight are **§3 the six gates** and **§4 the
kill criteria**. Gates are how a name earns attention; kills are how it loses
it regardless of how attractive the rest looks. Writing kills down *in advance*
is the whole mechanism — it is what makes them survive the moment you are
attached to a name.

**§7 the evidence standard** is what makes the output trustworthy: every number
cited to a filing, nothing from memory, primary sources over secondary. Without
it a language model will produce a confident, well-formatted, fabricated memo.

## Layer 2 — Skills

A skill is a workflow written once and invoked by name forever. Each names its
tools, its procedure, its output shape, and — importantly — its **Do not** list.

Skills call MCP tools and dispatch sub-agents. That is the layering: a skill is
the recipe, Layer 3 is the ingredients, Layer 4 is the extra hands.

`/diligence-checklist` is the composite: it orchestrates all five agents and
converges them into one memo.

## Layer 3 — MCP Servers

Live data, no copy-paste. Four servers:

- **`edgar`** — SEC's public JSON APIs. Ticker→CIK, filing history with direct
  document URLs, XBRL concept time series (each point carrying its accession
  number so figures are citable), Form 3/4/5 insider filings, and full-text
  search across filings since 2001. Throttled to SEC's fair-access policy;
  sends the `SEC_EDGAR_USER_AGENT` SEC requires.
- **`market`** — yfinance. Multiples, price history, consensus, standardized
  statements. Explicitly secondary: use it for the comp table and for consensus
  (which has no filing equivalent), then verify against EDGAR.
- **`fred`** — macro series for cycle context on cyclicals. Not a thesis driver.
- **`fetch`** — the official reference fetch server, for IR pages and releases.

Servers are launched by `uv run --with …`, so there is no virtualenv to manage
and no dependency on a third-party MCP package whose maintenance you do not
control.

## Layer 4 — Sub-Agents

Five agents, one name, run concurrently in isolated contexts. They exist for
two reasons, and the second matters more:

1. **Speed** — five workstreams in the wall-clock time of one.
2. **Independence** — the bull agent cannot see the bear agent's work. Neither
   anchors on the other. When they converge and disagree, the disagreement is
   located precisely, and *that disagreement is the thesis*.

The `/diligence-checklist` skill establishes base facts **before** fanning out,
and every agent reads that file first. Skipping this produces five agents with
five different revenue numbers and a memo that reconciles none of them.

## Layer 5 — Worktrees

A git worktree is a second working directory on a second branch, sharing one
repository. That makes it a natural scenario lab: model the bear case in a
worktree and the base case never moves.

```bash
scripts/scenario.sh new     NVDA bear
scripts/scenario.sh new     NVDA bull
scripts/scenario.sh compare NVDA       # assumptions side by side
scripts/scenario.sh diff    NVDA bear  # what this scenario changed
scripts/scenario.sh adopt   NVDA bear  # merge it into the base case
scripts/scenario.sh drop    NVDA bull
```

Branches are `scenario/<TICKER>/<name>`; directories default to
`../mfc-scenarios/<TICKER>-<name>` (override with `MFC_SCENARIO_HOME`). Each
new scenario is seeded with an `ASSUMPTIONS.md` that forces the delta table and
a stated mechanism — a scenario without a mechanism is a sensitivity table.

## Where the work lands

```
research/names/<TICKER>/
├── 00-base-facts.md        established once, read by every agent
├── 10-bull.md              bull-case agent
├── 11-bear.md              bear-case agent
├── 12-management.md        mgmt-credibility agent
├── 13-filings.md           filing-analyst agent
├── 14-revenue-quality.md   revenue-quality agent
├── ASSUMPTIONS.md          per-scenario, on scenario branches
├── MEMO.md                 the deliverable
└── KILL.md                 if killed: trigger, evidence, date
```

The agent files are working papers. `MEMO.md` is the deliverable, and its
structure is fixed by CLAUDE.md §6 so that two memos written a year apart are
still comparable.
