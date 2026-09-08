# Price sources

Bars live in `data/daily/`, one JSON file per name, rows of
`[epoch, open, high, low, close, adj, volume]` oldest first. Indicators read
`close` — split-adjusted by the provider, not dividend-adjusted. Anything that
writes that shape is a valid source, and nothing downstream knows which one ran.

| Source | Status here | Needs |
| --- | --- | --- |
| **Yahoo** (`scripts/daily_prices.py`) | working, the default | nothing |
| **Twelve Data REST** (`price_source.fetch_twelvedata`) | **blocked** | an API key *and* `api.twelvedata.com` on the network allowlist |
| **Twelve Data import** (`price_source.py --import-csv`) | working today | an assistant with the connector to fetch the CSV |

## Why the REST path is off

`api.twelvedata.com` answers **403 at the proxy** — it is not on this
environment's network allowlist, the same way `sec.gov` was not until it was
added. So the REST client is written against the CSV response this repo has
observed through the connector, and it has **not been exercised end to end**. It
says so rather than failing obscurely: a missing key names the environment
variable, an unreachable host names the allowlist.

**To switch it on, two things:**

1. Add `api.twelvedata.com` to the environment's allowed domains.
2. `export TWELVE_DATA_API_KEY=...` (free tier is enough for daily bars).

Then prove both in one call:

```
uv run python scripts/price_source.py AAPL --selftest
```

## The import path, which works now

The Twelve Data connector is authenticated to the *assistant* through claude.ai
OAuth. A separate Python process cannot borrow that session, so the bridge is a
file:

```
uv run python scripts/price_source.py LLY --import-csv bars.csv --verify   # compare only
uv run python scripts/price_source.py LLY --import-csv bars.csv            # and write
```

`bars.csv` is the provider's `time_series` response verbatim — semicolon
delimited, newest first, `datetime;open;high;low;close;volume`.

## The partial-bar trap

A live provider returns **today's bar while the session is still open**. On
2026-09-08 at mid-morning, Twelve Data's newest AMAT bar read a close of
$465.545 on 20,235 shares against a 6,000,000-share median. Treating that as a
close and computing RSI(14) on it produces a signal that will not exist at 4pm.

Two independent guards, because either alone misses a case:

- **A bar dated today is dropped**, unless `--include-today` is passed — which
  is correct only after the close.
- **A bar whose volume is under 20% of its trailing median is flagged**, because
  that is what an unfinished session looks like. It warns rather than deletes,
  since a half-day holiday looks the same.

## Cross-source agreement, measured

CLAUDE.md §7 says show both sources and say which we use. Both, on the sessions
they share:

| Name | Common sessions | Disagreements beyond 0.1% | Worst |
| --- | ---: | ---: | ---: |
| AMAT | 5 | **0** | 0.000% |
| LLY | 7 | **0** | 0.000% |

And the indicator implementations agree independently: Twelve Data's RSI(14) for
LLY on 2026-09-04 is **41.33058**; this repo returns **41.33058** on the printed
close. That match is why `signals.PRICE_FIELD` is `close` rather than `adj` — on
the dividend-adjusted series the same name reads 41.42706.

**A daily bar is keyed by its date, never its timestamp.** Yahoo stamps a bar at
the market open in UTC, an imported CSV at local midnight. Joining on the epoch
finds zero matches between two sources that agree perfectly — which is exactly
what happened on the first run of the comparison.

## What Twelve Data adds beyond bars

The connector also serves earnings, dividends, splits, analyst estimates,
insider transactions and institutional holdings. None of that is wired in.
Under §7 it is all secondary — quotable, never adoptable in place of a filing —
and EDGAR remains the primary source for anything that reaches a memo.

## Why the key is an environment variable, not plugin config

The plugin's `userConfig` block exists to inject values into **MCP server**
environments, and `tests/test_plugin_manifest.py` enforces that every declared
key is actually consumed by one — it rejected a `twelve_data_api_key` entry on
the first attempt, correctly. Nothing here is an MCP server: the REST client is
a script, and it reads `TWELVE_DATA_API_KEY` from the environment like any other
script would. Declaring it in the manifest would have been a promise no server
keeps.
