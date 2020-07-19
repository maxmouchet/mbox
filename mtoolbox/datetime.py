from datetime import datetime
from typing import Any, Optional


def parsetimestamp(x: Any) -> Optional[datetime]:
    try:
        return datetime.fromtimestamp(int(x))
    except (TypeError, ValueError):
        return None


def totimestamp(x: datetime) -> int:
    return int(x.timestamp())
