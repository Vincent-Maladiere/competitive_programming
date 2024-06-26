"""Zigzag Conversion.
"""
import pytest

# %%
def create_grid(s, numRows):
    
    n_ch = len(s)
    rows = [[] for _ in range(numRows)]
    idx = 0

    while True:

        for row_idx in range(numRows):
            ch = s[idx]
            rows[row_idx].append(ch)
            idx += 1
            if idx == n_ch:
                return rows
        
        for row_idx in range(numRows-2, 0, -1):
            for jdx in range(numRows-1, -1, -1):
                ch = ""
                if jdx == row_idx:
                    ch = s[idx]
                    idx += 1
                rows[jdx].append(ch)
                if idx == n_ch:
                    return rows


def convert(s, numRows):
    grid = create_grid(s, numRows)
    s = ""
    for row in grid:
        s += "".join(row)
    return s



# %%

@pytest.mark.parametrize("s, numRows, expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A")
])
def test_suite(s, numRows, expected):
    assert convert(s, numRows) == expected