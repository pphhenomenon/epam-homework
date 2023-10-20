from collections import defaultdict
from itertools import product
from typing import List


def check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:
    """Computes how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero."""

    n = len(a)

    _dict = defaultdict(int)

    for j in range(n):
        for i in range(n):
            t = a[i] + b[j]
            _dict[t] += 1

    count = 0

    for j in range(n):
        for i in range(n):
            t = -(c[i] + d[j])
            count += _dict[t]

    return count


def check_sum_of_four_other_solution(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:
    a_b_sums = defaultdict(int)
    c_d_sums = defaultdict(int)

    for elements in product(a, b):
        a_b_sums[sum(elements)] += 1
    for elements in product(c, d):
        c_d_sums[sum(elements)] += 1

    return sum(a_b_sums[-sum_] * c_d_sums[sum_] for sum_ in c_d_sums)
