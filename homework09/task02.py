"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [0][1]

"""


from contextlib import contextmanager
from typing import Iterator


@contextmanager
def suppressor(exception: Exception) -> Iterator:
    try:
        yield
    except exception:
        pass


class Suppressor:
    def __init__(self, exception: Exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        if isinstance(value, self.exception):
            return True


if __name__ == '__main__':
    with Suppressor(IndexError):
        [0][1]
