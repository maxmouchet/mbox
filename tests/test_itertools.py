from mtoolbox.itertools import countby, groupby


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
