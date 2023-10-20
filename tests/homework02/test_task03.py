import pytest

from homework02.task03 import combinations


@pytest.mark.parametrize(
    "arguments, product",
    [
        (
            [[1, 2], [3, 4]],
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        ),
        (
            [["white", "blue"], ["purple", "yellow"], ["grey", "blue"]],
            [
                ["white", "purple", "grey"],
                ["white", "purple", "blue"],
                ["white", "yellow", "grey"],
                ["white", "yellow", "blue"],
                ["blue", "purple", "grey"],
                ["blue", "purple", "blue"],
                ["blue", "yellow", "grey"],
                ["blue", "yellow", "blue"],
            ],
        ),
    ],
)
def test_positive_cases(arguments, product):
    assert combinations(*arguments) == product
