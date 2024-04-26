"""
There are n gas stations along a circular route, where the amount of gas
at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to
travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

If there exists a solution, it is guaranteed to be unique.
"""
# %%
import pytest

def can_complete(gas, cost):
    diff = [g - c for g, c in zip(gas, cost)]
    total = sum(diff)
    if total < 0:
        return -1

    start_idx = None
    total = 0
    for idx, d in enumerate(diff):
        total += d
        if total < 0:
            total = 0
            start_idx = None
        elif start_idx is None:
            start_idx = idx

    return start_idx


gas, cost = [6, 1, 4, 3, 5], [3, 8, 2, 4, 2] 
can_complete(gas, cost)


# %%

@pytest.mark.parametrize("gas, cost, expected", [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([10, 0, 0, 0], [1, 1, 1, 1], 0),
    ([1], [1], 0),
    ([1], [2], -1),
    ([1, 0, 2], [1, 1, 1], 2),
    ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ([1, 2], [2, 1], 1),
    ([6, 1, 4, 3, 5], [3, 8, 2, 4, 2], 2),

])
def test_suite(gas, cost, expected):
    assert expected == can_complete(gas, cost)
