from ketchup import options as ops
import datetime as dt


def test_calc_days_available_to_watch():
    end_date = dt.datetime(2023, 10, 8)
    start_date = dt.datetime(2023, 10, 1)

    response = ops.calc_days_avail_to_watch(start_date, end_date)

    assert response == 7
