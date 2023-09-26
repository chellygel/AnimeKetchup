from ketchup import fun_fact as ff


def test_random_factoid():
    show = ff.random_factoid()

    assert show[0] in ff.SHOWS
    assert show[5] is ff.SHOWS[show[0]]
