"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""


from re import split
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Returns a list of 10 longest words consisting from largest
    amount of unique symbols."""

    with open(file=file_path, encoding="unicode_escape") as data:
        text = data.read().replace("-\n", "")
        words = split(r"[ .,;\n]+", text)

    diverse_words = []

    for _ in range(10):
        diverse = max(words, key=lambda word: len(set(word)))
        while diverse in words:
            words.remove(diverse)
        diverse_words.append(diverse)

    return diverse_words


def get_rarest_symbol(file_path: str) -> str:
    """Returns the rarest symbol in the document."""

    with open(file=file_path, encoding="unicode_escape") as data:
        text = data.read().replace("\n", "")

    return min(text, key=text.count)


def count_punctuation_chars(file_path: str) -> int:
    """ "Returns the number of punctuation chars in the document."""

    with open(file=file_path, encoding="unicode_escape") as data:
        text = data.read().replace("-\n", "")
        chars = tuple(char for char in text if char in punctuation)

    return len(chars)


def count_non_ascii_chars(file_path: str) -> int:
    """Returns the number of non ascii chars in the document."""

    with open(file=file_path, encoding="unicode_escape") as data:
        chars = tuple(char for char in data.read() if not char.isascii())

    return len(chars)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Returns the most common non ascii char in the document."""

    with open(file=file_path, encoding="unicode_escape") as data:
        chars = tuple(char for char in data.read() if not char.isascii())

    return max(chars, key=chars.count)
