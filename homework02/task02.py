"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""


from collections import Counter
from typing import Any, List, Tuple


def major_and_minor_elements(array: List[Any]) -> Tuple[Any, Any]:
    most_common = max(set(array), key=array.count)
    least_common = min(set(array), key=array.count)
    return most_common, least_common


def other_solution(array: List[Any]) -> Tuple[Any, Any]:
    frequency = Counter(array).most_common()
    return frequency[0][0], frequency[-1][0]
