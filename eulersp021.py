#!/usr/bin/env python3


# Problem 21: Amicable numbers - https://projecteuler.net/problem=21
# Solved by Matias D. Lee.

# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.
# 

# Note: Most of the code was done for solving problem 12

import doctest
from math import sqrt
from functools import reduce

all_primes = set({})

def split(n):
	""" Function returns a and b such that 'a * b = n' and there is 
	no c such that 'n mod c = 0' and 'a < c < sqr(n)'.  If n is prime, 
	functions returns None
	
	>>> split(5)
	

	>>> split(10)
	(2, 5)

	>>> split(26)
	(2, 13)
	"""
	d = int(sqrt(n))
	for i in range(d,1,-1):
		if n%i==0:
			return i, int(n/i)
	return None

def factorization(n):
    """
    Function returns an ordered list xs of primes s.t. 
    for all p in xs,  p divides n.  
    
    >>> factorization(12)
    [2, 2, 3]

    >>> factorization(24)
    [2, 2, 2, 3]

    >>> factorization(28)
    [2, 2, 7]

    """
    pila = [n]
    primes = []
    while len(pila)!=0:
        top = pila.pop()
        if top in all_primes:
            primes.append(top)
            continue
        answer = split(top)
        if answer is None:
            primes.append(top)
            all_primes.add(top)
        else:
        	a,b = answer
        	pila += [a,b]

    return sorted(primes)

def powerset_of_a_list(xs):
    """
    >>> powerset_of_a_list([10])
    [[], [10]]

    >>> powerset_of_a_list([10, 2])
    [[], [2], [10], [2, 10]]

    >>> powerset_of_a_list([2, 2])
    [[], [2], [2], [2, 2]]
    """
    if len(xs) == 0:
        return [[]]

    if len(xs) >0:
        x = xs[0]
        xs_prime = xs[1:]
        rec_case = powerset_of_a_list(xs_prime) 
        return rec_case + [ys + [x] for ys in rec_case]

from functools import reduce

def calc_factors(n):
    """
    >>> calc_factors(4)
    {1, 2, 4}

    >>> calc_factors(28)
    {1, 2, 4, 7, 14, 28}
    """
    prime_factors = factorization(n)
    powerset = powerset_of_a_list(prime_factors)
    factors = set([])
    for xs in powerset:
        if len(xs) == 0:
            factors.add(1)
        else:
            factor = reduce(lambda x,y : x * y, xs)
            factors.add(factor)
    return factors

def d(x):
    """
    >>> d(220)
    284

    >>> d(284)
    220

    """
    return sum(calc_factors(x)) - x 

def p21_solver(n=10000):
    """

    """
    vals_to_check = {x for x in range(2,n)}
    amicables = []
    while(len(vals_to_check) != 0):
        v0 = vals_to_check.pop()
        d0 = d(v0)
        if d0 not in vals_to_check:
            continue 
        vals_to_check.remove(d0)
        if v0 == d(d0):
            amicables.append(v0)
            amicables.append(d0)            

    return sum(amicables)

if __name__ == '__main__':
    print(p21_solver())