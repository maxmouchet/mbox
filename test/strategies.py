from hypothesis import assume
from hypothesis.strategies import composite, datetimes


@composite
def datetimes_nomicro(draw, **kwargs):
    def nomicrosecond(x):
        return x.replace(microsecond=0)

    return draw(datetimes(**kwargs).map(nomicrosecond))
