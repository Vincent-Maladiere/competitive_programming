"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates
in-place such that each unique element appears at most twice. The relative order of
the elements should be kept the same.
"""

# %%
from collections import Counter


def remove_duplicates(nums):
    idx = 0
    seen = Counter()
    while idx < len(nums):
        value = nums[idx]
        if seen[value] <= 1:
            seen[value] += 1
            idx += 1
        else:
            nums.pop(idx)
    return len(nums)


# %%

def test_case_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]


def test_case_2():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates(nums)
    assert k == 7
    assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]