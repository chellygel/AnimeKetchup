import datetime as dt
import math


def calculate_watch_schedule(episodes, end_date, start_date, per_day_limit=None):
    """
    There are some options on what we could return to the user:
    1. basic episodes per day
    2. limited number of episodes by end date (possible)
    3. my limited number of episodes per day (not possible) which could return
        a: basic eps per day
        b: number of days to complete

    :param episodes:
    :param end_date:
    :param start_date:
    :param per_day_limit:
    :return: response dict
    """
    response = {
        "base_eps_per_day": 0,
        "days": 0,
        "actual_watch_days": 0,
        "is_possible": True,
        "realistic_end_date": None,
        "extra_episodes": None,
    }

    days_available = (end_date - start_date).days
    eps_per_day = math.ceil(episodes / days_available)
    actual_watch_days = episodes / eps_per_day
    response["base_eps_per_day"] = eps_per_day
    response["days"] = days_available
    response["actual_watch_days"] = actual_watch_days

    if per_day_limit:
        # It's possible the per day limit resolves before the end date
        min_days = episodes / per_day_limit
        realistic_end_date = start_date + dt.timedelta(days=min_days)
        response["realistic_end_date"] = realistic_end_date
        extra_episodes = episodes % per_day_limit
        response["extra_episodes"] = extra_episodes

        if realistic_end_date > end_date:
            # It isn't possible to watch with that limit so...
            response["is_possible"] = False

    return response
