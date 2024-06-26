"""
Given a roman numeral, convert it to an integer.
"""
import pytest
# %%

symbol_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

subtract_symbol = {
    "I": ["V", "X"],
    "X": ["L", "C"],
    "C": ["D", "M"],
}


def roman_to_int(s):
    
    n_ch = len(s)
    total = 0
    minus = 0

    for idx in range(n_ch):
        # sub
        if (
            s[idx] in subtract_symbol
            and idx + 1 < n_ch
            and s[idx+1] in subtract_symbol[s[idx]]
        ):
            minus = symbol_map[s[idx]]
        else:
            total += symbol_map[s[idx]] - minus
            minus = 0
    
    return total

# %%

@pytest.mark.parametrize("s, expected", [
    ("I", 1),
    ("IV", 4),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("MCCC", 1300)
])
def test_suite(s, expected):
    assert roman_to_int(s) == expected


# %%
