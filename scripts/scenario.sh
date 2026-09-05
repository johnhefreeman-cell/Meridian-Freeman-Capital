#!/usr/bin/env bash
# Layer 5 — Scenario Lab.
#
# Stress-test assumptions in isolated git worktrees so the base case is never
# contaminated by a variant. Each scenario is a branch plus a working directory;
# they exist side by side on disk and can be compared file-by-file.
#
#   scenario.sh new     MSFT bull          create a scenario worktree
#   scenario.sh list    [MSFT]             list scenarios
#   scenario.sh diff    MSFT bull          diff a scenario against the base case
#   scenario.sh compare MSFT               show every scenario's assumptions
#   scenario.sh adopt   MSFT bull          merge a scenario into the base case
#   scenario.sh drop    MSFT bull          discard a scenario

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SCENARIO_HOME="${MFC_SCENARIO_HOME:-$(dirname "$REPO_ROOT")/mfc-scenarios}"
BASE_BRANCH="$(git -C "$REPO_ROOT" symbolic-ref --quiet --short HEAD || echo main)"

die()  { printf 'error: %s\n' "$*" >&2; exit 1; }
info() { printf '  %s\n' "$*"; }

require_ticker() { [ -n "${1:-}" ] || die "ticker required"; }
upper() { printf '%s' "$1" | tr '[:lower:]' '[:upper:]'; }
slug()  { printf '%s' "$1" | tr '[:upper:] ' '[:lower:]-'; }

branch_for() { printf 'scenario/%s/%s' "$1" "$2"; }
path_for()   { printf '%s/%s-%s' "$SCENARIO_HOME" "$1" "$2"; }

