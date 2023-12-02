import datetime as dt
import utils as util
import options as op

# Set the default episode duration in minutes.
episode_duration_mins = 24

print("\nWelcome to AnimeKetchup, for all of your catch-up needs.\n")

total_eps = int(input(
    "How many episodes would you like to watch?\n"))

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
        "(Example: 15 Aug 2023): \n")

    start_date = util.get_date(
        start_date_prompt)

end_date = util.get_date(
    end_date_prompt, require_future=True)

if end_date < start_date:
    print("The end date cannot be before the start date. "
          "Please provide valid dates.\n")

overall_watch_time = op.calc_watch_time_hrs(
    total_eps, episode_duration_mins)

avail_days = op.calc_days_avail_to_watch(
    start_date, end_date, days_per_week_limit=None)

eps_per_day_to_watch = op.calc_eps_per_day(
    total_eps, avail_days, eps_per_day_limit=None)

print(f"To watch {total_eps} episodes, that will take yourself a total of "
      f"{overall_watch_time} hours to complete.\n")

print(f"You can watch {eps_per_day_to_watch} episodes a day to finish watching "
      f"the episodes of your choice by your deadline.")
