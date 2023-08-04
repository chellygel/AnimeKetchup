import random as r

SHOWS = {
    "One Piece": 1070,
    "Utena": 39
}


def random_factoid():
    show_name, show_episodes = r.choice(list(SHOWS.items()))
    return show_name, show_episodes

