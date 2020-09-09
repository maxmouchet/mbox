from datetime import datetime, timedelta

from hypothesis import given
from strategies import datetimes_nomicro

from mtoolbox.datetime import datetimerange, parsetimestamp, totimestamp


def test_daterange():
    start = datetime(2019, 1, 1)
    stop = datetime(2019, 1, 2)

    # Positive deltas
    dates = list(datetimerange(start, stop, timedelta(days=1, hours=12)))
    assert dates == [start]

    dates = list(datetimerange(start, stop, timedelta(days=1)))
    assert dates == [start]

    dates = list(datetimerange(start, stop, timedelta(hours=12)))
    assert dates == [start, start + timedelta(hours=12)]

    dates = list(datetimerange(stop, start, timedelta(hours=12)))
    assert dates == []

    # Negative deltas
    dates = list(datetimerange(stop, start, timedelta(days=-1, hours=-12)))
    assert dates == [stop]

    dates = list(datetimerange(stop, start, timedelta(days=-1)))
    assert dates == [stop]

    dates = list(datetimerange(stop, start, timedelta(hours=-12)))
    assert dates == [stop, stop - timedelta(hours=12)]

    # start = stop
    dates = list(datetimerange(start, start, timedelta(hours=12)))
    assert dates == []

    dates = list(datetimerange(start, start, timedelta(hours=-12)))
    assert dates == []


@given(dt=datetimes_nomicro())
def test_timestamp(dt):
    assert parsetimestamp(None) == None
    assert parsetimestamp("not a timestamp") == None
    assert parsetimestamp(totimestamp(dt)) == dt
    assert parsetimestamp(str(totimestamp(dt))) == dt
