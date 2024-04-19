"""
You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j].

Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].
"""
# %%
import pytest

def jump(nums):

    n_steps = 0
    n_nums = len(nums)
    pos = 0
    while pos < n_nums - 1:
        candidates = nums[pos]
        
        best_score, best_candidate = 0, 0
        for candidate in range(1, candidates+1):
            idx = pos + candidate
            
            if idx == n_nums - 1:
                best_candidate = candidate
                break
            
            score = nums[idx] + candidate
            if score > best_score:
                best_candidate = candidate
                best_score = score
        
        pos += best_candidate
        n_steps += 1

    return n_steps


# %%

@pytest.mark.parametrize("nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1, 1, 1, 1, 1], 4),
        ([3, 2, 1, 3, 2, 1], 2),
        ([1, 1, 2, 1, 1], 3),
        ([2, 1], 1),
        ([1, 2, 3], 2),
        ([1, 2, 1, 1, 1], 3)
    ]
)
def test_case(nums, expected):
    assert expected == jump(nums)
