#!/usr/bin/env python3

# Problem 4: Largest palindrome product - https://projecteuler.net/problem=4
# By Matias D. Lee
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 
#  2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 


def solver(n_digits):
	"""
	>>> solver(2)
	9009
	"""
	upper_limit = int('9' * n_digits)
	lower_limit = int('1' + '0' * (n_digits-1))

	palindromes = []
	for i in range(upper_limit, lower_limit-1, -1):
		for j in range(lower_limit, i+1): # Recall mult is commutative
			val = i * j
			as_string = str(val)
			if as_string == as_string[::-1]:
				palindromes.append(val)
	return max(palindromes)

if __name__ == '__main__':
	print(solver(3))