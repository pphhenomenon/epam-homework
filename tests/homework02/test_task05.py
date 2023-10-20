from string import ascii_lowercase

import pytest

from homework02.task05 import custom_range


@pytest.mark.parametrize(
    "iterable, start, stop, step, output",
    [
        (ascii_lowercase, "l", "g", 2, []),
        (ascii_lowercase, "g", "l", -2, []),
        (ascii_lowercase, "l", "g", None, []),
        (ascii_lowercase, "l", "g", -2, ["l", "j", "h"]),
        (ascii_lowercase, "g", "l", None, ["g", "h", "i", "j", "k"]),
        (ascii_lowercase, "g", None, None, ["a", "b", "c", "d", "e", "f"]),
    ],
)
def test_positive_cases(iterable, start, stop, step, output):
    assert custom_range(iterable, start, stop, step) == output


@pytest.mark.parametrize(
    "iterable, start, stop, step",
    [
        (ascii_lowercase, "0", None, None),
        (ascii_lowercase, "0", "t", None),
        (ascii_lowercase, "t", "10", None),
        (ascii_lowercase, "0", None, None),
        (ascii_lowercase, "0", "10", None),
    ],
)
def test_negative_cases(iterable, start, stop, step):
    with pytest.raises(ValueError) as error:
        custom_range(iterable, start, stop, step)
    assert error.value.args[0] == "objects are not in list"
