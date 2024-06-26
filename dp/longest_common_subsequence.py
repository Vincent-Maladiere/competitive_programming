"""
Given two strings text1 and text2, return the length of their longest common
subsequence.

If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order
of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""
# %%
import pytest


def longest_common(text1, text2):
    """Time complexity is O(n*m).
    """

    n, m = len(text1), len(text2)
    A = [[0 for jdx in range(m+1)] for idx in range(n+1)]
    for idx in range(n):
        for jdx in range(m):
            if text1[idx] == text2[jdx]:
                A[idx + 1][jdx + 1] = A[idx][jdx] + 1
            else:
                A[idx + 1][jdx + 1] = max(A[idx][jdx + 1], A[idx + 1][jdx])
    
    idx, jdx = n, m
    result = []    
    while A[idx][jdx] > 0:
        if A[idx][jdx] == A[idx - 1][jdx]:
            idx -= 1
        elif A[idx][jdx] == A[idx][jdx - 1]:
            jdx -= 1
        else:
            idx -= 1
            jdx -= 1
            result.append(text1[idx])

    return "".join(result[::-1])


# %%
@pytest.mark.parametrize("text1, text2, expected", [
    ("gac", "agcat", "ga"),
])
def test_suite(text1, text2, expected):
    assert longest_common(text1, text2) == expected

# %%
