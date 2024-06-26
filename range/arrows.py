"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where
points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different
points along the x-axis.

A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
There is no limit to the number of arrows that can be shot. A shot arrow keeps
traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst
all balloons.
"""
# %%
import pytest


def find_min_arrow_shots(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    out = []
    prev_int = intervals[0]

    for idx in range(1, len(intervals)):
        
        current_int = intervals[idx]
        
        if prev_int[1] >= current_int[0]:
            prev_int[0] = max(prev_int[0], current_int[0])
            prev_int[1] = min(prev_int[1], current_int[1])
        else:
            out.append(prev_int)
            prev_int = current_int
        
    out.append(prev_int)

    return len(out)


# %%

@pytest.mark.parametrize("points, expected", [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[1, 5], [2, 4], [3, 4]], 1),
    ([[1, 2]], 1)
])
def test_suite(points, expected):
    assert find_min_arrow_shots(points) == expected