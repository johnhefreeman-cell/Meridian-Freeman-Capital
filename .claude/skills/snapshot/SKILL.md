---
name: snapshot
description: Fast fundamental orientation on a ticker — price, multiples, growth, balance sheet and dilution — to decide whether it deserves real work. Use when the user asks for a quick look, a fundamental snapshot, the basic numbers on a name, "is this worth looking at", or says "/snapshot".
---

# Snapshot

Four numbers and a decision: **is this worth an hour?** Not what it is worth —
that is `/comps` and `/diligence-checklist`, and the difference matters.

Budget: two minutes. If it is taking longer, the answer is already "run the
real workup."

## Step 0 — Assign the business type

CLAUDE.md §3.0: A recurring, B asset-heavy, C financial, D resource. One line
of justification. **This decides which multiple is meaningful**, and printing
a forward P/E for a loss-maker or EV/Sales for a bank is worse than printing
nothing.

Where a name fits no type cleanly — fabless semiconductors are the known case —
say so rather than forcing it, and flag it for the doctrine to absorb.

## The four numbers

Pull from `edgar.*` first, `market.*` second, and label which. Where the two
disagree by more than 2%, show both and use the filing (CLAUDE.md §7).

**1 · Where it trades** — price, market cap, EV, 30-day and 12-month move,
distance from the 52-week high.

**2 · What it trades at** — the type's primary multiple from CLAUDE.md §5, not
a default P/E:

| Type | Show | Never show |
| --- | --- | --- |
| A · Recurring | EV/NTM Revenue, Rule of 40 | P/E on a loss-maker |
| B · Asset-heavy | EV/NTM EBITDA, FCF yield | EV/EBITDA where maintenance capex >60% of D&A |
| C · Financial | P/TBV against ROTCE | EV/anything — enterprise value is meaningless where leverage is the product |
| D · Resource | Mid-cycle EV/EBIT | Anything at spot prices |

**3 · What just happened** — last quarter revenue growth and earnings growth,
YoY, GAAP, with the non-GAAP bridge if management leads with adjusted figures.

**4 · Balance sheet and dilution** — cash, total debt, net debt/EBITDA, and
**share count change YoY**. This is the highest-signal line in the whole
snapshot and the one most often skipped.

## Check the two gates that are cheap

Not the full workup — just the two that a snapshot can honestly answer:

- **Kill criterion (CLAUDE.md §4):** share count growing >4%/yr with no
  corresponding revenue-per-share growth. Compute revenue per share both years
  and say whether the dilution bought anything.
- **Gate 4 (CLAUDE.md §3.1):** net debt/EBITDA against the type's threshold —
  3.0x for A and B, 2.0x on **mid-cycle** EBITDA for D, CET1 for C.

Report `PASS / FAIL / UNKNOWN`. `UNKNOWN` where the data was not available.

## Output

```
<TICKER> — <Name> · Type <X> · <date>

Trades          $X · mkt cap $Xm · EV $Xm · 30d ±X% · X% below 52wk high
Multiple        <type's primary> Xx        [EDGAR|MARKET]
Last quarter    revenue +X% YoY · earnings +X% YoY   [EDGAR]
Balance sheet   cash $Xm vs debt $Xm · net debt/EBITDA Xx
Dilution        shares +X% YoY · revenue/share +X%   -> PASS/FAIL

Gate 4          PASS/FAIL/UNKNOWN
Kill (dilution) TRIPPED / clear

Worth an hour?  YES / NO / MAYBE — one sentence why
```

## Do not answer "what is it worth"

The prompt this skill replaces ended with *"is the stock trading above, at, or
below fundamental fair value? Show the math."* **Refuse that**, and say why
rather than silently omitting it:

- CLAUDE.md §5 requires a bear/base/bull triple with the assumption driving
  each. A single fair value is the thing the doctrine explicitly forbids.
- A multiple against a sector average is not a valuation. `/comps` exists
  because a peer set of convenience produces a median of nothing.
- No 3-year IRR and no bear case are derivable from four numbers, and both are
  required before a position is sized.

End with the handoff instead: **"Valuation needs `/comps` for a defended peer
set, then `/diligence-checklist` for the gates."**

## Do not

- Do not report a figure without saying whether it came from a filing or a
  vendor.
- Do not print a multiple the business type does not support.
- Do not treat "cheap versus sector" as a finding. It is an observation, and
  usually a compensated one.
- Do not let a `MAYBE` become a position. A snapshot routes work; it never
  concludes.
