#!/usr/bin/env python3

#
# Problem 1: Multiples of 3 and 5 - https://projecteuler.net/problem=1
# By Matias D. Lee. 
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

from math import ceil

multiples = lambda x, N : [ x * i for i in range(1, ceil(N/x))]

def sum_shared_mult (a=5 , b=3 , N=1000):
	"""functions sums multiples shared by a and b lesser than N

        >>> sum_shared_mult (N=10)
        23
        """
	first_muls = multiples(a, N)
	second_muls = multiples(b, N)
	vals_to_sum = set(first_muls).union(set(second_muls))
	return sum(vals_to_sum) 

if __name__ == '__main__':
	print(sum_shared_mult())

