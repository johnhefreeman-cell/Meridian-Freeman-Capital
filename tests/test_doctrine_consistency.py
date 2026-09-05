"""Guard the calibrated mandate against drift.

The universe is all-cap and all-sector, so the six quality gates are
type-specific (CLAUDE.md §3.0/§3.1). The failure mode this file exists to
catch is a Type A assumption — recurring revenue, gross margin, FCF/NI,
net debt/EBITDA — silently creeping back into a component that is supposed
to branch by type. That regression is invisible until someone runs a bank
through the checklist and gets a confident wrong answer.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MD = (ROOT / "CLAUDE.md").read_text()
TYPES = ("A", "B", "C", "D")

MARKDOWN = sorted(
    p for p in ROOT.rglob("*.md")
    if ".git" not in p.parts and ".venv" not in p.parts
)


def read(rel: str) -> str:
    return (ROOT / rel).read_text()


# ------------------------------------------------- the old mandate is gone

@pytest.mark.parametrize("path", MARKDOWN, ids=lambda p: str(p.relative_to(ROOT)))
def test_no_market_cap_band_survives(path: Path):
    text = path.read_text()
    assert "$300M" not in text, (
        f"{path.relative_to(ROOT)} still encodes the retired $300M-$25B band; "
        "the universe is all-cap and size is handled by the §2.1 liquidity ceiling"
    )


@pytest.mark.parametrize("path", MARKDOWN, ids=lambda p: str(p.relative_to(ROOT)))
def test_no_blanket_sector_exclusion_survives(path: Path):
    text = path.read_text()
    assert "Sectors out of scope" not in text, (
        f"{path.relative_to(ROOT)} still lists excluded sectors; all sectors are "
        "in scope and exclusions are properties of the business"
    )


def test_financials_and_resources_are_in_scope():
    universe = read("universe/coverage.md")
    assert "All sectors and all market caps are in scope" in universe
    # The retired list named these as permanently excluded sectors.
    assert not re.search(r"not re-litigated: banks, insurers", universe)


# ------------------------------------------------------- the type system

def test_claude_md_defines_all_four_business_types():
    for label in ("A · Recurring", "B · Asset-heavy", "C · Financial", "D · Resource"):
        assert label in CLAUDE_MD, f"§3.0 is missing business type {label!r}"


def test_gate_matrix_scores_every_type():
    header = next(
        line for line in CLAUDE_MD.splitlines()
        if line.startswith("| # | Gate |")
    )
    for t in TYPES:
        assert f"{t} ·" in header, f"gate matrix has no column for type {t}"


def test_all_six_gates_are_present_in_the_matrix():
    rows = [l for l in CLAUDE_MD.splitlines() if re.match(r"^\| \d \| \*\*", l)]
    assert len(rows) == 6, f"expected 6 scored gates, found {len(rows)}"


def test_valuation_framework_covers_every_type():
    section = CLAUDE_MD.split("## 5. Valuation Framework")[1].split("## 6.")[0]
    for label in ("A · Recurring", "B · Asset-heavy", "C · Financial", "D · Resource"):
        assert label in section, f"§5 has no primary multiple for {label}"


def test_kill_criteria_have_type_specific_sections():
    section = CLAUDE_MD.split("## 4. Kill Criteria")[1].split("## 5.")[0]
    assert "### Universal" in section
    assert "### Type C" in section, "financials have no type-specific kill criteria"
    assert "### Type D" in section, "resources have no type-specific kill criteria"


# ------------------------------------------------------ the liquidity gate

def test_liquidity_ceiling_replaces_the_size_band():
    assert "max position ($) = 10 trading days × 25% ×" in CLAUDE_MD, (
        "§2.1 liquidity formula missing; nothing constrains size in an all-cap universe"
    )


@pytest.mark.parametrize("rel", [
    ".claude/skills/screen/SKILL.md",
    ".claude/skills/diligence-checklist/SKILL.md",
    "research/_templates/memo.md",
])
def test_components_that_size_positions_apply_the_liquidity_ceiling(rel: str):
    text = read(rel)
    assert "2.1" in text or "liquidity ceiling" in text.lower(), (
        f"{rel} sizes or screens names without referencing the §2.1 liquidity ceiling"
    )


# ------------------------------------ components branch by type, not by default

TYPE_A_ONLY_MARKERS = ("FCF/NI", "recurring", "gross margin", "Net debt/EBITDA",
                       "net debt/EBITDA")

# Vocabulary a component can only be using if it actually handles the type.
# Matching on letters alone is brittle — "types A and B", "**C ·**" and
# "for C;" are all legitimate — and it would pass a file that names a type
# without saying what to do about it.
FINANCIAL_MARKERS = ("ROTCE", "CET1", "charge-off", "reserve release",
                     "reserve build", "reserve-release", "deposit", "loan growth",
                     "AUM", "Type C", "P/TBV", "RBC")
RESOURCE_MARKERS = ("mid-cycle", "cost-curve", "price deck", "reserve life",
                    "production volume", "Type D", "reserves")

# Every component that scores a gate must handle the newly in-scope types.
# Listed explicitly so adding a skill or agent is a deliberate decision.
GATE_SCORING_COMPONENTS = [
    ".claude/skills/screen/SKILL.md",
    ".claude/skills/comps/SKILL.md",
    ".claude/skills/earnings-delta/SKILL.md",
    ".claude/skills/diligence-checklist/SKILL.md",
    ".claude/skills/mgmt-scorecard/SKILL.md",
    ".claude/agents/bear-case.md",
    ".claude/agents/revenue-quality.md",
    "research/_templates/memo.md",
]


@pytest.mark.parametrize("rel", GATE_SCORING_COMPONENTS)
def test_gate_scoring_components_handle_financials(rel: str):
    text = read(rel)
    assert any(m in text for m in FINANCIAL_MARKERS), (
        f"{rel} scores gates but has no Type C (financial) handling. Banks and "
        "insurers are in scope; FCF/NI and net debt/EBITDA are meaningless for them."
    )


@pytest.mark.parametrize("rel", GATE_SCORING_COMPONENTS)
def test_gate_scoring_components_handle_resources(rel: str):
    text = read(rel)
    assert any(m in text for m in RESOURCE_MARKERS), (
        f"{rel} scores gates but has no Type D (resource) handling. Energy and "
        "materials are in scope and must never be underwritten at spot."
    )


@pytest.mark.parametrize("rel", GATE_SCORING_COMPONENTS)
def test_type_a_thresholds_are_never_stated_unconditionally(rel: str):
    """A Type A threshold must appear scoped to a type, not as a global rule."""
    text = read(rel)
    if not any(m in text for m in TYPE_A_ONLY_MARKERS):
        return
    assert re.search(r"\bA / B\b|\*\*A[ ·:]|[Tt]ypes? A\b|\bA ·|for A[;.,]", text), (
        f"{rel} states Type A thresholds without scoping them to a type"
    )


def test_memo_template_records_the_assigned_type():
    memo = read("research/_templates/memo.md")
    assert "**Business type:**" in memo
    assert "Test applied (this type)" in memo, (
        "the gate table must record which test was applied, or the memo is not auditable"
    )
