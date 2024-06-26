"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum
of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""
# %%
from collections import Counter

def is_happy(n):
    digits = str(n)
    seen = Counter()
    while True:
        square_sum = sum([int(d) ** 2 for d in digits])
        if square_sum == 1:
            return True
        digits = str(square_sum)
        if seen[digits] > 0:
            return False
        else:
            seen[digits] += 1
    
# %%
