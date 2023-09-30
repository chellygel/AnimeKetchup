import math


def calc_watch_length_in_time(episodes, episode_duration_mins=24):
    total_hours = (episodes * episode_duration_mins) / 60
    days = int(total_hours // 24)
    hours = int(total_hours % 24)
    return days, hours


def calc_time_avail(start_date, end_date, episodes, episode_duration_mins):
    time_available = end_date - start_date
    min_hours_needed = math.ceil(episodes * episode_duration_mins / 60)
    return time_available, min_hours_needed


def is_less_than_24_hours(episodes, episode_duration_mins):
    min_hours_needed = math.ceil(episodes * episode_duration_mins / 60)
    return min_hours_needed < 24
