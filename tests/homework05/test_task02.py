import pytest

from homework05.task02 import custom_sum


def test_doc_print():
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__doc__ == ("This function can sum any "
                                  "objects which have __add__")


def test_name_print():
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__name__ == "custom_sum"


@pytest.mark.parametrize(
    "args, result",
    [
        ((1, 2, 3, 4), 10),
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
    ]

)
def test_result_print(args, result):
    assert custom_sum(*args) == result
