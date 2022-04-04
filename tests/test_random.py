import pytest

from mbox.random import sample_groups


def test_sample_groups():
    population = [[None for _ in range(10)] for _ in range(20)]

    groups = sample_groups(population, 0.2)
    assert all(len(group) == 2 for group in groups)

    groups = sample_groups(population, 8)
    assert all(len(group) == 8 for group in groups)

    with pytest.raises(ValueError):
        sample_groups(population, 2.0)
