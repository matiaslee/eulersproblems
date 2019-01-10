#!/usr/bin/env python3

#
# Problem 2 : Even Fibonacci numbers - https://projecteuler.net/problem=2
# By Matias D. Lee
#
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.
#


def fibs_generator_leq_N(N):
	"""Function generates fibonnaci sequences with values lesser than N

	>>> fibs_generator_leq_N(-1)
	[]

	>>> fibs_generator_leq_N(1)
	[1, 1]

	>>> fibs_generator_leq_N(6)
	[1, 1, 2, 3, 5]

	"""
	if N < 1:
		return []
	Xs = [1,1]
	new_val = Xs[-1] + Xs[-2]
	while new_val <= N:
		Xs.append(new_val) 	
		new_val = Xs[-1] + Xs[-2]
	return Xs

if __name__ == '__main__': 
	fib_seq = fibs_generator_leq_N(4000000)
	to_sum = [x for x in fib_seq if x % 2 == 0]
	print(sum(to_sum))
