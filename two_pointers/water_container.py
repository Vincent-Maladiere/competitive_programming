"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith
line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that
the container contains the most water.

Return the maximum amount of water a container can store.
"""
# %%
import pytest


def max_area(height):

    n_height = len(height)
    idx, jdx = 0, n_height - 1
    max_surface = 0
    while idx != jdx:
        surface = (jdx - idx) * min(height[idx], height[jdx])
        print(idx, jdx, surface, max_surface)
        if surface > max_surface:
            max_surface = surface
        if height[idx] <= height[jdx]:
            idx += 1
        else:
            jdx -= 1
    return max_surface

# %%

@pytest.mark.parametrize("height, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([2, 1, 1, 2], 6),
    ([2, 3, 20, 21, 4, 5, 1], 20),
    ([4, 5, 8, 2, 3, 1, 1, 1, 1, 100], 56),
    ([0, 1, 0, 0, 0], 0),
    ([2, 2, 2, 2], 6),
    ([1, 2, 3, 4, 5, 6, 7], 12),
    ([1, 2, 3, 4, 3, 2, 1], 8),
])
def test_suite(height, expected):
    assert max_area(height) == expected