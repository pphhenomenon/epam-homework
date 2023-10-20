from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    """Returns the maximal sum of subarray with length less or equal to "k"."""

    if not nums:
        raise ValueError("empty array received")

    n = len(nums)

    if k > n or k <= 0:
        raise ValueError("invalid subarray length received")

    sub_sum, res_sum = 0, nums[0]

    for j in range(k):
        sub_sum += nums[j]
        cur_sum = sub_sum
        max_sum = sub_sum
        for i in range(j + 1, n):
            cur_sum += nums[i] - nums[i - j - 1]
            max_sum = max(max_sum, cur_sum)
        res_sum = max(max_sum, res_sum)

    return res_sum
