import pytest

from homework01.task04 import (check_sum_of_four,
                               check_sum_of_four_other_solution)


@pytest.mark.parametrize(
    "a, b, c, d, ans",
    [
        ([], [], [], [], 0),
        ([0], [0], [0], [0], 1),
        ([2, 1], [2, 5], [1, -2], [-4, 5], 2),
        ([1, 2, 3], [4, 5, 6], [-7, -8, -9], [0, -1, -2], 10),
    ],
)
def test_positive_cases(a, b, c, d, ans):
    assert check_sum_of_four(a, b, c, d) == ans
    assert check_sum_of_four_other_solution(a, b, c, d) == ans
