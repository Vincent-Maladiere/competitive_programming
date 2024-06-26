"""
You are given an n x n 2D matrix representing an image, rotate the image
by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
# %%
import pytest


def rotate(m):

    len_m = len(m) - 1

    if len_m == 0:
        return

    for offset in range((len_m + 1) // 2):
        for kdx in range(offset, len_m - offset):

            idx, jdx = offset, kdx
            val = m[idx][jdx]

            # top right
            idx, jdx = kdx, len_m - offset
            val2 = m[idx][jdx]
            m[idx][jdx] = val

            # bottom right
            idx, jdx = len_m - offset, len_m - kdx 
            val = m[idx][jdx]
            m[idx][jdx] = val2

            # bottom left
            idx, jdx = len_m - kdx, offset
            val2 = m[idx][jdx]
            m[idx][jdx] = val

            # top left
            idx, jdx = offset, kdx 
            m[idx][jdx] = val2


# %%

@pytest.mark.parametrize("m, expected", [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],  
    ),
    (
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
    (
        [[1]], [[1]]
    ),
    (
        [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]],
        [[4,33,13,32,12,2],[24,1,14,33,27,29],[1,20,32,32,9,20],[6,7,27,2,25,26],[32,21,22,28,13,16],[34,7,26,14,21,28]],
    )
])
def test_suite(m, expected):
    rotate(m)
    assert m == expected