#!/usr/bin/env python3


# Problem 22: Names scores - https://projecteuler.net/problem=22
# Solved by Matias D. Lee.

# 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K 
# text file containing over five-thousand first names, begin by sorting 
# it into alphabetical order. Then working out the alphabetical value for 
# each name, multiply this value by its alphabetical position in the list 
# to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?
# 

import doctest
import string
from math import sqrt
from functools import reduce


def letter_evaluator_contructor():
    evaluator = {}
    letters = list(string.ascii_uppercase)
    for i, a in enumerate(letters):
        evaluator[a] = i + 1
    return evaluator

l_evaluator = letter_evaluator_contructor()

def name_evaluator(name):
    """
    >>> name_evaluator("LEE")
    22

    >>> name_evaluator("MATIAS")
    63

    """
    scores = list(map(lambda x : l_evaluator[x], list(name)))
    score = reduce(lambda x,y : x+y, scores)

    return score

import re
def solver(content=None):
    """
    >>> solver('"MATIAS", "LEE"')
    148

    """

    if content is None:
        with open('files/p022_names.txt') as f:
            content = f.read()
    
    list_of_names = re.findall(r"\w+", content)
    list_of_names.sort()
    scores = list(map(lambda index_name : (index_name[0]+1) * name_evaluator(index_name[1]), enumerate(list_of_names)))
    score = reduce(lambda x,y : x+y, scores)

    return(score)

if __name__ == '__main__':
    print(solver())
