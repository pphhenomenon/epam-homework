"""  # noqa: E501
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


from functools import reduce


def is_armstrong(number: int) -> bool:
    """The function checks if a number is an Armstrong number.

    :param number: number to check
    :type number: int

    :return: the result of checking
    :rtype: bool
    """
    digits = tuple(map(lambda i: int(i), str(number)))
    powers = map(lambda i: pow(i, len(digits)), digits)
    return reduce(lambda a, b: a + b, powers) == number
