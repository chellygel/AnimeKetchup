from dateutil import parser
from ketchup.luffy import LUFFY
import ketchup.day_counter as dc
import ketchup.fun_fact as fun_fact


def run():
    episodes = input(
        "Hello! How many episodes is the show you are interested in watching? "
    )

    end_date = input(
        "What date would you like to have completed this series?(yyyy,mm,dd) "
    )
    end_date = parser.parse(end_date)

    answer_today = input("Will you start watching today? [Y/n] ") or "y"
    if answer_today.lower() == "y":
        start_date = None
    else:
        start_date = input("What day will you start? (yyyy,mm,dd) ")
        # Totally trusting you to not bork the format for now lol
        start_date = parser.parse(start_date)

    # Time to math!

    days = dc.calculate_days_delta(end_date, start_date)
    eps = dc.calculate_episodes_per_day(episodes, days)
    print(f"Wow, that's only {days} days until then !!!")
    print(
        f"You will have to watch {eps} episodes per day to complete the show on time!"
    )

    ff = fun_fact.random_factoid()
    ff_eps_per_day = dc.calculate_episodes_per_day(ff[1], days)

    print(
        f"In comparison you would have to watch {ff_eps_per_day} episodes per day if you were watching {ff[0]}!"
    )
    print(" ")
    print(" ")
    print(LUFFY)
