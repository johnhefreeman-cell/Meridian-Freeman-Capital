"""Tests for dip detection and the order it produces.

Two behaviours carry real money here and are pinned hardest: a dip on a name
the framework has killed must come out BLOCKED rather than READY, and the limit
must be the signal bar's own close and nothing else.
"""

import datetime as dt
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import daily_prices as dp  # noqa: E402
import orders as od  # noqa: E402
import signals as sg  # noqa: E402


def bars(closes, volume=1_000_000, start=dt.datetime(2024, 1, 2)):
    """Cache-shaped full bars from a list of closes."""
    rows = []
    for i, c in enumerate(closes):
        stamp = int((start + dt.timedelta(days=i)).timestamp())
        c = float(c)
        rows.append([stamp, c, c * 1.01, c * 0.99, c, c, volume])
    return dict(ticker="TEST", symbol="TEST", rows=rows)


def uptrend_with_pullback(n=260, drop=0.10, tail=15):
    vals = [100.0 * (1.004 ** i) for i in range(n)]
    peak = vals[-1]
    vals += [peak * (1 - drop * k / tail) for k in range(1, tail + 1)]
    return vals


# --------------------------------------------------------------------------
# dips
# --------------------------------------------------------------------------

def test_a_dip_is_a_bar_not_a_state():
    found = sg.dips(bars(uptrend_with_pullback()))
    assert found
    for d in found:
        assert d["close"] > d["sma"]
        assert d["rsi"] < sg.RSI_BUY_BELOW


def test_dips_are_returned_in_order_with_their_index():
    found = sg.dips(bars(uptrend_with_pullback()))
    assert [d["index"] for d in found] == sorted(d["index"] for d in found)


def test_first_of_run_marks_only_the_opening_bar_of_a_pullback():
    """Later bars in one run are the same pullback restating itself."""
    found = sg.dips(bars(uptrend_with_pullback()))
    firsts = [d for d in found if d["first_of_run"]]
    assert len(firsts) >= 1
    assert firsts[0]["index"] == found[0]["index"]
    consecutive = [d for d in found[1:]
                   if d["index"] == found[found.index(d) - 1]["index"] + 1]
    for d in consecutive:
        assert d["first_of_run"] is False


def test_no_dips_in_a_steady_uptrend():
    assert sg.dips(bars([100.0 * (1.004 ** i) for i in range(260)])) == []


def test_no_dips_when_oversold_below_the_average():
    assert sg.dips(bars([200.0 - i * 0.4 for i in range(280)])) == []


def test_no_dips_before_the_average_exists():
    assert sg.dips(bars([100.0] * 150)) == []


# --------------------------------------------------------------------------
# The limit price
# --------------------------------------------------------------------------

def test_the_limit_is_the_signal_bars_closing_price():
    s = bars(uptrend_with_pullback())
    dip = sg.dips(s)[-1]
    order = od.build_order("TEST", s, dip)
    assert order["limit"] == pytest.approx(round(dip["close"], 2))
    assert order["limit_basis"] == "closing price of the signal bar"


def test_the_limit_is_not_the_latest_close_when_the_dip_is_older():
    s = bars(uptrend_with_pullback())
    first = sg.dips(s)[0]
    order = od.build_order("TEST", s, first)
    latest_close = dp.column(s, "close")[-1]
    assert order["limit"] == pytest.approx(round(first["close"], 2))
    assert order["limit"] != pytest.approx(round(latest_close, 2))


def test_the_order_is_a_day_limit_working_from_the_next_session():
    """The close has already happened when the signal is known."""
    s = bars(uptrend_with_pullback())
    order = od.build_order("TEST", s, sg.dips(s)[-1])
    assert order["order_type"] == "LIMIT"
    assert order["side"] == "BUY"
    assert order["time_in_force"] == "DAY"
    assert order["working_from"] == "the next session"


def test_quantity_is_unset_rather_than_invented():
    s = bars(uptrend_with_pullback())
    order = od.build_order("TEST", s, sg.dips(s)[-1])
    assert order["quantity"] == "UNSET"
    assert "sizing" in order["quantity_note"]


def test_the_default_fallback_is_to_chase_the_open():
    s = bars(uptrend_with_pullback())
    assert od.build_order("TEST", s, sg.dips(s)[-1])["fallback"] == od.FALLBACK_CHASE


# --------------------------------------------------------------------------
# Blocking on diligence — the one that must not regress
# --------------------------------------------------------------------------

def test_a_killed_name_is_blocked_not_ready(tmp_path):
    folder = tmp_path / "ZZZ"
    folder.mkdir()
    (folder / "KILL.md").write_text(
        "# ZZZ — KILLED\n\n**Trigger:** CLAUDE.md §4, insider selling\n")
    reason = od.diligence_block("ZZZ", root=tmp_path)
    assert reason is not None
    assert "KILLED" in reason
    assert "insider selling" in reason


def test_a_failed_verdict_also_blocks(tmp_path):
    folder = tmp_path / "YYY"
    folder.mkdir()
    (folder / "20-verdict.md").write_text(
        "# YYY\n\n**Outcome:** fails gates 1, 5 and 6\n")
    reason = od.diligence_block("YYY", root=tmp_path)
    assert reason is not None
    assert "FAILED VERDICT" in reason


