import pytest

from homework01.task03 import find_maximum_and_minimum


def file_path(file_name: str) -> str:
    return "tests/homework01/sources/{}".format(file_name)


@pytest.mark.parametrize(
    "file_name, min_num, max_num",
    [
        [file_path("a.txt"), 0, 0],
        [file_path("b.txt"), 0, 9],
        [file_path("c.txt"), -9, 0],
        [file_path("d.txt"), -43, 95],
    ],
)
def test_positive_cases(file_name, min_num, max_num):
    assert find_maximum_and_minimum(file_name) == (min_num, max_num)
