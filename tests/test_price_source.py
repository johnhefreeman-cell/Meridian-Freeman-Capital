"""Tests for the price-source layer.

The behaviour that matters most is the partial-bar guard. A provider returns
today's bar while the session is still open, and a 14-day RSI computed on a
half-formed close produces a signal that will not exist at the close — a wrong
answer that looks exactly like a right one.
"""

import datetime as dt
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import price_source as ps  # noqa: E402

# The exact shape observed from the provider: semicolon-delimited, newest first.
SAMPLE = """datetime;open;high;low;close;volume
2026-09-04;452.5;460.20001;443.35999;454.70999;6009400
2026-09-03;432.42001;437.14001;426.13000;435.91000;5999200
2026-09-02;443.5;443.5;433.57001;438.45999;6518400
"""


def bar(day, close, volume=1_000_000):
    stamp = int(dt.datetime(day.year, day.month, day.day).timestamp())
    return [stamp, close, close * 1.01, close * 0.99, close, close, volume]


# --------------------------------------------------------------------------
# Parsing the provider's CSV
# --------------------------------------------------------------------------

def test_parses_the_observed_csv_shape():
    rows = ps.parse_twelvedata_csv(SAMPLE)
    assert len(rows) == 3
    assert len(rows[0]) == 1 + len(ps.BAR_FIELDS)


def test_rows_come_back_oldest_first_even_though_the_provider_sends_newest_first():
    rows = ps.parse_twelvedata_csv(SAMPLE)
    days = [dt.date.fromtimestamp(r[0]) for r in rows]
    assert days == sorted(days)
    assert days[-1] == dt.date(2026, 9, 4)


def test_ohlc_lands_in_the_right_columns():
    rows = ps.parse_twelvedata_csv(SAMPLE)
    last = rows[-1]
    assert last[1] == pytest.approx(452.5)        # open
    assert last[2] == pytest.approx(460.20001)    # high
    assert last[3] == pytest.approx(443.35999)    # low
    assert last[4] == pytest.approx(454.70999)    # close
    assert last[6] == 6009400                     # volume


def test_adj_mirrors_close_because_the_endpoint_publishes_no_adjusted_series():
    for row in ps.parse_twelvedata_csv(SAMPLE):
        assert row[5] == row[4]


def test_a_row_with_an_unparseable_price_is_skipped_not_zeroed():
    text = SAMPLE + "2026-09-01;;;;;\n"
    assert len(ps.parse_twelvedata_csv(text)) == 3


def test_empty_input_yields_no_rows_rather_than_raising():
    assert ps.parse_twelvedata_csv("") == []
    assert ps.parse_twelvedata_csv("datetime;open;high;low;close;volume\n") == []


# --------------------------------------------------------------------------
# The partial-bar guard
# --------------------------------------------------------------------------

def test_todays_bar_is_dropped_by_default():
    today = dt.date(2026, 9, 8)
    rows = [bar(dt.date(2026, 9, 4), 454.71), bar(today, 465.55, volume=20_235)]
    kept, notes = ps.drop_partial(rows, today=today)
    assert len(kept) == 1
    assert dt.date.fromtimestamp(kept[-1][0]) == dt.date(2026, 9, 4)
    assert any("today's session" in n for n in notes)


def test_todays_bar_can_be_kept_deliberately_after_the_close():
    today = dt.date(2026, 9, 8)
    rows = [bar(dt.date(2026, 9, 4), 454.71), bar(today, 465.55)]
    kept, _ = ps.drop_partial(rows, today=today, include_today=True)
    assert len(kept) == 2


def test_a_past_session_is_never_dropped():
    today = dt.date(2026, 9, 8)
    rows = [bar(dt.date(2026, 9, 3), 435.91), bar(dt.date(2026, 9, 4), 454.71)]
    kept, notes = ps.drop_partial(rows, today=today)
    assert len(kept) == 2
    assert notes == []


def test_a_thin_final_bar_is_flagged_even_when_it_is_kept():
    """An unfinished session looks like a normal bar with a fraction of the tape."""
    today = dt.date(2026, 9, 30)
    rows = [bar(dt.date(2026, 9, 1) + dt.timedelta(days=i), 100.0, volume=1_000_000)
            for i in range(25)]
    rows[-1][6] = 20_000
    kept, notes = ps.drop_partial(rows, today=today, include_today=True)
    assert len(kept) == 25
    assert any("unfinished session" in n for n in notes)


