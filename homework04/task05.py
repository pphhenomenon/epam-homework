"""  # noqa: E501
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
[1, 2, 'fizz', 4, 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""


from typing import Generator


def fizzbuzz(n: int) -> Generator[int, None, None]:
    """Returns a generator that yields "n" FizzBuzz numbers.  # noqa: E501

    >>> list(fizzbuzz(5))
    [1, 2, 'fizz', 4, 'buzz']

    >>> list(fizzbuzz(10))
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz']

    >>> list(fizzbuzz(15))
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']
    """
    for i in range(1, n + 1):
        yield "fizz" * (not i % 3) + "buzz" * (not i % 5) or i
