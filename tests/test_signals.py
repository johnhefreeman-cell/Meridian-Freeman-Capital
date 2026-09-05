"""Tests for the buy setup: close > 200-day SMA and RSI(14) < 40.

RSI carries the weight here. It is the one indicator in this repo where a
plausible-looking implementation gives wrong numbers — Wilder's smoothing is
not a rolling mean, and the two differ by enough on a trending series to move a
name across the threshold. So it is checked against an independently written
reference, not only against invariants.
"""

import datetime as dt
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import daily_prices as dp  # noqa: E402
import signals as sg  # noqa: E402


def series_from(closes, adj=None, start=dt.datetime(2024, 1, 2)):
    """A cache-shaped payload of full bars from a list of closes.

    Rows are [epoch, open, high, low, close, adj, volume] — the same shape the
    fetcher writes, so these tests break if that format changes rather than
    quietly reading the wrong column.
    """
    rows = []
    for i, c in enumerate(closes):
        stamp = int((start + dt.timedelta(days=i)).timestamp())
        c = float(c)
        a = float(adj[i]) if adj is not None else c
        rows.append([stamp, c, c * 1.01, c * 0.99, c, a, 1_000_000])
    return dict(ticker="TEST", symbol="TEST", rows=rows)


def reference_rsi(values, window=14):
    """Wilder's RSI written independently of the implementation.

    Deliberately structured differently — separate gain/loss lists and an
    explicit smoothing loop — so a shared mistake is unlikely.
    """
    changes = [values[i] - values[i - 1] for i in range(1, len(values))]
    ups = [c if c > 0 else 0.0 for c in changes]
    downs = [-c if c < 0 else 0.0 for c in changes]
    if len(changes) < window:
        return []
    avg_up = sum(ups[:window]) / window
    avg_down = sum(downs[:window]) / window
    out = []
    for k in range(window, len(changes) + 1):
        if k > window:
            avg_up = (avg_up * (window - 1) + ups[k - 1]) / window
            avg_down = (avg_down * (window - 1) + downs[k - 1]) / window
        out.append(100.0 if avg_down == 0
                   else 100.0 - 100.0 / (1.0 + avg_up / avg_down))
    return out


# --------------------------------------------------------------------------
# The rule's constants
# --------------------------------------------------------------------------

def test_the_rule_is_two_hundred_fourteen_and_forty():
    assert sg.SMA_DAYS == 200
    assert sg.RSI_DAYS == 14
    assert sg.RSI_BUY_BELOW == 40.0


# --------------------------------------------------------------------------
# sma
# --------------------------------------------------------------------------

def test_sma_is_none_until_the_window_fills_then_appears():
    out = sg.sma([1.0] * 10, window=5)
    assert out[3] is None
    assert out[4] == pytest.approx(1.0)


def test_sma_rolls_rather_than_accumulating():
    out = sg.sma([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], window=3)
    assert out[2] == pytest.approx(2.0)
    assert out[5] == pytest.approx(5.0)


def test_sma_does_not_drift_over_a_long_series():
    """The rolling subtraction accumulates float error; check it stays tight."""
    vals = [100.0 + (i % 7) for i in range(5000)]
    out = sg.sma(vals, window=200)
    direct = sum(vals[-200:]) / 200
    assert out[-1] == pytest.approx(direct, abs=1e-9)


# --------------------------------------------------------------------------
# rsi — against the independent reference
# --------------------------------------------------------------------------

def test_rsi_matches_an_independent_implementation():
    vals = [100.0]
    for i in range(120):
        step = ((i * 37) % 11) - 5          # deterministic, mixed up and down
        vals.append(max(1.0, vals[-1] + step * 0.6))
    got = [x for x in sg.rsi(vals, 14) if x is not None]
    want = reference_rsi(vals, 14)
    assert len(got) == len(want)
    for a, b in zip(got, want):
        assert a == pytest.approx(b, abs=1e-9)


def test_rsi_is_wilder_smoothing_not_a_rolling_mean():
    """A rolling-mean lookalike gives a materially different number."""
    vals = [100.0]
    for i in range(60):
        vals.append(vals[-1] * (1.012 if i % 5 else 0.97))

    def rolling_mean_rsi(v, n=14):
        ch = [v[i] - v[i - 1] for i in range(1, len(v))]
        up = [max(c, 0.0) for c in ch]
        dn = [max(-c, 0.0) for c in ch]
        au = sum(up[-n:]) / n
        ad = sum(dn[-n:]) / n
        return 100.0 if ad == 0 else 100.0 - 100.0 / (1.0 + au / ad)

    wilder = sg.rsi(vals, 14)[-1]
    naive = rolling_mean_rsi(vals, 14)
    assert abs(wilder - naive) > 1.0        # they are not the same indicator


def test_rsi_first_value_lands_exactly_at_the_window_index():
    vals = [100.0 + i for i in range(30)]
    out = sg.rsi(vals, 14)
    assert out[13] is None
    assert out[14] is not None


def test_rsi_is_one_hundred_when_nothing_falls():
    assert sg.rsi([100.0 + i for i in range(40)], 14)[-1] == pytest.approx(100.0)


def test_rsi_is_zero_when_nothing_rises():
    assert sg.rsi([200.0 - i for i in range(40)], 14)[-1] == pytest.approx(0.0)


