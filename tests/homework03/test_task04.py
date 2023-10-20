import pytest

from homework03.task04 import is_armstrong


@pytest.mark.parametrize(
    "number",
    [
        153, 370, 407,
        1634, 8208, 9474,
    ],
)
def test_positive_cases(number):
    """Tests Armstrong numbers.

    :param number: number to check
    :type number: int

    :return: the truth of expression
    :rtype: bool
    """
    assert is_armstrong(number)


@pytest.mark.parametrize(
    "number",
    [
        450, 531, 619,
        1044, 1611, 8009,
    ],
)
def test_negative_cases(number):
    """Tests not Armstrong numbers.

    :param number: number to check
    :type number: int

    :return: the truth of expression
    :rtype: bool
    """
    assert not is_armstrong(number)
