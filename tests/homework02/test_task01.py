import pytest

from homework02.task01 import (count_non_ascii_chars, count_punctuation_chars,
                               get_longest_diverse_words,
                               get_most_common_non_ascii_char,
                               get_rarest_symbol)


def file_path(file_name: str) -> str:
    return "tests/homework02/sources/{}".format(file_name)


words = [
    [
        "vorgebahnte", "Betrachtung",
        "hinausführen", "bedenklichen",
        "verbirgt", "vielmehr",
        "Waldgang", "hinter",
        "Ausflug", "gefaßt",
    ],
    [
        'Gefährdung', 'Inzwischen',
        'Großväter', 'handelt',
        'Kernfrage', 'freilich',
        'verändert', 'bringt',
        'Fragen', 'ähnlich'
    ],
    [
        'praktische', 'Entwicklung',
        'überhaupt', 'Forschung',
        'Gesellschaft', 'Frauenfrage',
        'wenngleich', 'Welträtsel',
        'Optimismus', 'Probleme'
    ],
    [
        'Außenpolitik', 'beschäftigen',
        'verschwinden', 'Inzwischen',
        'Gesellschaft', 'Natürlich',
        'überhaupt', 'entwickelt',
        'soziale', 'klassenlose'
    ]
]

symbols = ["W", "E", "N", "I"]

numbers = [5, 6, 9, 9, 10, 8, 7, 9]

not_ascii = ["ü", "ä", "ß", "ß"]


@pytest.mark.parametrize(
    "file_name, diverse_words",
    [
        [file_path("a.txt"), words[0]],
        [file_path("b.txt"), words[1]],
        [file_path("c.txt"), words[2]],
        [file_path("d.txt"), words[3]],
    ],
)
def test_get_longest_diverse_words(file_name, diverse_words):
    assert get_longest_diverse_words(file_name) == diverse_words


@pytest.mark.parametrize(
    "file_name, rarest_symbol",
    [
        [file_path("a.txt"), symbols[0]],
        [file_path("b.txt"), symbols[1]],
        [file_path("c.txt"), symbols[2]],
        [file_path("d.txt"), symbols[3]],
    ],
)
def test_get_rarest_symbol(file_name, rarest_symbol):
    assert get_rarest_symbol(file_name) == rarest_symbol


@pytest.mark.parametrize(
    "file_name, punctuation_number",
    [
        [file_path("a.txt"), numbers[0]],
        [file_path("b.txt"), numbers[2]],
        [file_path("c.txt"), numbers[4]],
        [file_path("d.txt"), numbers[6]],
    ],
)
def test_count_punctuation_chars(file_name, punctuation_number):
    assert count_punctuation_chars(file_name) == punctuation_number


@pytest.mark.parametrize(
    "file_name, non_ascii_number",
    [
        [file_path("a.txt"), numbers[1]],
        [file_path("b.txt"), numbers[3]],
        [file_path("c.txt"), numbers[5]],
        [file_path("d.txt"), numbers[7]],
    ],
)
def test_count_non_ascii_chars(file_name, non_ascii_number):
    assert count_non_ascii_chars(file_name) == non_ascii_number


@pytest.mark.parametrize(
    "file_name, most_common_non_ascii",
    [
        [file_path("a.txt"), not_ascii[0]],
        [file_path("b.txt"), not_ascii[1]],
        [file_path("c.txt"), not_ascii[2]],
        [file_path("d.txt"), not_ascii[3]],
    ],
)
def test_get_most_common_non_ascii_char(file_name, most_common_non_ascii):
    assert get_most_common_non_ascii_char(file_name) == most_common_non_ascii
