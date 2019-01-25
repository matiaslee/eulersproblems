#!/usr/bin/env python3

# Problem 15: Lattice paths - https://projecteuler.net/problem=15
# By Matias D. Lee
#
# Starting in the top left corner of a 2×2 grid, and 
# only being able to move to the right and down, there 
# are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20×20 grid?
# 

def p15_solver(n):
    """
    >>> p15_solver(2)
    6

    >>> p15_solver(3)
    20
    """

    matrix = [[1 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            if j == i:
                matrix[i][j] = matrix[i-1][j] * 2
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[n][n]

if __name__ == '__main__':
    print(p15_solver(20)) 
