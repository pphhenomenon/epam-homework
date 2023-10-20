"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""

from typing import Callable


def storage(function: Callable) -> Callable:

    cache = {}

    def wrapper(*args, **kwargs):
        key = "{} {}".format(args, kwargs)

        if key in cache:
            return cache[key]

        value = function(*args, **kwargs)
        cache[key] = value
        return value

    return wrapper