seed_assumptions() {
  local dir="$1" ticker="$2" scenario="$3" target
  target="$dir/research/names/$ticker/ASSUMPTIONS.md"
  mkdir -p "$(dirname "$target")"
  [ -e "$target" ] && return 0
  cat > "$target" <<EOF
# $ticker — "$scenario" scenario assumptions

Branch: \`$(branch_for "$ticker" "$scenario")\`
Forked from: \`$BASE_BRANCH\`
Created: $(date -u +%Y-%m-%d)

Change the numbers below, rerun the model, and commit **on this branch only**.
The base case does not move until \`scenario.sh adopt\` is run.

## Deltas from base case

State each change and the *reason* it is plausible. A scenario without a
mechanism is a sensitivity table, not a scenario.

| Assumption | Base | This scenario | Why this is plausible |
| --- | --- | --- | --- |
| Revenue CAGR (3yr) | | | |
| Terminal gross margin | | | |
| Terminal EBITDA margin | | | |
| Exit multiple | | | |
| Discount rate | | | |
| Share count CAGR | | | |
| Reinvestment rate | | | |

## Result

| | Value |
| --- | --- |
| Implied 3-year IRR | |
| Implied price | |
| Return vs. spot | |
| Multiple expansion share of return | |

Per CLAUDE.md §5: base case must clear a 15% 3-year IRR, the bear case must
lose less than 25%, and multiple expansion may not exceed 40% of the return.

## What would make this the base case

The observable event that promotes this scenario. Be specific — a number in a
filing, not a sentiment shift.
EOF
  info "seeded $(realpath --relative-to="$REPO_ROOT" "$target" 2>/dev/null || echo "$target")"
}

cmd_new() {
  local ticker scenario branch dir
  require_ticker "${1:-}"
  ticker="$(upper "$1")"; scenario="$(slug "${2:-variant}")"
  branch="$(branch_for "$ticker" "$scenario")"
  dir="$(path_for "$ticker" "$scenario")"

  [ -e "$dir" ] && die "worktree already exists at $dir"
  mkdir -p "$SCENARIO_HOME"

  if git -C "$REPO_ROOT" show-ref --verify --quiet "refs/heads/$branch"; then
    info "branch $branch exists; attaching worktree to it"
    git -C "$REPO_ROOT" worktree add "$dir" "$branch" >/dev/null
  else
    git -C "$REPO_ROOT" worktree add -b "$branch" "$dir" "$BASE_BRANCH" >/dev/null
  fi

  seed_assumptions "$dir" "$ticker" "$scenario"
  printf '\nscenario ready\n'
  info "branch: $branch"
  info "path:   $dir"
  info "next:   edit ASSUMPTIONS.md, commit on this branch, then 'scenario.sh compare $ticker'"
}

cmd_list() {
  local filter="${1:-}" found=0
  [ -n "$filter" ] && filter="$(upper "$filter")"
  printf 'scenarios (base: %s)\n' "$BASE_BRANCH"
  while IFS= read -r line; do
    case "$line" in
      worktree\ *) wt="${line#worktree }" ;;
      branch\ refs/heads/scenario/*)
        br="${line#branch refs/heads/}"
        rest="${br#scenario/}"; tk="${rest%%/*}"; sc="${rest#*/}"
        if [ -z "$filter" ] || [ "$tk" = "$filter" ]; then
          printf '  %-8s %-14s %s\n' "$tk" "$sc" "$wt"; found=1
        fi ;;
    esac
  done < <(git -C "$REPO_ROOT" worktree list --porcelain)
  [ "$found" -eq 0 ] && info "(none)"
  return 0
}

cmd_diff() {
  local ticker scenario branch
  require_ticker "${1:-}"; [ -n "${2:-}" ] || die "scenario name required"
  ticker="$(upper "$1")"; scenario="$(slug "$2")"
  branch="$(branch_for "$ticker" "$scenario")"
  git -C "$REPO_ROOT" show-ref --verify --quiet "refs/heads/$branch" \
    || die "no scenario '$scenario' for $ticker"
  git -C "$REPO_ROOT" diff --stat "$BASE_BRANCH...$branch" -- "research/names/$ticker"
  printf '\n'
  git -C "$REPO_ROOT" diff "$BASE_BRANCH...$branch" -- "research/names/$ticker"
}

cmd_compare() {
  local ticker branch rest sc
  require_ticker "${1:-}"; ticker="$(upper "$1")"
  printf '=== %s: base case (%s) ===\n\n' "$ticker" "$BASE_BRANCH"
  git -C "$REPO_ROOT" show "$BASE_BRANCH:research/names/$ticker/ASSUMPTIONS.md" \
    2>/dev/null || info "(no base-case ASSUMPTIONS.md)"
  while IFS= read -r branch; do
    rest="${branch#scenario/$ticker/}"; sc="$rest"
    printf '\n=== %s: %s ===\n\n' "$ticker" "$sc"
    git -C "$REPO_ROOT" show "$branch:research/names/$ticker/ASSUMPTIONS.md" \
      2>/dev/null || info "(not committed on this branch yet)"
  done < <(git -C "$REPO_ROOT" for-each-ref --format='%(refname:short)' \
             "refs/heads/scenario/$ticker/")
}

cmd_adopt() {
  local ticker scenario branch
  require_ticker "${1:-}"; [ -n "${2:-}" ] || die "scenario name required"
  ticker="$(upper "$1")"; scenario="$(slug "$2")"
  branch="$(branch_for "$ticker" "$scenario")"
  git -C "$REPO_ROOT" show-ref --verify --quiet "refs/heads/$branch" \
    || die "no scenario '$scenario' for $ticker"
  git -C "$REPO_ROOT" diff --quiet && git -C "$REPO_ROOT" diff --cached --quiet \
    || die "base case has uncommitted changes; commit or stash first"
  info "merging $branch into $BASE_BRANCH"
  git -C "$REPO_ROOT" merge --no-ff "$branch" \
    -m "Adopt $ticker '$scenario' scenario as base case"
  printf '\nadopted. drop the worktree with: scripts/scenario.sh drop %s %s\n' \
    "$ticker" "$scenario"
}

cmd_drop() {
  local ticker scenario branch dir
  require_ticker "${1:-}"; [ -n "${2:-}" ] || die "scenario name required"
  ticker="$(upper "$1")"; scenario="$(slug "$2")"
  branch="$(branch_for "$ticker" "$scenario")"
  dir="$(path_for "$ticker" "$scenario")"
  [ -e "$dir" ] && git -C "$REPO_ROOT" worktree remove --force "$dir"
  git -C "$REPO_ROOT" branch -D "$branch" 2>/dev/null || true
  git -C "$REPO_ROOT" worktree prune
  info "dropped $branch"
}

usage() { sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'; }

case "${1:-help}" in
  new)     shift; cmd_new "$@" ;;
  list|ls) shift; cmd_list "$@" ;;
  diff)    shift; cmd_diff "$@" ;;
  compare) shift; cmd_compare "$@" ;;
  adopt)   shift; cmd_adopt "$@" ;;
  drop|rm) shift; cmd_drop "$@" ;;
  help|-h|--help) usage ;;
  *) usage; exit 1 ;;
esac
