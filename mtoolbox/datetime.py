from datetime import datetime, timedelta
from typing import Any, Iterator, Optional


def datetimerange(
    start: datetime, stop: datetime, step: timedelta
) -> Iterator[datetime]:
    curr = start
    while curr < stop:
        yield curr
        curr += step


def parsetimestamp(x: Any) -> Optional[datetime]:
    try:
        return datetime.fromtimestamp(int(x))
    except (TypeError, ValueError):
        return None


def totimestamp(x: datetime) -> int:
    return int(x.timestamp())
