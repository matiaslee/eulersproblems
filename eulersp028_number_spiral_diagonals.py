#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Problem 28: Quadratic Primes - https://projecteuler.net/problem=28
# By Matias D. Lee. 
# 

# 
# Starting with the number 1 and moving to the right in a clockwise 
# direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?
# 

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31


def solver(spiral_size):
    """ 
    >>> solver(3)
    25

    >>> solver(5)
    101
    
    >>> solver(7)
    261

    """
    square_length = 0
    diagonal_sum = 1
    last_value = 1
    size = 1

    while size < spiral_size:
        square_length += 2
        vals_to_sum = [last_value + i * square_length for i in range(1,5)]
        diagonal_sum += sum(vals_to_sum)
        last_value = vals_to_sum[-1]
        size += 2
    return diagonal_sum

if __name__ == '__main__':
    print(solver(1001))
