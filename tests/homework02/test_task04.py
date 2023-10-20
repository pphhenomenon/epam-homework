import pytest

from homework02.task04 import storage


@storage
def plus(a: int, b: int) -> int:
    return a + b


@storage
def product(a: int, b: int) -> int:
    return a * b


@storage
def power(a: int, b: int) -> int:
    return a ** b


@pytest.mark.parametrize(
    "procedure, numbers",
    [
        (plus, (89, 175)),
        (power, (89, 175)),
        (product, (89, 175)),
    ],
)
def test_positive_cases(procedure, numbers):
    a = procedure(*numbers)
    b = procedure(*numbers)
    assert a is b
