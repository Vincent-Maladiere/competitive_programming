"""Given an m x n matrix, return all elements of the matrix in spiral order.
"""
# %%
import pytest


def spiral_order(matrix):

    out = []
    n, m = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, 0, 0, 0
    idx = 0
    while True:
        
        for jdx in range(left, m-right):
            out.append(matrix[idx][jdx])
        if len(out) == m * n:
            return out
        top += 1
        
        for idx in range(top, n-bottom):
            out.append(matrix[idx][jdx])
        if len(out) == m * n:
            return out
        right += 1

        for jdx in range(m-1-right, left-1, -1):
            out.append(matrix[idx][jdx])
        if len(out) == m * n:
            return out
        bottom += 1

        for idx in range(n-1-bottom, top-1, -1):
            out.append(matrix[idx][jdx])
        if len(out) == m * n:
            return out
        left += 1

# %%
@pytest.mark.parametrize("matrix, expected", [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    ),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    ),
])
def test_suite(matrix, expected):
    assert spiral_order(matrix) == expected