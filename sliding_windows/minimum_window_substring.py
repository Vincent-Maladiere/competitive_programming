"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the
window.

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""
# %%
import pytest
from collections import Counter


def minWindow(s, t):

    len_s, len_t = len(s), len(t)
    if len_s < len_t:
        return ""
    
    idx, jdx = 0, 0
    counter = Counter(t)
    min_substring = ""
    min_size = float("inf")

    while jdx <= len_s - 1:
        
        ch = s[jdx]
        
        if ch in counter:
            counter[ch] -= 1
    
            while all(v <= 0 for v in counter.values()):
                if (jdx - idx) < min_size:
                    min_size = jdx - idx
                    min_substring = s[idx:jdx+1]

                ch = s[idx]
                if ch in counter:
                    counter[ch] += 1
                idx += 1

        jdx += 1
    
    return min_substring
                


# %%


@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("aaaaaabc", "abc", "abc"),
    ("aaaaaaab", "abc", ""),
    ("abddddddddddc", "abc", "abddddddddddc"),
    ("ab", "b", "b"),
])
def test_suite(s, t, expected):
    assert minWindow(s, t) == expected
# %%
