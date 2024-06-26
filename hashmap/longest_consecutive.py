# %%
import pytest
from collections import Counter


def longestConsecutive(nums):
    longest = 0
    intervals = dict()
    right_to_left = dict()
    left_to_right = dict()
    
    for idx in range(len(nums)):
        num = nums[idx]
        if num not in intervals:
            
            has_left = num - 1 in right_to_left
            has_right = num + 1 in left_to_right
            
            if has_left and has_right:
                left = right_to_left[num - 1]
                right = left_to_right[num + 1]
                length = 1 + intervals[num - 1] + intervals[num + 1]
                intervals[left] = length
                intervals[right] = length
                left_to_right[left] = right
                right_to_left[right] = left

            elif has_left:
                left = right_to_left[num - 1]
                length = intervals[num - 1] + 1
                intervals[left] = length
                intervals[num] = length

                right_to_left[num] = left
                left_to_right[left] = num

            elif has_right:
                right = left_to_right[num + 1]
                length = intervals[num + 1] + 1
                intervals[right] = length
                intervals[num] = length

                left_to_right[num] = right
                right_to_left[right] = num

            else:
                left_to_right[num] = num
                right_to_left[num] = num
                length = 1
                intervals[num] = length

            if length > longest:
                longest = length

            print(num)
            print("=>", left_to_right)
            print("<=", right_to_left)
            print(intervals)

    return longest


# %%

@pytest.mark.parametrize("nums, expected", [
    ([4, 1, 3, 2, 0], 5),
    ([0, 1, 2, 3, 4], 5),
    ([4, 3, 2, 1, 0], 5),
    ([0], 1),
    ([], 0),
    ([0, 1, 2, 4, 5, 3], 6),
    ([0, 1, 2, 4, 5, 3, -1, 6], 8),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
])
def test_suite(nums, expected):
    assert longestConsecutive(nums) == expected
# %%
