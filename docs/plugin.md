# Installing as a plugin

The repo works two ways, and it is worth being precise about the difference
because it is the whole reason this file exists.

| | Project mode | Plugin mode |
| --- | --- | --- |
| How it loads | You open the repo in Claude Code; `.claude/` is read from the working directory | You install it once on your account; it travels with you |
| Available in | Sessions with this repo cloned | Any session — **including Cowork** — no clone required |
| MCP script paths | Relative, resolved against the repo | `${CLAUDE_PLUGIN_ROOT}`, resolved against the install dir |
| Config file | `.mcp.json` | `.claude-plugin/mcp.json` |

Project mode is automatic and needs no setup. Plugin mode is what makes the
skills reachable from Cowork, because a Cowork session assembles its skills and
plugins from your **account**, server-side — it does not clone this repo.

## Install

```
/plugin marketplace add johnhefreeman-cell/Meridian-Freeman-Capital@claude/hello-a9jix6
/plugin install meridian-diligence@meridian-freeman-capital
```

The `@claude/hello-a9jix6` ref is required **until this branch merges to
`main`** — without it Claude Code reads the default branch, which does not yet
contain the plugin. After merging, drop the ref:

```
/plugin marketplace add johnhefreeman-cell/Meridian-Freeman-Capital
/plugin install meridian-diligence@meridian-freeman-capital
```

On install you are prompted for two values, declared as `userConfig` in
`.claude-plugin/plugin.json`:

| Key | Required | Why |
| --- | --- | --- |
| `sec_edgar_user_agent` | yes | SEC blocks or throttles EDGAR requests without real contact information |
| `fred_api_key` | no | Free key, macro server only. Stored as a secret. |

These are injected into the MCP server environments at launch. Neither is ever
written to the repo — `test_no_secret_is_hardcoded_in_either_config` fails the
build if a literal value appears in either MCP config.

## What ships

| Component | Count | Path declared in `plugin.json` |
| --- | --- | --- |
| Skills | 6 | `./.claude/skills/` |
| Agents | 5 | `./.claude/agents/` |
| MCP servers | 4 | `./.claude-plugin/mcp.json` |

The manifest points at the existing `.claude/` directories rather than copying
them into a plugin-standard `skills/` and `agents/` layout. One set of files
serves both modes, so a skill edited in project mode is the same skill the
plugin ships. No sync step, nothing to drift.

## Verify after installing

```
/plugin           # meridian-diligence listed and enabled
/mcp              # edgar, market, fred, fetch — all connected
/screen           # the skill resolves
```

## Known limits

**`uv` must be on PATH.** All three local MCP servers launch via
`uv run --with …`. Where `uv` is unavailable the servers fail to connect while
the skills and agents still load — you get the diligence framework without the
live data pipeline. Whether a Cowork sandbox provides `uv` is not something
this repo can assert; check `/mcp` in a Cowork session and report what you see.
If it is missing, the fallback is to run `/diligence-checklist` from a Claude
Code session on the repo, where `uv` is present.

**Duplicate skills if both modes are active.** Opening the repo as a project
*while* the plugin is installed loads each skill twice. Harmless but noisy;
disable the plugin with `/plugin` when working in the repo directly.

**`fetch` needs network egress.** `uvx mcp-server-fetch` downloads on first
run. In a locked-down sandbox it will fail; the other three servers are
unaffected.

## Changing the plugin

`tests/test_plugin_manifest.py` enforces the invariants that are easy to break
and silent when broken:

- both MCP configs declare the same servers, with identical args once
  `${CLAUDE_PLUGIN_ROOT}` is stripped
- every local script path in the plugin config is anchored to
  `${CLAUDE_PLUGIN_ROOT}` — a relative path here resolves against the *user's*
  project once installed, which fails only for people who installed it
- every `${user_config.*}` reference is declared, and every declared key is used
- every skill and agent has frontmatter whose `name` matches its filename

```bash
uv run --with pytest python -m pytest tests/ -q
```

Bump `version` in `.claude-plugin/plugin.json` when you change what ships.
