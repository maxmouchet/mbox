from datetime import datetime

from hypothesis import assume
from hypothesis.strategies import composite, datetimes


@composite
def datetimes_nomicro(draw, **kwargs):
    def nomicrosecond(x):
        return x.replace(microsecond=0)

    d = draw(datetimes(**kwargs).map(nomicrosecond))

    # https://github.com/HypothesisWorks/hypothesis/issues/2273
    # Folds and imaginary datetimes in the datetime strategy
    # Temporary solution to avoid imaginary dates.
    assume(datetime.fromtimestamp(d.timestamp()) == d)

    return d
