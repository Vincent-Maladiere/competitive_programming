"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# %%
import pytest

def sum3(nums):
    result = []
    nums.sort() 
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]: 
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else: 
                result.append([a , nums[l], nums[r]]) 
                l += 1 
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    return result

# %%


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 0, 0], [[0, 0, 0]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([-2, -1, 0, 1, 2], [[-2, 0, 2], [-1, 0, 1]]),
        ([-2, -1, -1, 0, 1, 2], [[-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]),
        ([-2, -1, -1, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1]]),
        ([-4, -3, -3, -2, 0, 6], [[-4, -2, 6], [-3, -3, 6]]),
        ([-6, 0, 2, 3, 3, 4, 6], [[-6, 0, 6], [-6, 2, 4], [-6, 3, 3]]),
    ],
)
def test_suite(nums, expected):
    out = sum3(nums)
    for candidate in out:
        assert candidate in expected
    for expected_ in expected:
        assert expected_ in out