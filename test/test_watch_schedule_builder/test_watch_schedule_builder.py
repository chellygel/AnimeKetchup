from ketchup import watch_schedule_builder as wsb
import datetime as dt


def test_calculate_wsb_valid_response():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(50, end_date, start_date)

    assert response["base_eps_per_day"] == 5
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] is None
    assert response["extra_episodes"] is None


def test_calculate_wsb_valid_response_uneven_days():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(51, end_date, start_date)

    assert response["base_eps_per_day"] == 6
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] is None
    assert response["extra_episodes"] is None


def test_calculate_wsb_valid_response_per_day_limit():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(
        50, end_date, start_date, per_day_limit=5)

    assert response["base_eps_per_day"] == 5
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 11)
    assert response["extra_episodes"] == 0


def test_calculate_wsb_valid_response_per_day_limit_uneven_days():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(
        70, end_date, start_date, per_day_limit=5)

    assert response["base_eps_per_day"] == 7
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is False
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 15)
    assert response["extra_episodes"] == 0


def test_calculate_wsb_valid_response_per_day_limit_realistic_end_date():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(
        60, end_date, start_date, per_day_limit=10)

    assert response["base_eps_per_day"] == 6
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 7)
    assert response["extra_episodes"] == 0


def test_calculate_wsb_valid_response_per_day_limit_unrealistic_end_date():
    end_date = dt.datetime(2024, 11, 3)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(
        50, end_date, start_date, per_day_limit=10)

    assert response["base_eps_per_day"] == 25
    assert response["days"] == 2
    assert response["actual_watch_days"] == 2
    assert response["is_possible"] is False
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 6)
    assert response["extra_episodes"] == 0


def test_calculate_wsb_valid_response_per_day_limit_extra_episodes():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)

    response = wsb.calculate_watch_schedule(
        80, end_date, start_date, per_day_limit=10)

    assert response["base_eps_per_day"] == 8
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 9)
    assert response["extra_episodes"] == 0
