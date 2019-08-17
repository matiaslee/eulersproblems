#!/usr/bin/env python3

#
# Problem 7: 10001st prime - https://projecteuler.net/problem=7
# By Matias D. Lee. 

#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
# can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# Solution: Brute Force :/ 

from math import sqrt

primes = [2]
def is_prime(n):
	d = int(sqrt(n))
	for i in primes:
		if(i>d):
			continue
		if n%i==0:
			return False
	return True

def solver():
	i = 3
	while len(primes)<10001:
		if is_prime(i):
			primes.append(i)
		i = i+2
	return i
	
if __name__ == '__main__':
    print(solver()) 
	
