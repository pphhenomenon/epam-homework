"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']  # noqa: E501
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']  # noqa: E501
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']  # noqa: E501

"""

from typing import Any, Iterable, List


def custom_range(iterable: Iterable[Any], start: Any,
                 stop: Any = None, step: int = 1) -> List[Any]:
    """Accepts any iterable of unique values and then it behaves
    as range function."""

    if isinstance(iterable, (str, tuple, dict)):
        iterable = list(iterable)

    if start not in iterable or stop is not None and stop not in iterable:
        raise ValueError("objects are not in list")

    if stop is None:
        stop = iterable.index(start)
        start = 0
    else:
        stop = iterable.index(stop)
        start = iterable.index(start)

    return iterable[start:stop:step]
