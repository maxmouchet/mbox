from mtoolbox.itertools import countby, groupby, groupby_pairs, groupby_stream


def test_countby():
    elements = [(0, "a"), (0, "a"), (0, "b"), (1, "b")]

    counts = countby(elements, lambda x: x[0])
    assert counts == {0: 3, 1: 1}

    counts = countby(elements, lambda x: x[1])
    assert counts == {"a": 2, "b": 2}

    counts = countby([], lambda x: x[0])
    assert counts == {}


def test_groupby():
    elements = [(0, "a"), (0, "a"), (0, "b"), (1, "b")]

    groups = groupby(elements, lambda x: x[0])
    assert groups == {0: [(0, "a"), (0, "a"), (0, "b")], 1: [(1, "b")]}

    groups = groupby(elements, lambda x: x[1])
    assert groups == {"a": [(0, "a"), (0, "a")], "b": [(0, "b"), (1, "b")]}

    groups = groupby([], lambda x: x[0])
    assert groups == {}


def test_groupby_pairs():
    # TODO: Better test
    pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    groups = groupby_pairs(pairs, lambda x: x)
    assert groups == {0: [(0, 0)], 1: [(1, 1)]}


def test_groupby_stream():
    elements = [(0, "a"), (0, "a"), (0, "b"), (1, "b")]

    groups = dict(groupby_stream(elements, lambda x: x[0], 100))
    assert groups == groupby(elements, lambda x: x[0])

    groups = list(groupby_stream(elements, lambda x: x[0], 1))
    assert groups == [
        (0, [(0, "a")]),
        (0, [(0, "a")]),
        (0, [(0, "b")]),
        (1, [(1, "b")]),
    ]
