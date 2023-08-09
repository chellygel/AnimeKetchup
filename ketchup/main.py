import datetime

from dateutil import parser
import datetime as dt
from ketchup.luffy import LUFFY
import ketchup.watch_schedule_builder as dc
import ketchup.fun_fact as fun_fact


def run():
    while True:
        try:
            episodes = int(input(
                "Hello! How many episodes are in the show you are interested in watching? "
            ))
        except ValueError:
            print("Sorry, please only enter a value greater than 0")
            continue

        if episodes <= 0:
            print("Sorry, please only enter a value greater than 0")
            continue
        else:
            break

    while True:
        try:
            end_date = input(
                "What date would you like to have completed this series?(yyyy,mm,dd) "
            )
            end_date = parser.parse(end_date)
        except ValueError:
            print("Sorry, please only enter a date. an example would be 2024,01,31")
            continue
        if end_date.date() < datetime.date.today():
            print("Sorry, please only enter a future date")
            continue
        else:
            break

    answer_today = input("Will you start watching today? [Y/n] ") or "y"
    if answer_today.lower() == "y":
        start_date = dt.datetime.today()
    else:
        start_date = input("What day will you start? (yyyy,mm,dd) ")
        start_date = parser.parse(start_date)

    per_day_limit = input("What is the limit of episodes you will watch per day?[leave empty or a number] ")

    # The following seems as though it could be better...
    # We want to set the per day limit as an integer, or None...
    try:
        per_day_limit = int(per_day_limit)
        if per_day_limit == 0:
            per_day_limit = None
    except ValueError:
        per_day_limit = None

    # Time to math!
    watch_schedule = dc.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit)
    print(f"Wow, that's only {watch_schedule['days']} days between today and then !!!")

    if watch_schedule["is_possible"]:
        print(
            f"You will have to watch {watch_schedule['base_eps_per_day']} episodes per day to complete the show on time!"
        )
        if watch_schedule["extra_episodes"]:
            print(f"You will have {watch_schedule['extra_episodes']} extra, you can add an additional watch day or tack them on to one of your other days.")
    else:
        print(f"I'm sorry, but that limit and end date make it impossible!")
        print(f"Don't worry, consider these options instead:")
        print(
            f"Option 1: You can watch {watch_schedule['base_eps_per_day']} episodes per day to catch up"
        )
        if watch_schedule["extra_episodes"]:
            print(f"You will have {watch_schedule['extra_episodes']} extra, you can add an additional watch day or tack them on to one of your other days.")
        print(
            f"Option 2: You could also choose to watch {per_day_limit} episodes per day and finish by {watch_schedule['realistic_end_date']}"
        )

    ff = fun_fact.random_factoid()
    ff_watch_schedule = dc.calculate_watch_schedule(ff[1], end_date, start_date, per_day_limit)

    print(
        f"In comparison you would have to watch {ff_watch_schedule['base_eps_per_day']} episodes per day if you were watching {ff[0]}!"
    )
    print(" ")
    print(" ")
    print(LUFFY)
