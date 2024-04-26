"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
"""
import pytest

# %%
def product(nums):
    n_nums = len(nums)
    out = [1 for _ in range(n_nums)]
    
    running_prod = 1
    for idx in range(n_nums-1):
        running_prod *= nums[idx]
        out[idx+1] = running_prod

    running_prod = 1
    for idx in range(n_nums-1):
        running_prod *= nums[-1-idx]
        out[-2-idx] *= running_prod

    return out


# %%

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1], [1]),
])
def test_case(nums, expected):
    assert expected == product(nums)