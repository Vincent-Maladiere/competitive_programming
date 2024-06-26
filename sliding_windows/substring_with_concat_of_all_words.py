"""
You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of
any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is
not a concatenated string because it is not the concatenation of any permutation
of words.

Return an array of the starting indices of all the concatenated substrings in s.
You can return the answer in any order.
"""
# %%
import pytest
from collections import Counter


def findSubstring(s, words):
    len_w, len_s = len(words[0]), len(s)
    if len_w > len_s:
        return []

    start_indices = []

    for offset in range(len_w):
        idx = offset        
        jdx = offset
        counter = Counter(words)
        queue_words = []
        
        while jdx <= len_s - len_w:

            word = s[jdx:jdx+len_w]

            if counter[word] > 0:
                counter[word] -= 1
                queue_words.append(word)
                jdx += len_w
                
                if not counter.total():
                    start_indices.append(idx)
                else:
                    continue 
            
            idx += len_w
            jdx = max(idx, jdx)
            if len(queue_words) > 0:
                word = queue_words.pop(0)
                counter[word] += 1

    return start_indices


# %%
@pytest.mark.parametrize("s, words, expected", [
    ("barfoothefoobarman", ["bar", "foo"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
    ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8]),
    ("barfoofoobarthefoobarman", ["bar","foo","the"], [6, 9, 12]),
    ("ababababab", ["ababa","babab"], [0])
])
def test_suite(s, words, expected):
    assert findSubstring(s, words) == expected