from datetime import date
from ketchup import watch_schedule_builder as wsb


def test_per_week_limit_none():
    result = wsb.calculate_watch_schedule(
        episodes=14, end_date=date(2023, 8, 31), start_date=date(2023, 8, 1)
    )
    assert result["is_possible"]


def test_per_week_limit_not_exceeded():
    result = wsb.calculate_watch_schedule(
        episodes=20,
        end_date=date(2023, 8, 31),
        start_date=date(2023, 8, 1),
        per_week_limit=5,
    )
    assert result["is_possible"]


def test_per_week_limit_exceeded():
    result = wsb.calculate_watch_schedule(
        episodes=30,
        end_date=date(2023, 8, 31),
        start_date=date(2023, 8, 1),
        per_week_limit=5,
    )
    assert not result["is_possible"]
