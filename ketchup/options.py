import math

"""
This file needs to be renamed, possibly to math-utils.py, or something more to
reflect its usage.

- Used to create mathematical functions and logic.
- Used to create an option generator, to be called by main.py instead.
"""


def calculate_episodes_from_hours(episodes, episode_duration_mins=24):
    total_hours = (episodes * episode_duration_mins) / 60
    days = int(total_hours // 24)
    hours = int(total_hours % 24)
    return days, hours


# Option 0 in Discord.
def calc_watch_time_hrs(total_eps, episode_length_mins):
    overall_watch_time = total_eps * episode_length_mins / 60
    return overall_watch_time


def calc_days_avail_to_watch(start_date, end_date, eps_per_week_limit=None):
    # Calculate the difference between the end_date and the start_date.
    calc_date_diff = end_date - start_date

    # Extracts the total number of days from the timedelta "day" object.
    avail_days = calc_date_diff.days

    if eps_per_week_limit:
        weeks = math.ceil(avail_days / 7)
        avail_days = min(weeks * eps_per_week_limit, avail_days)

    return avail_days


def calc_eps_per_day(total_eps, avail_days, eps_per_day_limit=None):
    if avail_days <= 0:
        return 0  # This avoids division by zero.

    if eps_per_day_limit is not None:
        result = min(total_eps / avail_days, eps_per_day_limit)
    else:
        result = total_eps / avail_days

    return math.ceil(result)


#  entry point function??
def calc_all(
        total_eps,
        days_until_end_date,
        start_date,
        end_date,
        eps_per_day_limit=None,
        days_per_week_limit=None):
    #  If only total_episodes & days: call calculate_eps_per_day
    if total_eps is not None and days_until_end_date is not None:
        result = calc_eps_per_day(
            total_eps,
            days_until_end_date
        )

    # If only eps_per_day_limit is set, call calculate_eps_per_day with the
    # eps_per_day_limit set.
    elif eps_per_day_limit is not None and days_per_week_limit is None:
        result = calc_eps_per_day(
            total_eps,
            days_until_end_date,
            eps_per_day_limit
        )

    # If only days_per_week_limit is set, call calculate_eps_per_day with the
    # days_per_week_limit set.
    elif eps_per_day_limit is None and days_per_week_limit is not None:
        actual_total_days = calc_days_avail_to_watch(
            start_date,
            end_date,
            days_per_week_limit
        )

        result = calc_eps_per_day(total_eps, actual_total_days)

    # If both eps_per_day_limit and days_per_week_limit are set. Call the
    # calc_days_avail_to_watch and the calc_eps_per_day with limits, then do
    # the math if possible or not, and set response to possible or not.
    elif eps_per_day_limit is not None and days_per_week_limit is not None:
        days_available = calc_days_avail_to_watch(start_date, end_date)

        eps_per_day_with_limits = calc_eps_per_day(
            total_eps,
            days_until_end_date,
            eps_per_day_limit)

        is_possible = (eps_per_day_with_limits * 7 <= days_per_week_limit and
                       total_eps <= days_available * eps_per_day_limit)

        if is_possible:
            result = eps_per_day_with_limits

        else:
            result = calc_eps_per_day(
                total_eps,
                days_available,
                eps_per_day_limit
            )

    else:
        pass

    return result


def build_not_possible_options(
        total_eps,
        days_until_end_date,
        start_date,
        end_date,
        eps_per_day_limit=None,
        days_per_week_limit=None):
    pass
