"""Validate the plugin manifests and keep the two MCP configs in sync.

The repo is both a Claude Code project and a plugin. That means two MCP
configs that must stay identical except for how the server script path
resolves:

  .mcp.json                 project mode  -> mcp/edgar_server.py
  .claude-plugin/mcp.json   plugin mode   -> ${CLAUDE_PLUGIN_ROOT}/mcp/edgar_server.py

Nothing enforces that at runtime, and a server added to one and not the
other fails silently in the surface you did not test. These tests enforce it.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT_VAR = "${CLAUDE_PLUGIN_ROOT}"


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text())


@pytest.fixture(scope="module")
def plugin() -> dict:
    return load(".claude-plugin/plugin.json")


@pytest.fixture(scope="module")
def marketplace() -> dict:
    return load(".claude-plugin/marketplace.json")


@pytest.fixture(scope="module")
def plugin_mcp() -> dict:
    return load(".claude-plugin/mcp.json")


@pytest.fixture(scope="module")
def project_mcp() -> dict:
    return load(".mcp.json")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert m, f"{path.relative_to(ROOT)} has no YAML frontmatter"
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip()
    return out


# ---------------------------------------------------------------- plugin.json

def test_plugin_name_is_kebab_case(plugin):
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", plugin["name"]), plugin["name"]


def test_declared_component_paths_exist(plugin):
    for field in ("skills", "agents"):
        target = ROOT / plugin[field].removeprefix("./")
        assert target.is_dir(), f"plugin.json {field} -> missing dir {target}"


def test_declared_mcp_config_exists(plugin):
    assert (ROOT / plugin["mcpServers"].removeprefix("./")).is_file()


def test_every_skill_is_loadable(plugin):
    skills_dir = ROOT / plugin["skills"].removeprefix("./")
    found = sorted(p.parent.name for p in skills_dir.glob("*/SKILL.md"))
    assert found, "plugin declares a skills dir with no SKILL.md in it"
    for name in found:
        fm = frontmatter(skills_dir / name / "SKILL.md")
        assert fm.get("name") == name, f"{name}: frontmatter name must match dir"
        assert len(fm.get("description", "")) > 40, f"{name}: description too thin to trigger on"


def test_every_agent_is_loadable(plugin):
    agents_dir = ROOT / plugin["agents"].removeprefix("./")
    files = sorted(agents_dir.glob("*.md"))
    assert files, "plugin declares an agents dir with no agent files"
    for path in files:
        fm = frontmatter(path)
        assert fm.get("name") == path.stem, f"{path.name}: frontmatter name must match filename"
        assert fm.get("description"), f"{path.name}: missing description"


# ----------------------------------------------------------- marketplace.json

def test_marketplace_required_fields(marketplace):
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", marketplace["name"])
    assert marketplace["owner"]["name"]
    assert marketplace["plugins"]


RESERVED = {
    "claude-code-marketplace", "claude-code-plugins", "claude-plugins-official",
    "claude-plugins-community", "claude-community", "anthropic-marketplace",
    "anthropic-plugins", "agent-skills", "anthropic-agent-skills",
    "knowledge-work-plugins", "life-sciences", "claude-for-legal",
    "claude-for-financial-services", "financial-services-plugins",
    "first-party-plugins", "healthcare",
}


def test_marketplace_name_is_not_reserved(marketplace):
    assert marketplace["name"] not in RESERVED


def test_relative_plugin_sources_start_with_dot_slash(marketplace):
    for entry in marketplace["plugins"]:
        src = entry["source"]
        if isinstance(src, str):
            assert src.startswith("./"), f"{entry['name']}: relative source must start with ./"
            assert ".." not in src, f"{entry['name']}: source may not escape marketplace root"


def test_marketplace_entry_matches_plugin_manifest(marketplace, plugin):
    names = [p["name"] for p in marketplace["plugins"]]
    assert plugin["name"] in names, (
        "plugin.json name is not listed in marketplace.json; /plugin install would not find it"
    )


# ------------------------------------------------- the two MCP configs agree

def strip_plugin_root(args: list[str]) -> list[str]:
    return [a.replace(PLUGIN_ROOT_VAR + "/", "") for a in args]


def test_both_configs_declare_the_same_servers(plugin_mcp, project_mcp):
    assert set(plugin_mcp["mcpServers"]) == set(project_mcp["mcpServers"]), (
        "a server exists in one MCP config but not the other"
    )


def test_server_args_match_once_plugin_root_is_stripped(plugin_mcp, project_mcp):
    for name, pcfg in plugin_mcp["mcpServers"].items():
        jcfg = project_mcp["mcpServers"][name]
        assert pcfg["command"] == jcfg["command"], f"{name}: command differs"
        assert strip_plugin_root(pcfg["args"]) == jcfg["args"], (
            f"{name}: args differ beyond the CLAUDE_PLUGIN_ROOT prefix"
        )


def test_plugin_config_anchors_local_scripts_to_plugin_root(plugin_mcp):
    for name, cfg in plugin_mcp["mcpServers"].items():
        local = [a for a in cfg["args"] if a.endswith(".py")]
        for arg in local:
            assert arg.startswith(PLUGIN_ROOT_VAR + "/"), (
                f"{name}: {arg} is relative; it would resolve against the user's "
                "project, not the plugin, once installed"
            )


def test_referenced_server_scripts_exist(plugin_mcp):
    for name, cfg in plugin_mcp["mcpServers"].items():
        for arg in cfg["args"]:
            if arg.endswith(".py"):
                rel = arg.replace(PLUGIN_ROOT_VAR + "/", "")
                assert (ROOT / rel).is_file(), f"{name}: missing {rel}"


# ------------------------------------------------------ userConfig wiring

USER_CONFIG_RE = re.compile(r"\$\{user_config\.([a-zA-Z0-9_]+)\}")


def referenced_user_config_keys(cfg: dict) -> set[str]:
    return set(USER_CONFIG_RE.findall(json.dumps(cfg)))


def test_every_referenced_user_config_key_is_declared(plugin, plugin_mcp):
    declared = set(plugin.get("userConfig", {}))
    referenced = referenced_user_config_keys(plugin_mcp)
    missing = referenced - declared
    assert not missing, f"mcp.json references undeclared userConfig keys: {sorted(missing)}"


def test_every_declared_user_config_key_is_used(plugin, plugin_mcp):
    declared = set(plugin.get("userConfig", {}))
    unused = declared - referenced_user_config_keys(plugin_mcp)
    assert not unused, f"userConfig declares keys nothing consumes: {sorted(unused)}"


def test_user_config_options_have_required_metadata(plugin):
    for key, opt in plugin.get("userConfig", {}).items():
        assert opt.get("type"), f"{key}: missing type"
        assert opt.get("title"), f"{key}: missing title"
        assert opt.get("description"), f"{key}: missing description"


def test_secrets_are_marked_sensitive(plugin):
    for key, opt in plugin.get("userConfig", {}).items():
        if re.search(r"key|token|secret|password", key):
            assert opt.get("sensitive") is True, f"{key} looks like a secret but is not sensitive"


def test_no_secret_is_hardcoded_in_either_config(plugin_mcp, project_mcp):
    for cfg in (plugin_mcp, project_mcp):
        env_values = [
            v for s in cfg["mcpServers"].values() for v in (s.get("env") or {}).values()
        ]
        for v in env_values:
            assert "${" in v, f"hardcoded env value in an MCP config: {v!r}"


# ------------------------------------------------ install docs stay in step

def test_install_commands_agree_across_docs():
    """README and docs/plugin.md both document the install; they must match."""
    import re
    readme = (ROOT / "README.md").read_text()
    guide = (ROOT / "docs" / "plugin.md").read_text()
    pattern = re.compile(r"^/plugin (?:marketplace add|install) \S+", re.MULTILINE)
    assert set(pattern.findall(readme)) <= set(pattern.findall(guide)), (
        "README documents an install command docs/plugin.md does not"
    )


def test_documented_install_matches_the_manifest_names():
    guide = (ROOT / "docs" / "plugin.md").read_text()
    plugin = load(".claude-plugin/plugin.json")
    market = load(".claude-plugin/marketplace.json")
    expected = f"/plugin install {plugin['name']}@{market['name']}"
    assert expected in guide, f"docs do not document the real install: {expected}"
