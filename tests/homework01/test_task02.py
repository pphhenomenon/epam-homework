import pytest

from homework01.task02 import check_fibonacci, check_fibonacci_other_solution


@pytest.mark.parametrize(
    "data",
    [
        [0],
        [1],
        [5],
        [34],
        [0, 1],
        [1, 1],
        [5, 8],
        [8, 13, 21],
        [13, 21, 34, 55, 89],
        [0, 1, 1, 2, 3, 5, 8, 13],
    ],
)
def test_positive_cases(data):
    assert check_fibonacci(data)
    assert check_fibonacci_other_solution(data)


@pytest.mark.parametrize(
    "data",
    [
        "0",
        "1",
        "5",
        "34",
        "0, 1",
        "1, 1",
        "5, 8",
        "8, 13, 21",
        "13, 21, 34, 55, 89",
        "0, 1, 1, 2, 3, 5, 8, 13",
    ],
)
def test_positive_cases_strings(data):
    assert check_fibonacci(data)


@pytest.mark.parametrize(
    "data",
    [
        [4],
        [7],
        [9],
        [35],
        [0, 0],
        [3, 3],
        [5, 7],
        [5, 8, 23],
        [5, 8, 23, 21, 55],
        [0, 1, 1, 0, 3, 8, 21, 89],
    ],
)
def test_negative_cases(data):
    assert not check_fibonacci(data)
    assert not check_fibonacci_other_solution(data)


@pytest.mark.parametrize(
    "data",
    [
        "4",
        "7",
        "9",
        "35",
        "0, 0",
        "3, 3",
        "5, 7",
        "5, 8, 23",
        "5, 8, 23, 21, 55",
        "0, 1, 1, 0, 3, 8, 21, 89",
    ],
)
def test_negative_cases_strings(data):
    assert not check_fibonacci(data)
