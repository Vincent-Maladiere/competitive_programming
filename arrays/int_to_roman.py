"""
Given a roman numeral, convert it to an integer.
"""
import pytest
# %%

roman_map = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I",
}

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
    "M": "C",
    "D": "C",
    "C": "X",
    "L": "X",
    "X": "I",
    "V": "I",
}


def int_to_roman(num):
    
    s = ""
    for multiple, symbol in roman_map.items():

        repeats = num // multiple
        s += repeats * symbol
        num -= repeats * multiple

        if symbol != "I":
            sub_symbol = subtract_symbol[symbol]
            sub_value = symbol_map[sub_symbol]
            if num // sub_value in [4, 9]:
                s += sub_symbol
                num += sub_value            

            repeats = num // multiple
            s += repeats * symbol
            num -= repeats * multiple
    
    return s


# %%

@pytest.mark.parametrize("s, expected", [
    (1, "I"),
    (1994, "MCMXCIV"),
    (1999, "MCMXCIX"),
    (58, "LVIII"),
    (1300, "MCCC"),
])
def test_suite(s, expected):
    assert int_to_roman(s) == expected


# %%
