"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


from itertools import zip_longest
from typing import Generator


def string_generator(string: str) -> Generator:
    """Generates a string character that hasn't been deleted.

    Arguments:
        string (str): string that can contain `#` characters

    Yields:
        Generator: string character
    """
    counter = 0
    for character in reversed(string):
        if character == "#":
            counter += 1
            continue
        if counter:
            counter -= 1
            continue
        yield character


def backspace_compare(first: str, second: str) -> bool:
    """Returns `True` if the strings are equal, `False` otherwise.

    Arguments:
        first (str): first string
        second (str): second string

    Returns:
        bool: `True` if the strings are equal, `False` otherwise
    """
    for x, y in zip_longest(string_generator(first), string_generator(second)):
        if x != y:
            return False
    return True
