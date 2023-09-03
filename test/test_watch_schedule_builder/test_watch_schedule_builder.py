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
    assert response["actual_watch_days"] == 8.5
    assert response["is_possible"] is True
    assert response["realistic_end_date"] is None
    assert response["extra_episodes"] is None


def test_calculate_wsb_valid_response_per_day_limit():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)
    episodes = 50
    per_day_limit = 5

    response = wsb.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=per_day_limit)

    extra_episodes = episodes % per_day_limit

    assert response["base_eps_per_day"] == 5
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 11)
    assert response["extra_episodes"] == extra_episodes
    assert response["per_day_limit"] == per_day_limit


def test_calculate_wsb_valid_response_per_day_limit_uneven_days():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)
    episodes = 63
    per_day_limit = 3

    response = wsb.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=per_day_limit)

    extra_episodes = episodes % per_day_limit

    assert response["base_eps_per_day"] == 7
    assert response["days"] == 10
    assert response["actual_watch_days"] == 9
    assert response["is_possible"] is False
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 22)
    assert response["extra_episodes"] == extra_episodes
    assert response["per_day_limit"] == per_day_limit


def test_calculate_wsb_valid_response_per_day_limit_realistic_end_date():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)
    episodes = 60
    per_day_limit = 10

    response = wsb.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=per_day_limit)

    assert response["base_eps_per_day"] == 6
    assert response["days"] == 10
    assert response["actual_watch_days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 7)
    assert response["extra_episodes"] == 0
    assert response["per_day_limit"] == per_day_limit


def test_calculate_wsb_valid_response_per_day_limit_unrealistic_end_date():
    end_date = dt.datetime(2024, 11, 3)
    start_date = dt.datetime(2024, 11, 1)
    episodes = 50
    per_day_limit = 10

    response = wsb.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=per_day_limit)

    assert response["base_eps_per_day"] == 25
    assert response["days"] == 2
    assert response["actual_watch_days"] == 2
    assert response["is_possible"] is False
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 6)
    assert response["extra_episodes"] == 0
    assert response["per_day_limit"] == per_day_limit


def test_calculate_wsb_valid_response_per_day_limit_extra_episodes():
    end_date = dt.datetime(2024, 11, 11)
    start_date = dt.datetime(2024, 11, 1)
    episodes = 75
    per_day_limit = 10

    response = wsb.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=per_day_limit)

    assert response["base_eps_per_day"] == 8
    assert response["days"] == 10
    assert response["is_possible"] is True
    assert response["realistic_end_date"] == dt.datetime(2024, 11, 8, 12)
    assert response["extra_episodes"] == 5
    assert response["per_day_limit"] == per_day_limit