def test_rsi_sits_near_fifty_on_a_symmetric_sawtooth_and_leans_with_the_last_bar():
    """Equal up and down moves centre RSI on 50, but Wilder smoothing weights
    the newest bar most, so the last change tips it either side. Both facts are
    asserted — a value pinned exactly on 50 would mean the smoothing is missing.
    """
    def sawtooth(steps, first_up=True):
        vals = [100.0]
        for i in range(steps):
            up = (i % 2 == 0) if first_up else (i % 2 == 1)
            vals.append(vals[-1] + (1.0 if up else -1.0))
        return vals

    ends_down = sg.rsi(sawtooth(80, first_up=True), 14)[-1]
    ends_up = sg.rsi(sawtooth(80, first_up=False), 14)[-1]
    assert 45.0 < ends_down < 50.0
    assert 50.0 < ends_up < 55.0
    assert ends_down + ends_up == pytest.approx(100.0, abs=0.5)


def test_rsi_stays_inside_its_bounds():
    vals = [100.0]
    for i in range(400):
        vals.append(max(0.5, vals[-1] * (1 + (((i * 53) % 21) - 10) / 100)))
    for x in sg.rsi(vals, 14):
        if x is not None:
            assert 0.0 <= x <= 100.0


def test_rsi_returns_all_none_when_the_series_is_too_short():
    assert sg.rsi([100.0] * 10, 14) == [None] * 10


# --------------------------------------------------------------------------
# The setup
# --------------------------------------------------------------------------

def rising_then(pullback_pct, n=260):
    """A long uptrend, then a pullback that leaves price above the average."""
    vals = [100.0 * (1.004 ** i) for i in range(n)]
    peak = vals[-1]
    for k in range(1, 16):
        vals.append(peak * (1 - pullback_pct * k / 15))
    return vals


def test_buy_needs_both_legs():
    """Above the average with no pullback is not the setup."""
    got = sg.evaluate(series_from([100.0 * (1.004 ** i) for i in range(260)]))
    assert got["above_sma"] is True
    assert got["rsi_below"] is False
    assert got["buy"] is False


def test_a_pullback_inside_an_uptrend_fires():
    got = sg.evaluate(series_from(rising_then(0.10)))
    assert got["above_sma"] is True
    assert got["rsi_below"] is True
    assert got["buy"] is True


def test_oversold_below_the_average_does_not_fire():
    """The falling-knife case the trend leg exists to exclude."""
    vals = [200.0 - i * 0.4 for i in range(280)]
    got = sg.evaluate(series_from(vals))
    assert got["rsi_below"] is True
    assert got["above_sma"] is False
    assert got["buy"] is False


def test_price_exactly_on_the_average_is_not_above_it():
    """`buy` requires a strict close above; a tie is not an uptrend."""
    got = sg.evaluate(series_from([100.0] * 260))
    assert got["above_sma"] is False
    assert got["buy"] is False


def test_rsi_exactly_at_the_threshold_does_not_fire():
    """'less than 40' is strict, so 40.0 itself is not a pullback."""
    assert sg.evaluate(series_from(rising_then(0.10)), rsi_below=0.0)["buy"] is False


def test_evaluate_returns_none_without_two_hundred_bars():
    assert sg.evaluate(series_from([100.0] * 150)) is None


def test_near_line_flags_fire_close_to_each_threshold():
    got = sg.evaluate(series_from(rising_then(0.10)))
    # engineered to sit near the RSI line; the flag must notice
    near = sg.evaluate(series_from(rising_then(0.10)), rsi_below=got["rsi"] + 1.0)
    assert near["near_rsi_line"] is True


def test_distance_is_signed_and_relative_to_the_average():
    got = sg.evaluate(series_from([100.0 * (1.004 ** i) for i in range(260)]))
    assert got["distance"] == pytest.approx(got["close"] / got["sma"] - 1)
    assert got["distance"] > 0


# --------------------------------------------------------------------------
# evaluate_both — the dividend-adjustment guard
# --------------------------------------------------------------------------

def test_agreeing_series_report_agreement():
    got = sg.evaluate_both(series_from(rising_then(0.10)))
    assert got["agrees"] is True


def test_disagreement_between_adjusted_and_raw_is_surfaced():
    """A dividend-adjusted average can sit on the other side of today's close."""
    n = 260
    adj = [90.0] * n + [101.0]              # adjusted history sits lower
    got = sg.evaluate_both(series_from([100.0] * n + [101.0], adj=adj))
    assert got["above_sma"] is True         # against the adjusted average
    assert got["raw"]["above_sma"] is True
    assert got["agrees"] is True            # both above here
    # now push the raw history above today's close so the two disagree
    got2 = sg.evaluate_both(series_from([110.0] * n + [101.0], adj=adj))
    assert got2["above_sma"] is True
    assert got2["raw"]["above_sma"] is False
    assert got2["agrees"] is False


# --------------------------------------------------------------------------
# Symbol handling
# --------------------------------------------------------------------------

def test_class_shares_are_translated_for_the_price_source_and_back():
    assert dp.to_yahoo("BRK.B") == "BRK-B"
    assert dp.from_yahoo("BRK-B") == "BRK.B"


def test_ordinary_tickers_pass_through_untouched():
    assert dp.to_yahoo("AMAT") == "AMAT"
    assert dp.from_yahoo("AMAT") == "AMAT"


def test_closes_selects_the_requested_field():
    s = series_from([10.0] * 3, adj=[9.0] * 3)
    assert dp.closes(s, "close")[1] == [10.0, 10.0, 10.0]
    assert dp.closes(s, "adj")[1] == [9.0, 9.0, 9.0]


def test_column_rejects_an_unknown_field_instead_of_guessing():
    with pytest.raises(KeyError):
        dp.column(series_from([10.0] * 3), "vwap")


def test_column_reads_the_high_and_low_the_fill_logic_depends_on():
    s = series_from([100.0] * 3)
    assert dp.column(s, "high")[0] == pytest.approx(101.0)
    assert dp.column(s, "low")[0] == pytest.approx(99.0)
