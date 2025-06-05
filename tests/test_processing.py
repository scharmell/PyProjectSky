import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        (
            "CANCELED",
            [{"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state(data_for_processing, state, expected):
    assert filter_by_state(data_for_processing, state) == expected


@pytest.mark.parametrize(
    "reversed, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(data_for_processing, reversed, expected):
    assert sort_by_date(data_for_processing, reversed) == expected
