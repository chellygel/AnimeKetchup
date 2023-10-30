import dateparser
import datetime as dt

DDP = dateparser.date.DateDataParser(
    languages=["en"], settings={"DATE_ORDER": "DMY"})


def get_date(
        prompt: str, require_future: bool = False, require_past: bool = False
) -> dt.datetime:
    while True:
        try:
            user_date = input(prompt)
            user_date = DDP.get_date_data(user_date).date_obj
        except ValueError:
            print("Sorry, please only enter a date. "
                  "An example would be '10 Aug 2023' ")
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
