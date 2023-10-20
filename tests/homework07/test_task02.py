import pytest

from homework07.task02 import backspace_compare


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("ab#c", "ad#c"),
        ("a##c", "#a#c"),
    ],
)
def test_backspace_compare_positive_cases(first: str, second: str):
    """Tests the `backspace_compare` function in positive cases.

    Arguments:
        first (str): first string
        second (str): second string
    """
    assert backspace_compare(first, second)


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("a#c", "a#b"),
        ("abc#", "ab#c"),
    ],
)
def test_backspace_compare_negative_cases(first: str, second: str):
    """Tests the `backspace_compare` function in negative cases.

    Arguments:
        first (str): first string
        second (str): second string
    """
    assert not backspace_compare(first, second)
