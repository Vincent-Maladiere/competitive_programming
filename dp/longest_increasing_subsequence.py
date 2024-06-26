"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting
some or no elements without changing the order of the remaining elements.

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
# %%
import pytest
from bisect import bisect_left
import numpy as np


def longest_incr(nums):
    """This solution has a time complexity of O(n*log(n)).
    """
    n = len(nums)
    buffer = [-np.inf]
    indices = [None]
    previous = [None] * n
    for idx in range(n):
        if nums[idx] > buffer[-1]:
            previous[idx] = indices[-1]
            buffer.append(nums[idx])
            indices.append(idx)
        else:
            kdx = bisect_left(buffer, nums[idx])
            buffer[kdx] = nums[idx]
            indices[kdx] = idx
            previous[idx] = indices[kdx - 1]
    
    jdx = indices[-1]
    result = []
    while jdx is not None:
        result.append(nums[jdx])
        jdx = previous[jdx]

    return result[::-1]


# %%
@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 4, 5, 3, 9, 7, 9], [1, 2, 4, 5, 7, 9]),
    ([10, 9, 2, 5, 3, 7, 101, 18], [2, 3, 7, 18]),
    ([1, 3, 2, 4, 5], [1, 2, 4, 5]),
])
def test_suite(nums, expected):
    assert longest_incr(nums) == expected