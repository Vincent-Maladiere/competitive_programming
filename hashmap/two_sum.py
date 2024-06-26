"""
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.
"""
# %%
import pytest
import numpy as np
import bisect

def twoSum(nums, target):
    indices = np.argsort(nums)
    nums = sorted(nums)
    n_nums = len(nums)
    for idx in range(n_nums):
        complement = target - nums[idx]
        jdx = bisect.bisect(nums, complement) - 1
        if nums[jdx] == complement:
            return [indices[idx], indices[jdx]]
        
# %%
