"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""
# %%
import pytest

def max_profit(prices):

    buy = prices[0]
    profit = 0

    for idx in range(1, len(prices)):
        if prices[idx] < buy:
            buy = prices[idx]
        elif prices[idx] - buy > profit:
            profit = prices[idx] - buy

    return profit


# %%

@pytest.mark.parametrize("prices, expected_profit", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 2, 2, 2], 0),
    ([3, 2, 1] + [0] * 10_000, 0)
])
def test_case(prices, expected_profit):
    profit = max_profit(prices)
    assert expected_profit == profit





# %%
