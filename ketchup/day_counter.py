import datetime as dt


def calculate_episodes_per_day(episodes, days):
    # Calculate eps per day, will build more interesting options later.
    # . . . like counting weekends idk?
    eps_per_day = int(episodes) / days
    return eps_per_day


def calculate_days_delta(end_date, start_date=None):
    # Calculate to datetime object
    end_date = dt.date(end_date.year, end_date.month, end_date.day)

    start_date = start_date or dt.date.today()
    days_delta = end_date - start_date

    # Return a number of days
    return days_delta.days
