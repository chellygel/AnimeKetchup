import datetime as dt
import day_counter as dc
import fun_fact as ff
import luffy

date_format = "%Y,%m,%d"

episodes = input("Hello! How many episodes is the show you are interested in watching? ")

end_date = input("What date would you like to have completed this series?(yyyy,mm,dd) ")
end_date = dt.datetime.strptime(end_date, date_format)

answer_today = input("Will you start watching today? [Y/n] ")
if answer_today.lower() == "y":
    start_date = None
else:
    start_date = input("What day will you start? (yyyy,mm,dd) ")
    # Totally trusting you to not bork the format for now lol
    start_date = dt.datetime.strptime(start_date, date_format)

# Time to math!

days = dc.calculate_days_delta(end_date, start_date)
eps = dc.calculate_episodes_per_day(episodes, days)
print(F"Wow, that's only {days} days until then !!!")
print(F"You will have to watch {eps} episodes per day to complete the show on time!")

ff = ff.random_factoid()
ff_eps_per_day = dc.calculate_episodes_per_day(ff[1], days)

print(F"In comparison you would have to watch {ff_eps_per_day} episodes per day if you were watching {ff[0]}!")
print(" ")
print(" ")
print(luffy.LUFFY)