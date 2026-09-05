"""Tests for the 200-day SMA strength tag.

Built on synthetic series rather than the workbook, so the behaviour is pinned
independently of any one price history. The cases that matter are the boundary
(what happens exactly at the average), the near-line flag (which is the whole
mitigation for using weekly data to approximate a daily average), and the
run-length counter (which is what separates a name one week past a crossover
from one that has held its side for a year).
"""

import datetime as dt
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import trend_state as ts  # noqa: E402


def series(prices, start=dt.date(2024, 1, 5)):
    """Weekly series from a list of closes, oldest first."""
    return {start + dt.timedelta(weeks=i): float(p) for i, p in enumerate(prices)}


def flat_then(level, weeks, tail):
    return [level] * weeks + list(tail)


# --------------------------------------------------------------------------
# The window is the rule, not a parameter
# --------------------------------------------------------------------------

def test_forty_weeks_is_the_two_hundred_day_equivalent():
    assert ts.SMA_WEEKS * 5 == ts.TRADING_DAYS


# --------------------------------------------------------------------------
# sma
# --------------------------------------------------------------------------

def test_sma_is_none_before_the_window_fills():
    closes = [10.0] * 39
    assert ts.sma(closes, 38) is None


def test_sma_uses_exactly_the_window_and_ends_at_the_index():
    closes = [1.0] * 40 + [100.0]
    # index 39 is the last of the forty ones
    assert ts.sma(closes, 39) == pytest.approx(1.0)
    # index 40 drops the oldest one and adds the hundred
    assert ts.sma(closes, 40) == pytest.approx((39 * 1.0 + 100.0) / 40)


def test_sma_respects_a_custom_window():
    closes = list(range(1, 21))
    assert ts.sma(closes, 19, window=5) == pytest.approx(18.0)


# --------------------------------------------------------------------------
# classify — the boundary
# --------------------------------------------------------------------------

def test_price_exactly_on_the_average_is_strong_not_weak():
    """The rule says 'at or above'. A tie has to resolve, and it resolves up."""
    got = ts.classify(series([100.0] * 45))
    assert got["state"] == ts.STRONG
    assert got["distance"] == pytest.approx(0.0)


def test_a_cent_below_the_average_is_weak():
    closes = [100.0] * 44 + [99.0]
    got = ts.classify(series(closes))
    assert got["state"] == ts.WEAK
    assert got["distance"] < 0


def test_classify_returns_none_without_enough_history():
    assert ts.classify(series([100.0] * 20)) is None


def test_distance_is_measured_against_the_average_not_the_prior_close():
    closes = [100.0] * 40 + [200.0]
    got = ts.classify(series(closes))
    avg = (39 * 100.0 + 200.0) / 40
    assert got["distance"] == pytest.approx(200.0 / avg - 1)


# --------------------------------------------------------------------------
# The near-line flag — the mitigation for weekly data
# --------------------------------------------------------------------------

def test_near_line_flags_a_name_sitting_on_its_average():
    """A daily SMA could put this one on the other side, so it must be flagged."""
    closes = [100.0] * 44 + [100.5]
    got = ts.classify(series(closes))
    assert got["near_line"] is True


def test_near_line_does_not_flag_a_name_well_clear():
    closes = [100.0] * 44 + [180.0]
    got = ts.classify(series(closes))
    assert got["near_line"] is False


def test_near_line_is_symmetric_about_the_average():
    below = ts.classify(series([100.0] * 44 + [99.0]))
    above = ts.classify(series([100.0] * 44 + [101.0]))
    assert below["near_line"] and above["near_line"]
    assert below["state"] == ts.WEAK and above["state"] == ts.STRONG


# --------------------------------------------------------------------------
# weeks_on_side — the tag alone hides this
# --------------------------------------------------------------------------

def test_a_fresh_crossover_counts_one_week():
    closes = [100.0] * 40 + [80.0] * 6 + [130.0]
    got = ts.classify(series(closes))
    assert got["state"] == ts.STRONG
    assert got["weeks_in_state"] == 1