def test_a_name_with_research_but_no_verdict_is_not_blocked(tmp_path):
    folder = tmp_path / "WWW"
    folder.mkdir()
    (folder / "10-bull.md").write_text("# bull case\n")
    assert od.diligence_block("WWW", root=tmp_path) is None


def test_a_name_with_no_research_at_all_is_not_blocked(tmp_path):
    assert od.diligence_block("NOPE", root=tmp_path) is None


def test_blocking_survives_the_hyphen_used_by_the_price_source(tmp_path):
    """The price feed spells it BRK-B; the research folder is BRK.B."""
    folder = tmp_path / "BRK.B"
    folder.mkdir()
    (folder / "KILL.md").write_text("# BRK.B\n\n**Trigger:** test\n")
    assert od.diligence_block("BRK-B", root=tmp_path) is not None


def test_build_order_marks_status_from_the_block(tmp_path):
    s = bars(uptrend_with_pullback())
    dip = sg.dips(s)[-1]
    folder = tmp_path / "TEST"
    folder.mkdir()
    (folder / "KILL.md").write_text("# TEST\n\n**Trigger:** whatever\n")
    assert od.build_order("TEST", s, dip, research_root=tmp_path)["status"] == "BLOCKED"
    assert od.build_order("TEST", s, dip, research_root=tmp_path / "empty")["status"] == "READY"


def test_the_research_root_resolves_at_call_time_not_import_time(tmp_path):
    """A default bound to RESEARCH_DIR would freeze the location at import."""
    folder = tmp_path / "TEST"
    folder.mkdir()
    (folder / "KILL.md").write_text("# TEST\n\n**Trigger:** whatever\n")
    original = od.RESEARCH_DIR
    try:
        od.RESEARCH_DIR = tmp_path
        assert od.diligence_block("TEST") is not None
    finally:
        od.RESEARCH_DIR = original


# --------------------------------------------------------------------------
# §2.1 liquidity ceiling
# --------------------------------------------------------------------------

def test_liquidity_ceiling_is_ten_days_of_a_quarter_of_the_tape():
    s = bars([100.0] * 260, volume=1_000_000)
    # median daily dollar volume = 100 * 1,000,000
    assert od.liquidity_ceiling(s) == pytest.approx(10 * 0.25 * 100_000_000)


def test_liquidity_ceiling_uses_the_printed_close_not_the_adjusted_one():
    """§2.1 asks what the tape traded; an adjusted price understates it."""
    rows = [[int(dt.datetime(2024, 1, 2).timestamp()) + i * 86400,
             100.0, 101.0, 99.0, 100.0, 50.0, 1_000_000] for i in range(25)]
    got = od.liquidity_ceiling(dict(rows=rows))
    assert got == pytest.approx(10 * 0.25 * 100_000_000)


def test_liquidity_ceiling_is_none_without_a_full_window():
    assert od.liquidity_ceiling(bars([100.0] * 5)) is None


def test_ceiling_constants_match_the_doctrine():
    assert od.LIQUIDITY_DAYS == 10
    assert od.LIQUIDITY_SHARE == 0.25
    assert od.LIQUIDITY_WINDOW == 20


# --------------------------------------------------------------------------
# Fragility flag and output
# --------------------------------------------------------------------------

def test_a_signal_sitting_on_a_threshold_is_flagged_fragile():
    s = bars(uptrend_with_pullback())
    dip = sg.dips(s)[-1]
    dip = {**dip, "rsi": sg.RSI_BUY_BELOW - 0.2}
    assert od.build_order("TEST", s, dip)["fragile"] is True


def test_a_signal_clear_of_both_thresholds_is_not_flagged():
    s = bars(uptrend_with_pullback())
    dip = {**sg.dips(s)[-1], "rsi": 20.0, "distance": 0.35}
    assert od.build_order("TEST", s, dip)["fragile"] is False


def test_csv_rows_carry_the_block_reason_so_it_cannot_be_lost_in_export(tmp_path):
    s = bars(uptrend_with_pullback())
    order = od.build_order("TEST", s, sg.dips(s)[-1])
    order["status"], order["blocked_reason"] = "BLOCKED", "KILLED — reason here"
    row = od.as_csv_rows([order])[0]
    assert row["status"] == "BLOCKED"
    assert "KILLED" in row["blocked_reason"]
    assert row["quantity"] == "UNSET"


def test_write_files_emits_both_formats(tmp_path):
    s = bars(uptrend_with_pullback())
    order = od.build_order("TEST", s, sg.dips(s)[-1])
    written = od.write_files([order], str(tmp_path), dt.date(2026, 9, 4))
    assert len(written) == 2
    payload = json.load(open(tmp_path / "2026-09-04.json"))
    assert payload[0]["ticker"] == "TEST"
    assert payload[0]["signal_date"] == order["signal_date"].isoformat()


def test_render_says_so_when_nothing_fires():
    assert "Nothing to place" in od.render([], ["AAPL"], [], dt.date(2026, 9, 4))
