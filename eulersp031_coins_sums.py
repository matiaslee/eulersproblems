#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Problem 29: Coins sums - https://projecteuler.net/problem=31
# By Matias D. Lee. 
# 

# 
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# 
# It is possible to make £2 in the following way:
# 
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# 
# How many different ways can £2 be made using any number of coins?
# 
# Note: this solution can replace `dict` by `np.array` in order to be 
#       shorter and more efficient.
#

from collections import defaultdict

def sums_of_a_coin(coin_value, target_sum):
    """
    >>> sums_of_a_coin(2, 6)
    defaultdict(<class 'int'>, {2: 1, 4: 1, 6: 1})

    >>> sums_of_a_coin(2, 7)
    defaultdict(<class 'int'>, {2: 1, 4: 1, 6: 1})

    >>> sums_of_a_coin(200, 200)
    defaultdict(<class 'int'>, {200: 1})

    """
    n = int(target_sum/coin_value)
    sums = defaultdict(int)
    for i in range(1, n+1):
        sums[i * coin_value] = 1

    return sums

def sums_mixer(one_sums, other_sums, target_sum):
    """
    >>> sums_mixer({2: 1, 4: 1, 6: 1}, {2: 1, 4: 1}, 1000)
    defaultdict(<class 'int'>, {2: 2, 4: 3, 6: 3, 8: 2, 10: 1})

    >>> sums_mixer({2: 1, 4: 1, 6: 1}, {2: 1, 4: 1}, 9)
    defaultdict(<class 'int'>, {2: 2, 4: 3, 6: 3, 8: 2})

    >>> sums_mixer({2: 1, 4: 1, 6: 1}, {5: 1}, 13)
    defaultdict(<class 'int'>, {2: 1, 4: 1, 6: 1, 5: 1, 7: 1, 9: 1, 11: 1})

    """

    sums = defaultdict(int)

    # mix current sums
    one_keys = set(one_sums.keys())
    other_keys = set(other_sums.keys())
    intersection = one_keys & other_keys
    one_keys_only = one_keys - intersection
    other_keys_only = other_keys - intersection

    for k in list(intersection):
        sums[k] = one_sums[k] + other_sums[k]

    for k in list(one_keys_only):
        sums[k] = one_sums[k] 

    for k in list(other_keys_only):
        sums[k] = other_sums[k]

    # create new sums, adding between sums:
    for k1 in one_sums:
        for k2 in other_sums:
            if k1 + k2 <= target_sum:
                sums[k1 + k2] += one_sums[k1] * other_sums[k2]
    
    return sums

def solver(target_sum=200):
    """
    >>> solver(3)
    2

    >>> solver(5)
    4

    >>> solver(6)
    5
    """
    sums_of_coins = [sums_of_a_coin(i, target_sum) for i in [1, 2, 5, 10, 20, 50, 100, 200]]
    current_sums = sums_of_coins[0]
    for next_sums in sums_of_coins[1:]:
        current_sums = sums_mixer(current_sums, next_sums, target_sum) 

    return current_sums[target_sum]

if __name__== "__main__":
    print(solver())
