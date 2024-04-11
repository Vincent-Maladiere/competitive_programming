"""
Given an integer array nums and an integer val, remove all occurrences
of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.
"""

# %%

def remove_elements(nums, val):
    k = 0
    while val in nums:
        idx = nums.index(val)
        nums.pop(idx)
        k += 1
    return k



# %%

def test_case_1():
    nums = [3, 2, 2, 3]
    val = 3
    k = remove_elements(nums, val)
    expected_out = [2, 2]
    assert k == len(expected_out)
    assert expected_out == nums


def test_case_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = remove_elements(nums, val)
    expected_out = [0, 1, 4, 0, 3]
    assert k == len(expected_out)
    assert expected_out == nums