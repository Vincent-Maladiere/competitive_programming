"""
Given a string s, find the length of the longest
substring without repeating characters.
"""
# %%
import pytest

def length_of_longest_substring(s):
    n_text = len(s) - 1
    if n_text == -1:
        return 0

    length = 1
    max_length = 1
    idx, jdx = 0, 0
    while jdx <= n_text - 1:
        if not s[jdx+1] in s[idx:jdx+1]:
            jdx += 1
            length += 1
            if length > max_length:
                max_length = length
        else:
            idx += 1
            length -= 1
            length = max(length, 1)
            jdx = max(jdx, idx)
        
    return max_length


# %%

@pytest.mark.parametrize("s, expected", [
    ("pwwkew", 3),
    ("bbbbb", 1),
    ("abcabcbb", 3),
    ("abcde", 5),
    ("", 0),
    ("a" * 5 * int(1e4), 1),
    ("abcde" * int(1e4), 5),
])
def test_suite(s, expected):
    assert length_of_longest_substring(s) == expected

# %%
