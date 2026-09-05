# Meridian Freeman Capital

A diligence workspace built on Claude Code. Five layers, each doing one job:
the fund's judgment lives in `CLAUDE.md`, the workflows in skills, the data in
MCP servers, the parallelism in sub-agents, and the what-ifs in worktrees.

```
CLAUDE.md ──► Skills ──┬──► MCP Servers ──┐
"the brain"  "workflows"│   "data pipeline" ├──► Worktrees
                        └──► Sub-Agents ────┘   "scenario lab"
                            "research team"
```

| Layer | Where | What it does |
| --- | --- | --- |
| 1 · Brain | `CLAUDE.md` | Mandate, quality gates, kill criteria, valuation framework, evidence standard. Read before every task. |
| 2 · Workflows | `.claude/skills/` | `/screen` `/comps` `/earnings-delta` `/filing-diff` `/mgmt-scorecard` `/diligence-checklist` |
| 3 · Data | `.mcp.json`, `mcp/` | EDGAR, market data, FRED, generic fetch — live, no copy-paste |
| 4 · Research team | `.claude/agents/` | Five agents run in parallel on one name, converge into one memo |
| 5 · Scenario lab | `scripts/scenario.sh` | Bear/base/bull modeled in isolated worktrees, compared side by side |

## Setup

```bash
uv sync                       # or: pip install -e .
cp .env.example .env          # then fill in SEC_EDGAR_USER_AGENT (required)
```

`SEC_EDGAR_USER_AGENT` must contain real contact information — SEC blocks
requests without it. `FRED_API_KEY` is optional and free.

Verify the pipeline from inside Claude Code with `/mcp`; all four servers
should report connected.

```bash
uv run --with pytest python -m pytest tests/ -q
```

## Use it

```
/screen software, >20% growth, >70% gross margin, net cash
/diligence-checklist NVDA
/comps NVDA,AMD,AVGO,MRVL
/earnings-delta NVDA
/filing-diff NVDA
/mgmt-scorecard NVDA
```

`/diligence-checklist` is the deep one: it establishes base facts once, fans
out all five agents concurrently, scores the six gates, runs the kill criteria,
and writes `research/names/<TICKER>/MEMO.md`.

Then stress it:

```bash
scripts/scenario.sh new     NVDA bear     # isolated worktree + branch
scripts/scenario.sh new     NVDA bull
scripts/scenario.sh compare NVDA          # all scenarios side by side
scripts/scenario.sh adopt   NVDA bear     # merge the winner into the base case
```

## Layout

```
CLAUDE.md                     Layer 1 — the diligence brain
.claude/skills/*/SKILL.md     Layer 2 — one-command workflows
.mcp.json  mcp/*.py           Layer 3 — data pipeline
.claude/agents/*.md           Layer 4 — parallel research team
scripts/scenario.sh           Layer 5 — worktree scenario lab
research/names/<TICKER>/      all work product for a name
research/_templates/memo.md   the fixed memo structure
universe/coverage.md          coverage, kills, screen history
docs/architecture.md          how the layers fit together
tests/                        offline tests for the MCP servers
```

## Calibrate before real use

`CLAUDE.md` ships with a defensible starting position, not the fund's actual
one. Sections marked **[CALIBRATE]** — mandate, universe, valuation framework —
encode opinions you should replace with your own. The gates and kill criteria
in §3 and §4 are the ones that will actually stop you from losing money; edit
them deliberately.

## Data sources

| Server | Source | Key | Notes |
| --- | --- | --- | --- |
| `edgar` | SEC EDGAR public JSON APIs | none | Primary source. Rate-limited to SEC's fair-access policy. |
| `market` | yfinance | none | **Secondary.** Multiples and consensus only; verify fundamentals against EDGAR. |
| `fred` | St. Louis Fed | free | Macro context. This fund does not underwrite macro theses. |
| `fetch` | `mcp-server-fetch` | none | Investor relations pages, press releases. |

The evidence standard in CLAUDE.md §7 is the rule that makes the rest work:
every number is cited to a filing, no number comes from memory, and primary
sources outrank everything else.

---

*Internal research tooling. Nothing produced here is investment advice or a
recommendation to any third party.*
