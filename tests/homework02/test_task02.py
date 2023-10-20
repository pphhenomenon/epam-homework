import pytest

from homework02.task02 import major_and_minor_elements, other_solution


@pytest.mark.parametrize(
    "numbers, most_common, least_common",
    [
        ([3, 2, 3], 3, 2),
        ([2, 2, 1, 1, 1, 2, 2], 2, 1),
        (["a", "a", "b", "a", "b", "c", "a"], "a", "c"),
    ],
)
def test_positive_cases(numbers, most_common, least_common):
    assert major_and_minor_elements(numbers) == (most_common, least_common)
    assert other_solution(numbers) == (most_common, least_common)
