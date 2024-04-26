"""
There are n children standing in a line.

Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute
the candies to the children.
"""
import pytest
# %%
 
def candy(ratings):

    n_ratings = len(ratings)
    candies = [1 for _ in range(n_ratings)]

    streak = 2
    for idx in range(1, n_ratings):
        if ratings[idx] > ratings[idx-1]:
            candies[idx] = streak
            streak += 1
        else:
            streak = 2
    
    streak = 2
    for idx in range(1, n_ratings):
        if ratings[-idx-1] > ratings[-idx] and streak >= candies[-idx-1]:
            candies[-idx-1] = streak
            streak += 1
        else:
            streak = 2
        
    return sum(candies)


# %%

@pytest.mark.parametrize("ratings, expected", [
    ([5, 5, 3, 1, 4, 0, 2, 3], 15),
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([0, 1, 2, 2, 1, 0], 12),
    ([0, 1, 2, 2, 2, 1, 0], 13),
    ([0, 1, 2, 1, 0], 9),
    ([5, 3, 1, 3, 5], 11),
])
def test_case(ratings, expected):
    assert candy(ratings) == expected