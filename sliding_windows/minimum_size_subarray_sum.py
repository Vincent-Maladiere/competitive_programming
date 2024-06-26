"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.

If there is no such subarray, return 0 instead.
"""
# %%
import pytest

def min_subarray_length(target, nums):
    n_nums = len(nums)
    idx, jdx = 0, 0
    min_length = 0
    total = nums[0]

    while idx != n_nums:
        
        if total >= target:
            if (jdx - idx) < min_length or min_length == 0:
                min_length = jdx - idx + 1
                print(idx, jdx)

            total -= nums[idx]
            idx += 1
            jdx = max(idx, jdx)

        else:
            if jdx == n_nums - 1:
                break
            jdx += 1
            total += nums[jdx]

    return min_length


min_subarray_length(11, [1, 2, 3, 4, 5])


# %%
@pytest.mark.parametrize("target, nums, expected", [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1], 0),
    (5, [2, 2, 2], 0),
    (5, [1, 1, 1, 1, 1], 5),
    (11, [1, 2, 3, 4, 5], 3),
])
def test_suite(target, nums, expected):
    assert min_subarray_length(target, nums) == expected