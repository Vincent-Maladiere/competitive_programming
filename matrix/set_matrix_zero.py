"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place.
"""
# %%
import pytest


def set_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    
    has_first_row_zero = has_first_col_zero = False
    # set indices in first row and first col
    for idx in range(m):
        for jdx in range(n):
            if matrix[idx][jdx] == 0:
                matrix[0][jdx] = 0
                matrix[idx][0] = 0
                if idx == 0:
                    has_first_row_zero = True
                if jdx == 0:
                    has_first_col_zero = True

    # set values to zero
    for idx in range(1, m):
        if matrix[idx][0] == 0:
            for jdx in range(1, n):
                matrix[idx][jdx] = 0
    
    for jdx in range(1, n):
        if matrix[0][jdx] == 0:
            for idx in range(1, m):
                matrix[idx][jdx] = 0

    # finish with setting the row and cols indices to 0.
    if has_first_row_zero:
        for jdx in range(n):
            matrix[0][jdx] = 0
    
    if has_first_col_zero:
        for idx in range(m):
            matrix[idx][0] = 0


# %%

@pytest.mark.parametrize("matrix, expected", [
    (
        [[1, 1, 1], [1, 0 , 1], [1, 1, 1]],
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
    ),
    (
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
    (
        [[1]], [[1]],
    ),
    (
        [[1, 0]], [[0, 0]],
    ),
])
def test_suite(matrix, expected):
    set_zeros(matrix)
    assert matrix == expected