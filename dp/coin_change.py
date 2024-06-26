"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
# %%
import pytest

def check_min_coins(coins, amount):
    """This solution is only useful to test in a O(n) time complexity \
    if the amount can be reached using the coins at our disposal.

    It can't guarantee to return the minimum number of coins. Take the following example:
    nums = [1, 3, 3, 4] and amount = 6.
    This function returns 3 (4 + 1 + 1), whereas the optimal solution is 2 (3 + 3).
    """
    coins = sorted(coins, reverse=True)
    total = 0
    for coin in coins:
        total += amount // coin
        amount = amount % coin
        if amount == 0:
            return total
    return -1


def moneyback_dyn(coins, amount):
    n = len(coins)
    least_coins = [[float('inf')] * (amount + 1) for _ in range(n)]

    for sub_amount in range(amount + 1): 
        if sub_amount % coins[0] == 0: 
            least_coins[0][sub_amount] = sub_amount / coins[0]

    for i in range(1, n): 
        for j in range(amount + 1):
            least_coins[i][j] = least_coins[i - 1][j] 
            if coins[i] <= j: 
                if least_coins[i][j - coins[i]] + 1 < least_coins[i][j]:
                    least_coins[i][j] = least_coins[i][j - coins[i]] + 1
    
    chosen = [0] * n
    j = amount
    i = n - 1
    while j > 0 and i >= 0: 
        if j >= coins[i]:
            if least_coins[i][j - coins[i]] + 1 == least_coins[i][j]: 
                chosen[i] += 1 
                j -= coins[i] 
                continue 
        i -= 1
    if j != 0:
        return -1
    return sum(chosen)


# %%

@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([100, 50, 10], 100, 1),
    ([1] * 100, 100, 100),
    ([1, 3, 3, 4], 6, 2),
])
def test_suite(coins, amount, expected):
    assert moneyback_dyn(coins, amount) == expected

# %%