def test_a_normal_final_bar_is_not_flagged():
    today = dt.date(2026, 9, 30)
    rows = [bar(dt.date(2026, 9, 1) + dt.timedelta(days=i), 100.0, volume=1_000_000)
            for i in range(25)]
    _, notes = ps.drop_partial(rows, today=today, include_today=True)
    assert notes == []


def test_drop_partial_on_an_empty_series_is_a_no_op():
    assert ps.drop_partial([], today=dt.date(2026, 9, 8)) == ([], [])


# --------------------------------------------------------------------------
# Cross-source comparison
# --------------------------------------------------------------------------

def test_bars_are_joined_on_the_session_date_not_the_timestamp():
    """Providers stamp a daily bar at different times; the epoch is not a key."""
    day = dt.date(2026, 9, 4)
    at_open = [int(dt.datetime(2026, 9, 4, 13, 30).timestamp()),
               1, 1, 1, 454.71, 454.71, 100]
    at_midnight = bar(day, 454.71)
    assert at_open[0] != at_midnight[0]
    report = ps.compare([at_open], [at_midnight])
    assert report["common"] == 1
    assert report["disagreements"] == []


def test_a_real_price_difference_is_reported_with_its_size():
    day = dt.date(2026, 9, 4)
    report = ps.compare([bar(day, 100.0)], [bar(day, 102.0)])
    assert len(report["disagreements"]) == 1
    assert report["disagreements"][0]["gap"] == pytest.approx(100.0 / 102.0 - 1)
    assert report["worst"] == pytest.approx(abs(100.0 / 102.0 - 1))


def test_a_difference_inside_tolerance_is_not_reported():
    day = dt.date(2026, 9, 4)
    report = ps.compare([bar(day, 100.0)], [bar(day, 100.05)], tolerance=0.001)
    assert report["disagreements"] == []


def test_sessions_missing_from_either_side_are_named():
    a = [bar(dt.date(2026, 9, 3), 1.0), bar(dt.date(2026, 9, 4), 1.0)]
    b = [bar(dt.date(2026, 9, 4), 1.0), bar(dt.date(2026, 9, 8), 1.0)]
    report = ps.compare(a, b)
    assert report["only_a"] == ["2026-09-03"]
    assert report["only_b"] == ["2026-09-08"]


# --------------------------------------------------------------------------
# The Twelve Data path refuses clearly rather than failing obscurely
# --------------------------------------------------------------------------

def test_a_missing_key_says_what_to_do(monkeypatch):
    monkeypatch.delenv(ps.TD_KEY_ENV, raising=False)
    with pytest.raises(ps.SourceUnavailable) as exc:
        ps.fetch_twelvedata("AAPL")
    assert ps.TD_KEY_ENV in str(exc.value)


def test_an_unreachable_host_names_the_allowlist(monkeypatch):
    monkeypatch.setenv(ps.TD_KEY_ENV, "not-a-real-key")

    def boom(*a, **k):
        raise OSError("CONNECT tunnel failed, response 403")

    monkeypatch.setattr(ps.urllib.request, "urlopen", boom)
    with pytest.raises(ps.SourceUnavailable) as exc:
        ps.fetch_twelvedata("AAPL")
    assert "allowlist" in str(exc.value)


# --------------------------------------------------------------------------
# Cache writing
# --------------------------------------------------------------------------

def test_write_cache_round_trips_and_records_its_source(tmp_path):
    rows = ps.parse_twelvedata_csv(SAMPLE)
    path = ps.write_cache("AMAT", rows, root=str(tmp_path))
    payload = json.load(open(path))
    assert payload["ticker"] == "AMAT"
    assert payload["source"] == "twelvedata"
    assert payload["adj_is_close"] is True
    assert len(payload["rows"]) == 3


def test_class_shares_are_written_under_the_price_sources_spelling(tmp_path):
    path = ps.write_cache("BRK.B", ps.parse_twelvedata_csv(SAMPLE), root=str(tmp_path))
    assert Path(path).name == "BRK-B.json"
    assert json.load(open(path))["ticker"] == "BRK.B"
