import datetime as dt
import math


def calculate_watch_schedule(
        episodes,
        end_date,
        start_date,
        episode_duration_mins=24,
        per_day_limit=None,
        per_week_limit=None
):
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
    :param episode_duration_mins: Duration of each episode in minutes
    :param per_day_limit:
    :param per_week_limit:
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

    # Calculate the total time available in hours
    total_available_hours = (end_date - start_date).total_seconds() / 3600

    # Calculate the episode duration in hours
    episode_duration_hours = episode_duration_mins / 60

    days_available = (end_date - start_date).days

    if days_available == 0:
        eps_possible = int(total_available_hours // episode_duration_hours)
        eps_per_day = eps_possible
    else:
        # Calculate the number of episodes
        # that can be watched within the available time
        eps_possible = int(total_available_hours // episode_duration_hours)
        eps_per_day = math.ceil(eps_possible / days_available)

    actual_watch_days = math.ceil(eps_possible / eps_per_day)

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

    if per_week_limit:
        weeks_available = days_available / 7
        eps_per_week = math.ceil(episodes / weeks_available)

        if eps_per_week > per_week_limit:
            response["is_possible"] = False

    return response