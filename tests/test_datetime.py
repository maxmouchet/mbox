from datetime import datetime, timedelta

from hypothesis import given
from strategies import datetimes_nomicro

from mtoolbox.datetime import datetimerange, parsetimestamp, totimestamp


def test_daterange():
    start = datetime(2019, 1, 1)
    stop = datetime(2019, 1, 2)

    dates = list(datetimerange(start, stop, timedelta(days=1)))
    assert dates == [start]

    dates = list(datetimerange(start, stop, timedelta(hours=12)))
    assert dates == [start, start + timedelta(hours=12)]


@given(dt=datetimes_nomicro())
def test_timestamp(dt):
    assert parsetimestamp(None) == None
    assert parsetimestamp("not a timestamp") == None
    assert parsetimestamp(totimestamp(dt)) == dt
    assert parsetimestamp(str(totimestamp(dt))) == dt
