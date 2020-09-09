from datetime import datetime, timedelta
from math import ceil
from typing import Any, Iterator, Optional


def datetimerange(
    start: datetime, stop: datetime, step: timedelta
) -> Iterator[datetime]:
    n = (stop - start) / step
    return (start + i * step for i in range(ceil(n)))


def parsetimestamp(x: Any, tz: Any = None) -> Optional[datetime]:
    try:
        return datetime.fromtimestamp(int(x), tz)
    except (TypeError, ValueError):
        return None


def totimestamp(x: datetime) -> int:
    return int(x.timestamp())