def test_a_long_held_side_counts_many_weeks():
    closes = [100.0] * 40 + [float(120 + i) for i in range(12)]
    got = ts.classify(series(closes))
    assert got["state"] == ts.STRONG
    assert got["weeks_in_state"] >= 10


def test_run_length_is_never_negative_or_longer_than_the_series():
    closes = [100.0] * 60
    got = ts.classify(series(closes))
    assert 0 <= got["weeks_in_state"] <= len(closes)


# --------------------------------------------------------------------------
# Slope of the average
# --------------------------------------------------------------------------

def test_a_rising_average_is_reported_rising():
    closes = [float(50 + i) for i in range(60)]
    got = ts.classify(series(closes))
    assert got["sma_rising"] is True
    assert got["sma_slope"] > 0


def test_a_falling_average_is_reported_falling():
    closes = [float(200 - i) for i in range(60)]
    got = ts.classify(series(closes))
    assert got["sma_rising"] is False
    assert got["sma_slope"] < 0


def test_slope_is_none_when_history_is_too_short_to_look_back():
    """45 weeks gives an average today but none from 13 weeks ago."""
    got = ts.classify(series([100.0] * 45))
    assert got["sma_slope"] is None
    assert got["sma_rising"] is None
    assert got["state"] == ts.STRONG      # the tag still resolves


def test_slope_appears_once_there_is_a_prior_average_to_compare():
    got = ts.classify(series([100.0] * 54))
    assert got["sma_slope"] is not None
    assert got["sma_rising"] is False     # flat is not rising


def test_price_can_be_above_a_falling_average():
    """Both facts are reported because they mean different things."""
    closes = [float(200 - i) for i in range(58)] + [400.0]
    got = ts.classify(series(closes))
    assert got["state"] == ts.STRONG
    assert got["sma_rising"] is False


# --------------------------------------------------------------------------
# price_override — marking against a fresher quote
# --------------------------------------------------------------------------

def test_price_override_can_flip_the_state_and_is_labelled_stale():
    base = series([100.0] * 45)
    assert ts.classify(base)["state"] == ts.STRONG
    got = ts.classify(base, price_override=80.0)
    assert got["state"] == ts.WEAK
    assert got["price"] == 80.0
    assert got["stale_sma"] is True


def test_without_an_override_the_result_is_not_marked_stale():
    assert ts.classify(series([100.0] * 45))["stale_sma"] is False


def test_run_length_ignores_the_override():
    """The run counts closes in the series; an override is not one of them."""
    base = series([100.0] * 45)
    assert (ts.classify(base, price_override=80.0)["weeks_in_state"]
            == ts.classify(base)["weeks_in_state"])


# --------------------------------------------------------------------------
# classify_all
# --------------------------------------------------------------------------

def test_classify_all_drops_names_without_enough_history():
    got = ts.classify_all({"LONG": series([100.0] * 45),
                           "SHORT": series([100.0] * 10)})
    assert set(got) == {"LONG"}


def test_classify_all_applies_overrides_by_ticker():
    got = ts.classify_all(
        {"A": series([100.0] * 45), "B": series([100.0] * 45)},
        prices={"A": 50.0})
    assert got["A"]["state"] == ts.WEAK
    assert got["B"]["state"] == ts.STRONG
    assert got["B"]["stale_sma"] is False


# --------------------------------------------------------------------------
# forward_vol
# --------------------------------------------------------------------------

def test_forward_vol_is_zero_on_a_flat_series():
    assert ts.forward_vol(series([100.0] * 45)) == pytest.approx(0.0)


def test_forward_vol_rises_with_dispersion():
    calm = series([100.0 + (i % 2) * 0.5 for i in range(45)])
    wild = series([100.0 + (i % 2) * 20.0 for i in range(45)])
    assert ts.forward_vol(wild) > ts.forward_vol(calm)


def test_forward_vol_is_none_without_enough_weeks():
    assert ts.forward_vol(series([100.0] * 5)) is None
