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

Two ways to load it. **Project mode** — clone and open in Claude Code:

```bash
uv sync                       # or: pip install -e .
cp .env.example .env          # then fill in SEC_EDGAR_USER_AGENT (required)
```

**Plugin mode** — install once on your account so the skills and agents reach
every session, Cowork included, with no clone:

```
/plugin marketplace add johnhefreeman-cell/Meridian-Freeman-Capital@claude/hello-a9jix6
/plugin install meridian-diligence@meridian-freeman-capital
```

You are prompted for `sec_edgar_user_agent` on install; the FRED key is
optional. See [docs/plugin.md](docs/plugin.md) for the difference between the
two modes and the known limits.

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
.claude-plugin/               plugin + marketplace manifests
tests/                        offline tests for the MCP servers
```

## The mandate

Calibrated, not seeded — `CLAUDE.md` encodes the actual book:

- **Quality compounders**, concentrated long, 12–18 names, 2–4 year holds.
- **All caps, all sectors.** There is no market-cap band and no sector
  exclusion list. Exclusions are properties of the business — no earnings power
  yet, or economics that cannot be tied to filings.
- **15% 3-year IRR** in the base case, bear case losing under 25%.

Because the universe spans banks and miners as well as software, the six
quality gates are **type-specific**. Every name is classified A (recurring),
B (asset-heavy), C (financial) or D (resource) before any gate is scored, and
the type selects the gate thresholds, the valuation metric, and the extra kill
criteria. Scoring a bank on gross margin or a miner on recurring revenue is not
conservative — it is meaningless, and it throws away good names for bad reasons.

Size discipline comes from a **per-name liquidity ceiling** rather than a cap
floor: `10 trading days × 25% × 20-day median dollar volume`. A $120M name is
not excluded for being small; it is excluded when the position you want does
not fit in the tape.

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
