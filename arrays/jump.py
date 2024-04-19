"""
You are given an integer array nums. You are initially positioned at
the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
# %%
import pytest


def can_jump(nums):

    gas = 0
    for num in nums:
        if gas < 0:
            return False
        elif num > gas:
            gas = num
        gas -= 1

    return True


# %%


@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([2, 3, 1, 1, 4, 0], True),
    ([2, 0, 2, 0], True),
    ([100_001] + [0] * 100_000, True),
    ([0, 1, 2], False),
    ([3, 0, 0, 1, 1, 10, 9, 8, 7, 0, 0, 0, 0, 0], True),
    ([0], True),
    ([2, 0, 0], True),
    ([2, 0, 2, 0, 0], True),
    ([0, 3, 1, 0, 4, 3, 2, 0, 1], False),
])
def test_case(nums, expected):
    assert can_jump(nums) == expected