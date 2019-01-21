#!/usr/bin/env python3

#
# Problem 19: Longest Collatz sequence - https://projecteuler.net/problem=19
# By Matias D. Lee. 
#
# 
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
# 

sum_of_square = lambda x: (x * (x + 1) * (2*x + 1)) / 6
square_of_sum = lambda x: ((x * (x+1))/2)**2 

def solver(n):
    """
    >>> solver(10)
    2640
    """
    return int(square_of_sum(n) - sum_of_square(n))

if __name__ == '__main__':
    print(solver(100)) 