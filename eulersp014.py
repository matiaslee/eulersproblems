#!/usr/bin/env python3

#
# Problem 14: Longest Collatz sequence - https://projecteuler.net/problem=14
# By Matias D. Lee. 
# 
# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 

import doctest
from operator import itemgetter

C_length = {1 : 1}

def next_collatz(n):
    """
    >>> next_collatz(1)
    

    >>> next_collatz(2)
    1

    >>> next_collatz(5)
    16
    """
    if n==1:
        return None
    elif n % 2 == 0:
        c = n/2
    else:
        c = 3*n + 1
    return int(c)

def collatz_length(n):
    """
    >>> collatz_length(13)
    10
    """
    if n not in C_length:
        C_length[n] = 1 + collatz_length(next_collatz(n))

    return C_length[n] 


def calc_c_lengths(iterable_obj):
    """
    >>> calc_c_lengths(range(1,4))
    [(1, 1), (2, 2), (3, 8)]


    >>> calc_c_lengths(range(1,4,2))
    [(1, 1), (3, 8)]

    >>> calc_c_lengths(range(1,6,2))
    [(1, 1), (3, 8), (5, 6)]
    """
    lengths = []
    for i in iterable_obj:
        lengths.append((i, collatz_length(i)))

    return(lengths)

def p14_solver(n):
    """
    >>> p14_solver(4)
    (3, 8)

    >>> p14_solver(6)
    (3, 8)
    """
    lengths = calc_c_lengths(range(1,n,2))
    m = max(lengths,key=itemgetter(1))
    return m

if __name__ == '__main__':
    print(p14_solver(1000000))
