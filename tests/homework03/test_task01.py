import pytest

from homework03.task01 import cache


@pytest.mark.parametrize("number", [2, 5, 7])
def test_greeting(number: int):
    """Tests the greeting function.

    :param number: the number of times the function returns the cached value
    :type number: int

    :return: the truth of an expression
    :rtype: bool
    """
    times_invoked, times_needed = 0, 2

    @cache(times=number)
    def greeting(name: str) -> str:
        """The function takes the person's name and returns the greeting.

        :param name: the name of the person to be greeted
        :type name: str

        :return: greeting
        :rtype: str
        """
        nonlocal times_invoked

        times_invoked += 1

        return "Hello, {}".format(name)

    assert not times_invoked
    for _ in range(number + times_needed):
        assert greeting("GitHub") == "Hello, GitHub"
    assert times_invoked == times_needed


@pytest.mark.parametrize("number", [2, 5, 7])
def test_product(number: int):
    """Tests the product function.

    :param number: the number of times the function returns the cached value
    :type number: int

    :return: the truth of an expression
    :rtype: bool
    """

    times_invoked, times_needed = 0, 2

    @cache(times=number)
    def product(a: int, b: int) -> int:
        """The function takes 2 integers and returns their product.

        :param a: multiplier
        :type a: int
        :param b: multiplier
        :type b: int

        :return: product
        :rtype: int
        """
        nonlocal times_invoked

        times_invoked += 1

        return a * b

    assert not times_invoked
    for _ in range(number + times_needed):
        assert product(17, 93) == 1581
    assert times_invoked == times_needed
