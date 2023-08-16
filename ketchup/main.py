import datetime

import dateparser
import datetime as dt
from ketchup.luffy import LUFFY
import ketchup.watch_schedule_builder as dc
import ketchup.fun_fact as fun_fact

DDP = dateparser.date.DateDataParser(languages=['en'], settings={'DATE_ORDER': 'DMY'})


def get_date(prompt: str, require_future: bool = False, require_past: bool = False) -> datetime.datetime:
    while True:
        try:
            user_date = input(prompt)
            user_date = DDP.get_date_data(user_date).date_obj
        except ValueError:
            print("Sorry, please only enter a date. An example would be '10 Aug 2023' ")
            continue
        if require_future:
            if user_date.date() < dt.date.today():
                print("Sorry, please only enter a future date.")
                continue
        if require_past:
            if user_date.date() > dt.date.today():
                print("Sorry, please only enter a past date.")
                continue
        else:
            break
    return user_date


def run():
    while True:
        try:
            episodes = int(input(
                "\nHello! How many episodes are in the show you are interested in watching?:\n"
            ))
        except ValueError:
            print("Sorry, please only enter a value greater than 0.")
            continue

        if episodes <= 0:
            print("Sorry, please only enter a value greater than 0.")
            continue
        else:
            break

    end_date_prompt = "What date would you like to have completed this series?(Ex: 15 Aug 2050):\n"
    end_date = get_date(end_date_prompt, require_future=True)

    answer_today = input("Will you start watching today? [Y/N]:\n") or "y"
    if answer_today.lower() == "y":
        start_date = dt.datetime.today()
    else:
        start_date_prompt = "What day will you start? (Ex: 15 Aug 2023):\n"
        start_date = get_date(start_date_prompt)

    per_week_limit = int(input("How many episodes a week do you plan to watch as well?:\n"))

    per_day_limit = int(input("What is the limit of episodes you will watch per day? [0+]\n") or 0)

    # The following seems as though it could be better...
    # We want to set the per day limit as an integer, or None...
    try:
        per_day_limit = int(per_day_limit)
        if per_day_limit == 0:
            per_day_limit = None
    except ValueError:
        per_day_limit = None

    # Time to math!
    watch_schedule = dc.calculate_watch_schedule(episodes, end_date, start_date, per_day_limit, per_week_limit)
    print(f"Wow, that's only {watch_schedule['days']} days between today and then!")

    if watch_schedule["is_possible"]:
        print(
            f"You will have to watch {watch_schedule['base_eps_per_day']} episodes per day "
            f"to complete the show on time!"
        )
        if watch_schedule["extra_episodes"]:
            print(f"You will have {watch_schedule['extra_episodes']} extra, "
                  f"you can add an additional watch day or tack them on to one of your other days.")
    else:
        print(f"I'm sorry, but that limit and end date make it impossible!")
        print(f"Don't worry, consider these options instead:")
        print(
            f"Option 1: You can watch {watch_schedule['base_eps_per_day']} episodes per day to catch up"
        )
        if watch_schedule["extra_episodes"]:
            print(f"You will have {watch_schedule['extra_episodes']} extra, "
                  f"you can add an additional watch day or tack them on to one of your other days.")
        print(
            f"Option 2: You could also choose to watch {per_day_limit} episodes per day "
            f"and finish by {watch_schedule['realistic_end_date']}"
        )

    ff = fun_fact.random_factoid()
    ff_watch_schedule = dc.calculate_watch_schedule(ff[1], end_date, start_date, per_day_limit, per_week_limit)

    print(
        f"In comparison you would have to watch {ff_watch_schedule['base_eps_per_day']} "
        f"episodes per day if you were watching {ff[0]}!"
    )
    print(" ")
    print(" ")
    print(LUFFY)
