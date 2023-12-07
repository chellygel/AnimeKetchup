import datetime as dt
import unittest.mock
import io

from ketchup.main_wip import run


def test_run():
    def mock_input(prompt):
        if "How many episodes would you like to watch?" in prompt:
            return "12"
        elif "How many episodes would you like to watch per week?" in prompt:
            return "3"
        elif "Will you start watching today?" in prompt:
            return "y"
        else:
            return "15 Aug 2024"

    expected_output = "You are able to finish watching this anime" \
                      " by your desired end date."

    with unittest.mock.patch('builtins.input', side_effect=mock_input):
        with unittest.mock.patch('ketchup.utils.get_date',
                                 return_value=dt.datetime(2024, 8, 15)):
            with unittest.mock.patch('sys.stdout',
                                     new_callable=io.StringIO) as mock_stdout:
                start_date, end_date = run()
                assert expected_output in mock_stdout.getvalue()

    assert start_date is not None
    assert end_date == dt.datetime(2024, 8, 15)
