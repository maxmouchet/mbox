from datetime import date, datetime, timedelta

from hypothesis import given
from hypothesis.extra.pytz import timezones
from hypothesis.strategies import shared
from pytz import UTC
from strategies import datetimes_nomicro

from mtoolbox.datetime import datetimerange, parsetimestamp, totimestamp

tzs = timezones()


def test_datetimerange():
    start = datetime(2019, 1, 1, 8, 15, 30)
    stop = datetime(2019, 1, 2, 8, 15, 30)

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

    # dates (not datetimes)
    start = date(2020, 1, 1)
    stop = date(2020, 1, 2)

    dates = list(datetimerange(start, stop, timedelta(days=1)))
    assert dates == [start]


@given(dt=datetimes_nomicro())
def test_timestamp(dt):
    assert parsetimestamp(None) == None
    assert parsetimestamp("not a timestamp") == None
    assert parsetimestamp(totimestamp(dt)) == dt
    assert parsetimestamp(str(totimestamp(dt))) == dt


@given(dt=datetimes_nomicro(timezones=shared(tzs)), tz=shared(tzs))
def test_timestamp_with_tz(dt, tz):
    assert parsetimestamp(totimestamp(dt), tz) == dt
    assert parsetimestamp(str(totimestamp(dt)), tz) == dt
