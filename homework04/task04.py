"""  # noqa: E501
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""


from typing import List


def fizzbuzz(n: int) -> List[int]:
    """Returns "n" FizzBuzz numbers.  # noqa: E501

    >>> fizzbuzz(5)
    [1, 2, 'fizz', 4, 'buzz']

    >>> fizzbuzz(10)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']

    >>> fizzbuzz(15)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    """
    numbers = []

    for i in range(1, n + 1):
        numbers.append("fizz" * (not i % 3) + "buzz" * (not i % 5) or i)

    return numbers
