from collections import defaultdict
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


def countby(elements: Iterator[T], key: Callable[[T], U]) -> Dict[U, int]:
    groups = groupby(elements, key)
    counts = {k: len(v) for k, v in groups.items()}
    return counts


def groupby(elements: Iterator[T], key: Callable[[T], U]) -> Dict[U, List[T]]:
    groups: Dict[U, List[T]] = defaultdict(list)
    for el in elements:
        groups[key(el)].append(el)
    return dict(groups)
