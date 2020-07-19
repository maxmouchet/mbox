from hypothesis import given
from strategies import datetimes_nomicro

from mtoolbox.datetime import parsetimestamp, totimestamp


@given(dt=datetimes_nomicro())
def test_timestamp(dt):
    assert parsetimestamp(None) == None
    assert parsetimestamp("not a timestamp") == None
    assert parsetimestamp(totimestamp(dt)) == dt
    assert parsetimestamp(str(totimestamp(dt))) == dt
