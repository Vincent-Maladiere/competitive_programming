"""
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the
ith interval and intervals is sorted in ascending order by starti.

You are also given an interval newInterval = [start, end] that represents
the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
# %%
import pytest

def insert(intervals, newInterval):
    if len(intervals) == 0:
        return newInterval

    new_left, new_right = newInterval
    out = []
    idx = 0
    n_intervals = len(intervals)
    
    while idx <= n_intervals - 1 and new_left > intervals[idx][1]:
        out.append(intervals[idx])
        idx += 1

    if idx <= n_intervals - 1: 
        new_left = min(new_left, intervals[idx][0])

    while idx <= n_intervals - 1 and new_right >= intervals[idx][0]:
        new_right = max(new_right, intervals[idx][1])
        idx += 1

    out.append([new_left, new_right])

    while idx <= n_intervals - 1:
        out.append(intervals[idx])
        idx += 1

    return out


# %%

@pytest.mark.parametrize("intervals, newInterval, expected", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([], [1, 2], [[1, 2]]),
    ([[1, 2]], [3, 4], [[1, 2], [3, 4]]),
    ([[3, 4]], [1, 2], [[1, 2], [3, 4]]),
    ([[1, 2], [3, 4]], [2, 3], [[1, 4]]),
    ([[2, 3], [4, 5], [6, 9]], [1, 10], [[1, 10]]),
])
def test_suite(intervals, newInterval, expected):
    assert insert(intervals, newInterval) == expected