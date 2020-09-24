from datetime import date, datetime, timedelta
from math import ceil
from typing import Any, Iterator, Optional, TypeVar, Union

T = TypeVar("T", date, datetime)


def datetimerange(start: T, stop: T, step: Optional[timedelta] = None) -> Iterator[T]:
    step = step or (stop - start)
    n = (stop - start) / step
    return (start + i * step for i in range(ceil(n)))


def parsetimestamp(x: Any, tz: Any = None) -> Optional[datetime]:
    try:
        return datetime.fromtimestamp(int(x), tz)
    except (TypeError, ValueError):
        return None


def totimestamp(x: datetime) -> int:
    return int(x.timestamp())
