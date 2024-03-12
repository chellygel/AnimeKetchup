import datetime as dt

from . import utils as util
from . import options as op

# The purpose of this file was to replace the current 'main.py' file, and to
# slim down the overall size of the file, especially with how the `options.py`
# and `utils.py` files have been created to extract functions from the original
# code that we were using multiple times. This helps to improve how we adhere
# by the DRY method.


def run():
    # This will not always be hard-coded as "24", because certain episodes will
    # have different episode lengths, and also we plan to allow users to insert
    # an input called "filler" to remove any filler episodes from their watch.
    episode_duration_mins = 24

    print("\nWelcome to animeketchup, for all of your catch-up needs.\n")

    total_eps = int(input(
        "How many episodes would you like to watch?\n"))

    eps_per_week_limit = int(input(
        "\nHow many episodes would you like to watch per week? "
        "Enter '0' for no limit.\n")
    )

    end_date_prompt = (
        "\nWhat date would you like to have completed this "
        "series? (Example: 15 Aug 2050): \n")

    answer_today = input(
        "\nWill you start watching today? [Y/N]:\n") or "y"

    start_date = None

    if answer_today.lower() == "y":
        start_date = dt.datetime.today()

    else:
        start_date_prompt = (
            "\nWhat day will you start watching? "
            "(Example: 15 Aug 2050): \n")

        start_date = util.get_date(start_date_prompt)

    end_date = util.get_date(end_date_prompt, require_future=True)

    if start_date is None:
        print("Invalid start date. Exiting.")
        return

    if end_date < start_date:
        print("The end date cannot be before the start date. "
              "Please provide valid dates.\n")

    overall_watch_time = op.calc_watch_time_hrs(
        total_eps, episode_duration_mins)

    if eps_per_week_limit:
        avail_days = op.calc_days_avail_to_watch(
            start_date, end_date, eps_per_week_limit)

        end_date_with_limit = start_date + dt.timedelta(days=avail_days)

        if end_date_with_limit <= end_date:
            print(
                "\nYou are able to finish watching this anime by your desired "
                "end date.")

        print(
            f"\nWith your limit of \033[4m{eps_per_week_limit}\033[0m episodes "
            f"per week, you can finish watching this anime in "
            f"\033[4m{avail_days}\033[0m days.\n")

        print(f"That will be on the \033[4m"
              f"{end_date_with_limit.strftime('%d %b %Y at %I:%M %p')}"
              f"\033[0m.")

        print(f"\nTo watch \033[4m{total_eps}\033[0m episodes, that will take "
              f"yourself a total of \033[4m{overall_watch_time}\033[0m hours to"
              f" complete.")

    else:
        limit_episodes_per_day = 3

        end_date_without_limit = start_date + dt.timedelta(
            hours=overall_watch_time)

        if end_date_without_limit <= end_date:
            print(
                "\nYou are able to finish watching this anime by your desired "
                "end date.")

        print(f"\nWithout a limit of how many episodes to watch per week, "
              f"you can finish this anime by \033[4m"
              f"{end_date_without_limit.strftime('%d %b %Y at %I:%M %p')}"
              f"\033[0m with \033[4m{overall_watch_time}\033[0m "
              f"hours of total watch time.")

        print("\nHowever, this in unrealistic, so.")

        end_date_with_limit = start_date + dt.timedelta(
            days=total_eps / limit_episodes_per_day)

        print(
            f"\nIf you limit yourself to \033[4m{limit_episodes_per_day}"
            f"\033[0m episodes per day, you can alternatively finish by "
            f"\033[4m{end_date_with_limit.strftime('%d %b %Y')}"
            f"\033[0m instead.")

    return start_date, end_date


if __name__ == "__main__":
    run()
