from ketchup import options as ops


def test_calc_watch_time_hrs():
    total_eps = 50
    episode_length_in_mins = 24

    response = ops.calc_watch_time_hrs(total_eps, episode_length_in_mins)

    assert response == 20
