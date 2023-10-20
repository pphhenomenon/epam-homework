import pytest

from homework07.task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "def": "RED",
        "complex_key": {
            "key1": "value",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ("element", "result"),
    [
        ("RED", 6),
        ("BLUE", 2),
        ("Python", 0),
    ],
)
def test_find_occurrences(element: str, result: int):
    """Tests the `find_occurrences` function.

    Arguments:
        element (str): Target
        result (int): The number of occurrences of the element in the tree
    """
    assert find_occurrences(example_tree, element) == result
