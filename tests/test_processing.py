import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "value, state",
    [
        (
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        )
    ],
)


def test_filter_by_state(value, state):
    assert filter_by_state(value) == state


@pytest.mark.parametrize(
    "value, date",
    [
        (
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)


def test_sort_by_date(value, date):
    assert sort_by_date(value) == date
