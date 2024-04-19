"""
You are given an integer array prices where prices[i] is the price of a given stock
on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""
# %%
import pytest


def max_profit(prices):

    profit = 0
    buy = prices[0]

    for idx in range(1, len(prices)):
        if prices[idx] > buy:
            profit += prices[idx] - buy
        buy = prices[idx]

    return profit


@pytest.mark.parametrize("prices, expected", [
    ([7,1,5,3,6,4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
])
def test_case(prices, expected):
    assert max_profit(prices) == expected

