"""
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.
"""
import pytest

# %%
def trap(height):

    n_height = len(height)
    water = [0 for _ in range(n_height)]

    highest = 0
    for idx in range(n_height):
        if height[idx] >= highest:
            highest = height[idx]
        water[idx] = highest - height[idx]

    highest = 0
    for idx in range(n_height-1, -1, -1):
        if height[idx] >= highest:
            highest = height[idx]
        water[idx] = min(water[idx], highest - height[idx])
    
    return sum(water)


# %%

@pytest.mark.parametrize("height, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([1], 0),
    ([1, 0, 0, 1], 2),
    ([1, 2, 3, 2, 1], 0),
    ([3, 2, 2, 2], 0),
    ([1, 0, 1, 0, 1], 2)
])
def test_suite(height, expected):
    assert trap(height) == expected