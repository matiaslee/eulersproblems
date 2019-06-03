#!/usr/bin/env python3

# Problem 26: Reciprocal Cycles - https://projecteuler.net/problem=26
# By Matias D. Lee
# 
# A unit fraction contains 1 in the numerator. The decimal representation 
# of the unit fractions with denominators 2 to 10 are given:
# 
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1 
# 
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
# in its decimal fraction part.

def calc_remainders(d):
    """ 
    Function returns a pair (rs, r) where rs is a list of remainders of dividing (1/d) and 
    r != 0 is the first remainder that is repeated. If r==0 there is no recurring cycle. 

    >>> calc_remainders(4)
    ([1, 2], 0)

    >>> calc_remainders(10)
    ([1], 0)

    >>> calc_remainders(3)
    ([1], 1)

    >>> calc_remainders(6)
    ([1, 4], 4)

    >>> calc_remainders(7)
    ([1, 3, 2, 6, 4, 5], 1)

    """

    next_remainder = lambda remainder : (remainder * 10) % d
    remainders = [1]
    nr = next_remainder(1)
    while nr not in remainders and nr > 0:
        remainders.append(nr)
        nr = next_remainder(nr)
    return remainders, nr

def recurring_cycle_length(d):
    rs, last_r = calc_remainders(d)
    length = 0
    if last_r > 0:
        i = rs.index(last_r)
        length  = len(rs) - i
    
    return length 

def solver(N):
    """
    >>> solver(10)
    7
    """
    answer = 2
    rcl = recurring_cycle_length(answer)
    for i in range(3, N+1):
        rcl_i = recurring_cycle_length(i)
        if  rcl_i > rcl:
            answer, rcl = i, rcl_i
    return answer

if __name__ == '__main__':
    print(solver(999))
    