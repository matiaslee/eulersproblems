#!/usr/bin/env python3

#
# Project Euler: Problem 3 - https://projecteuler.net/problem=3
# Solved by Matias D. Lee 
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
# 

from math import sqrt

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

def calc_primes(n):
	"""
	Function returns an ordered list xs of primes s.t. 
	for all p in xs,  p divides n.

	>>> calc_primes(12)
	[2, 3]

	>>> calc_primes(13195)
	[5, 7, 13, 29]
	"""
	pila = [n]
	primes = []
	while len(pila)!=0:
		top = pila.pop()
		answer = split(top)
		if answer is None:
			if top not in primes:
				primes.append(top)
		else:
			a,b = answer
			pila += [a,b]

	return sorted(primes)


N=600851475143
if __name__ == '__main__':
	print(calc_primes(N)[-1])


