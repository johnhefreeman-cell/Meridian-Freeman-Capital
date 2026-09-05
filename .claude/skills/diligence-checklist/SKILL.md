---
name: diligence-checklist
description: Run the full diligence workup on a ticker by dispatching the parallel research team, then converge results into a memo. Use when the user asks to diligence, research, work up, or fully analyze a name, asks "should we own X", or says "/diligence-checklist".
---

# Diligence Checklist

The full workup. This is the skill that spends real time — it fans out the
Layer 4 research team, then converges the results into a memo in the
CLAUDE.md §6 structure.

## Step 0 — Mandate check

Confirm the name is inside CLAUDE.md §2. If it is out of mandate, say so and
stop. Do not do the work and mention the problem afterward.

## Step 1 — Establish the base facts once

Do this *before* fanning out, so all five agents reason from the same numbers:

- `edgar.company_profile` — CIK, SIC, fiscal year end
- `edgar.list_filings` — last 3 10-Ks, last 4 10-Qs, last DEF 14A
- `market.quote` — price, market cap, EV, current multiples
- 3 years of revenue, gross profit, operating income, OCF, capex, share count
  via `edgar.xbrl_concept`

Write these to `research/names/<TICKER>/00-base-facts.md`. Every agent reads
this file first. This is what stops five agents from producing five different
revenue numbers.

## Step 2 — Fan out the research team

Dispatch all five in **one message** so they run concurrently. Each writes its
own file under `research/names/<TICKER>/`:

| Agent | Writes | Question it answers |
| --- | --- | --- |
| `bull-case` | `10-bull.md` | What has to be true for this to triple? |
| `bear-case` | `11-bear.md` | What is the way we lose 50%? |
| `mgmt-credibility` | `12-management.md` | Have they done what they said, for 3 years? |
| `filing-analyst` | `13-filings.md` | What changed in the language, and who is trading? |
| `revenue-quality` | `14-revenue-quality.md` | Is the revenue real, recurring, and diversified? |

Give each agent: the ticker, the path to `00-base-facts.md`, its output path,
and the instruction to cite every figure.

## Step 3 — Score the six gates

Using the agents' output, fill the CLAUDE.md §3 table. `PASS / FAIL / UNKNOWN`
with a citation for each. **`UNKNOWN` is not `PASS`** — it is an open item that
must be listed as such.

## Step 4 — Run the kill criteria

Every item in CLAUDE.md §4, explicitly, each with the evidence checked. Any
single trip ends the work: write `research/names/<TICKER>/KILL.md` with the
trigger, the evidence, and the date, then report the kill and stop. Do not
soften a kill because the rest of the work was good — that is the entire
purpose of having written them down in advance.

## Step 5 — Converge

Reconcile the bull and bear cases. Where they disagree, the disagreement is
the thesis: name the specific fact that would settle it, and whether it is
knowable before the position is sized.

Write `research/names/<TICKER>/MEMO.md` from `research/_templates/memo.md`,
in the CLAUDE.md §6 order. The memo is the deliverable; the agent files are
its working papers.

## Step 6 — Report

Summarize in the chat: verdict, gate table, the two or three open items, and
the proposed next step (usually `/scenario` for stress-testing, or a kill).

## Do not

- Do not run the agents before Step 1 — inconsistent base facts poison everything.
- Do not write a memo with an unresolved `UNKNOWN` gate without flagging it in
  the first paragraph.
- Do not size a position here. Sizing follows the bear case, and the bear case
  is not stress-tested until `/scenario` runs.
