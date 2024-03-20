"""A word w is an anagram of a word v if a permutation of the letters transforming w
into v exists. Given a set of n words of length at most k, we would like to detect all
possible anagrams.
"""
# %%
from collections import defaultdict

def anagram(x):
    tokens = x.split()
    dict_sequences = defaultdict(set)
    for token in tokens:
        sorted_token = "".join(sorted(token))
        dict_sequences[sorted_token].add(token)
    out = []
    for sorted_token, token_set in dict_sequences.items():
        if len(token_set) > 1:
            out.append(token_set)

    return tuple(out)
# %%


def test_example():
    x = (
        "below the car is a rat drinking cider and bending its elbow while this thing "
        "is an arc that can act like a cat which cried during the night caused by pain "
        "in its bowel"
    )
    out = anagram(x)
    expected_out = (
        {"bowel", "below", "elbow"},
        {"arc", "car"},
        {"night", "thing"},
        {"cried", "cider"},
        {"act", "cat"},
    )
    assert all([token_set in expected_out for token_set in out])
    assert all([token_set in out for token_set in expected_out])
# %%
