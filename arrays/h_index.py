"""
Given an array of integers citations where citations[i] is the number of citations
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as
the maximum value of h such that the given researcher has published at least h papers
that have each been cited at least h times.
"""
# %%
import pytest

def h_index(citations):

    citations = sorted(citations, reverse=True)
    n_citations = len(citations)
    
    for idx in range(n_citations):
        if citations[idx] < idx + 1:
            return idx

    return n_citations

 
# %%
@pytest.mark.parametrize("citations, expected", [
    ([2, 2, 2, 2], 2),
    ([2, 5, 0, 1, 6, 7, 3], 3),
    ([0], 0),
    ([1], 1),
])
def test_case(citations, expected):
    assert expected == h_index(citations)