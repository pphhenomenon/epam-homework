import pytest

from homework01.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "nums, k, total",
    [
        ([-11, -100, -5, -1, -17], 5, -1),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 24),
    ],
)
def test_positive_cases(nums, k, total):
    assert find_maximal_subarray_sum(nums, k) == total


@pytest.mark.parametrize(
    "nums, k",
    [
        ([], 5),
        ([1, 3, -1, -3, 5, 3, 6, 7], 0),
        ([1, 4, 2, 10, 2, 3, 1, 0, 20], -7),
    ],
)
def test_negative_cases(nums, k):
    with pytest.raises(ValueError):
        find_maximal_subarray_sum(nums, k)
