#!/usr/bin/env python3

# 
# Problem 5: Smallest multiple - https://projecteuler.net/problem=5
# By Matias D. Lee
# 
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?
# 

from math import sqrt
from collections import defaultdict

def split(n):
	d = int(sqrt(n))
	for i in range(d,1,-1):
		if n%i==0:
			return i, int(n/i)
	return None

def factorization(n):
	"""
	>>> factorization(18)
	defaultdict(<class 'int'>, {3: 2, 2: 1})
	"""
	pila = [n]
	primes = defaultdict(int)
	while len(pila)!=0:
		top = pila.pop()
		answer = split(top)
		if answer is None:
			primes[top] = primes[top] + 1
		else:
			a,b = answer
			pila += [a,b]
	return primes


def solver(n):
	"""
	>>> solver(10)
	2520
	"""
	my_primes = defaultdict(int)
	for i in range(1,n+1):
		current_primes = factorization(i)
		for p in current_primes:
			my_primes[p] = max(my_primes[p], current_primes[p])

	result = 1
	for p in my_primes:
		result *= (p ** my_primes[p])

	return result

if __name__ == '__main__':
	print(solver(20))
	