import datetime as dt
import unittest.mock
from ketchup import main


def test_get_date_valid_future_date():
    future_date = dt.date.today() + dt.timedelta(days=7)
    user_input = future_date.strftime("%d % %Y")

    #  strftime is the string format time which is a part of the
    #  datetime module. The format is: day, month, year.

    with unittest.mock.patch("builtins.input", return_value=user_input):
        result = main.get_date("Enter a date: ", require_future=True)

    assert result.date() == future_date


def test_get_date_valid_any_date():
    date = dt.date.today()
    user_input = date.strftime("%d %b %Y")

    with unittest.mock.patch("builtins.input", return_value=user_input):
        result = main.get_date("Enter a date: ")

    assert isinstance(result, dt.datetime)
    assert result.date() == date


def test_get_date_invalid_input():
    user_input = "InvalidDateInput"

    with unittest.mock.patch("builtins.input", return_value=user_input):
        result = main.get_date("Enter a date: ")

    assert result is None
