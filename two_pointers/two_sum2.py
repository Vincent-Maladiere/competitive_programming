"""
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific target
number.

Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.
"""
# %%
import pytest
from bisect import bisect

def binary_search(arr, target):
    a, b = 0, len(arr) - 1
    while a < b:
        mid = a + (b - a) // 2
        if arr[mid] - target >= 0:
            b = mid
        else:
            a = mid + 1
    return a


def two_sum(numbers, target):
    n_numbers = len(numbers)
    for idx in range(n_numbers):
        complement = target - numbers[idx]
        # jdx = binary_search(numbers, value_to_find)
        jdx = bisect(numbers, complement)
        if numbers[jdx - 1] == complement:
            return [idx+1, jdx]


# %%

@pytest.mark.parametrize("numbers, target, expected", [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
])
def test_suite(numbers, target, expected):
    assert two_sum(numbers, target) == expected