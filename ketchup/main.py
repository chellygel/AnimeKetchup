import math
import dateparser
import datetime as dt
import ketchup.watch_schedule_builder as wsb
from ketchup import options as ops
from ketchup import utils

DDP = dateparser.date.DateDataParser(
    languages=["en"], settings={"DATE_ORDER": "DMY"})


def calculate_watch_length_in_time(episodes, episode_duration_mins=25):
    """
    This function is calculating the overall watch length of the show, by
    determining the amount of hours it will take from the episode amount
    which has been assigned. So, depending on the duration of the episode,
    you can about watch three episodes within an hour, if the episode duration
    is set to the default duration.
    """

    # This is processing how many total hours it is going to take to finish
    # watching the desired amount of episodes. It multiplies the amount of
    # episodes the user wishes to watch, by the episode_duration_mins that has
    # been defaulted to 24 minutes, and then that is divided by "60" for the
    # amount of minutes in an hour.

    total_hours = (episodes * episode_duration_mins) / 60
    days = int(total_hours // episode_duration_mins)
    hours = int(total_hours % episode_duration_mins)
    return days, hours


def determine_end_and_start_date():
    end_date_prompt = (
        "What date would you like to have completed this series? "
        "(Example: 15 Aug 2050): "
    )

    answer_today = input(
        "Will you start watching today? [Y/N]: ") or "y"

    if answer_today.lower() == "y":
        start_date = dt.datetime.today()
    else:
        start_date_prompt = "What day will you start?" \
                            " (Ex: 15 Aug 2023): "
        start_date = utils.get_date(start_date_prompt)

    end_date = utils.get_date(end_date_prompt, require_future=True)

    if end_date < start_date:
        print("The end date cannot be before the start date. "
              "Please provide valid dates.\n")

    return answer_today, start_date, end_date


# TODO: Remove most of the logic from this func, separate into separate files.
# TODO: Re-add the "Watch an allotted amount of episodes per day option.
# TODO: Re-add the "Assign both a limit to how many episodes a day you watch,
#       as well as how many days a week you decide to watch.
def run():
    print("\nHello and welcome to AnimeKetchup "
          "for all your episode catch-up needs!\n")
    while True:
        try:
            user_option = int(input(
                "Please choose an option:\n"
                "1) Watch specified amount of episodes without any limits.\n"
                "2) Choose how many days per week to watch episodes.\n"
                "3) Exit.\n"
                "\nEnter the number of your choice: "))

        except ValueError:
            print("Sorry, please enter a valid option.")
            continue

        if user_option == 1:
            while True:
                try:
                    episodes = int(input(
                        "How many episodes are you interested in watching?: "))
                except ValueError:
                    print("Sorry, please only enter a value greater than 0.")
                    continue
                if episodes <= 0:
                    print("Sorry, please only enter a value greater than 0.")
                    continue
                else:
                    break

            episode_duration_mins = 25

            answer_today, start_date, end_date = determine_end_and_start_date()

            time_available = end_date - start_date

            min_hours_needed = math.ceil(episodes * episode_duration_mins / 60)

            if time_available.total_seconds() < min_hours_needed * 3600:
                total_duration_hours = episodes * episode_duration_mins / 60
                current_time = dt.datetime.now()
                time_difference = dt.timedelta(hours=total_duration_hours)
                realistic_end_date = current_time + time_difference

                print(
                    f"Sorry, it is not possible to watch {episodes} "
                    f"episodes by that time. "
                    f"You would instead finish the "
                    f"show by {realistic_end_date}.\n"
                )
                continue

            watch_schedule = wsb.calculate_watch_schedule(
                episodes,
                end_date,
                start_date,
                episode_duration_mins=episode_duration_mins
            )

            if watch_schedule["days"] >= 0:
                days, hours = ops.calculate_episodes_from_hours(
                    episodes, episode_duration_mins)

                # Calculate the time difference between today and the end date
                time_difference = end_date - dt.datetime.now()
                time_difference_days = time_difference.days
                time_difference_seconds = time_difference.seconds

                time_difference_hours, remainder = divmod(
                    time_difference_seconds, 3600)
                time_difference_minutes, time_difference_seconds = divmod(
                    remainder, 60)

                print(
                    f"\nWow, that's only {time_difference_days} days, "
                    f"{time_difference_hours} hours, "
                    f"and {time_difference_minutes} "
                    f"minutes between today and then!")

                if days > 0:
                    print(
                        f"To watch your desired amount of episodes, "
                        f"that will take {days} days and {hours} hours.\n")

                else:
                    print(
                        f"To watch your desired amount of episodes, "
                        f"that will take {hours} hours.\n")

        elif user_option == 2:
            while True:
                try:
                    episodes = int(input(
                        "How many episodes are you interested in watching?: "))
                except ValueError:
                    print("Sorry, please only enter a value greater than 0.")
                    continue
                if episodes <= 0:
                    print("Sorry, please only enter a value greater than 0.")
                    continue
                else:
                    break

            episode_duration_mins = 25

            while True:
                try:
                    per_week_limit = int(input(
                        "How many days per week can you "
                        "dedicate to watching?: "))

                except ValueError:
                    print("Sorry, please only enter a value greater than 0.")
                    continue

                if per_week_limit <= 0:
                    print("Sorry, please only enter a value greater than 0.")
                    continue

                else:
                    break

            answer_today, start_date, end_date = determine_end_and_start_date()

            weeks_required = math.ceil(episodes / per_week_limit)

            episodes_per_day_alternative = 3
            episodes_per_day = episodes_per_day_alternative * per_week_limit

            weeks_required_alternative = math.ceil(episodes / episodes_per_day)

            realistic_end_date = start_date + dt.timedelta(
                weeks=weeks_required)

            realistic_end_date_alternative = start_date + dt.timedelta(
                weeks=weeks_required_alternative)

            print(f"To watch {episodes} episodes at a rate of {per_week_limit} "
                  f"days per week and one episode per day, you should finish by"
                  f" {realistic_end_date.strftime('%d %b %Y')}.\n")
            #  The realistic_end_date is considering only two episodes per week
            #  being watched by the user.

            print(f"Alternatively, you can watch {episodes_per_day_alternative}"
                  f" episodes a day, which is "
                  f"{episodes_per_day_alternative * per_week_limit} episodes "
                  f"per week. So you could finish within approximately "
                  f"{episodes_per_day_alternative} weeks.\n")

            print(f"Watching {episodes_per_day_alternative * per_week_limit} "
                  f"episodes per week instead, you can finish by "
                  f"{realistic_end_date_alternative.strftime('%d %b %Y')}.\n")

        elif user_option == 3:
            print("Thank you for using AnimeKetchup. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option.")

            another_option = input(
                "Would you like to choose another option? (Y/N): ").lower()

            if another_option != "y":
                print("Thank you for using AnimeKetchup. Goodbye!")
                break  # Break the loop if the user chooses not to continue.
