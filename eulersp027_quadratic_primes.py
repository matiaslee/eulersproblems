#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Problem 27: Quadratic Primes - https://projecteuler.net/problem=27
# By Matias D. Lee. 
# 
# Euler discovered the remarkable quadratic formula:
#
# n**2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
# However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
# is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive 
# values 0≤n≤79. 
#  The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
#
#    n2+an+b
#
# where |a| < 1000 and |b| ≤ 1000
#
# where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces 
# the maximum number of primes for consecutive values of n, starting with n=0.
#

# Some facts: 
# - b has to be prime and then b > 0. (n2+an+b is prime for n==0)
# - a < 0 => |a| < b. (n2+an+b is prime and thefore cannot be negative)
# - a has to be even. (Otherwise n2+an+b is even for n==1)
# - We can reach 
# - n2+an+b == n(n+a) + b, then if n==b or n+a==b, b|n2+an+b
# 

from math import sqrt

all_primes = {2}

def is_prime(n):
    if n in all_primes:
        return True
    
    d = int(sqrt(n))
    for i in range(2,d):
        if i>d:
            break
        if n%i==0:
            return False
    
    all_primes.add(n)
    return True

def primes_generator(N):
    primes = [2]
    for n in range(3,N, 2): 
        if is_prime(n):
            primes.append(n)
    return primes

def check_max_n(a, b, n):
    check = True
    while check:
        val_to_check = n**2 + a*n + b
        if val_to_check < 0 or not is_prime(val_to_check):
            check = False
        else:
            n += 1
    return (n-1)

def check_first_39(a,b):
    for n in range(0, 39):
        val_to_check = n**2 + a*n + b
        if val_to_check < 0 or not is_prime(val_to_check):
            return False
    return True

from collections import defaultdict

if __name__ == '__main__':
    bs_ = primes_generator(1000)
    factors = [
        (b, [-b + i for i in range(0, 2*b, 2)]) for b in bs_ 
    ]
    candidates = defaultdict(set)
    n_base = 39
    
    for b, as_ in factors:
        for a in as_:
            max_n = check_max_n(a,b,n_base)
            candidates[max_n].add((a,b))
    
    to_check = list(candidates.keys())
    to_check.sort(reverse=True)
    found_it = False
    for k in to_check:
        factors = candidates[k]
        for a,b in factors:
            if check_first_39(a,b):
                found_it = True
                break
        if found_it:
            break

    print('a: {} - b: {} - max n: {}'.format(a,b,k))
    print('Answer: {}'.format(a*b))

