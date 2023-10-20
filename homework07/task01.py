"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""


from typing import Any

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
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """Returns the number of occurrences of the element in the tree.

    Arguments:
        tree (dict): Dictionary (tree)
        element (Any): Target

    Returns:
        int: The number of occurrences of the element in the tree
    """
    counter = 0

    if isinstance(tree, dict):
        if element in tree.values():
            counter += 1
        for branch in tree.values():
            counter += find_occurrences(branch, element)

    if isinstance(tree, (set, list, tuple)):
        counter += tree.count(element)
        for sequence in tree:
            counter += find_occurrences(sequence, element)

    return counter
