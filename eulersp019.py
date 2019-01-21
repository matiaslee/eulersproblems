#!/usr/bin/env python3

#
# Problem 19: Longest Collatz sequence - https://projecteuler.net/problem=19
# By Matias D. Lee. 
# 
#  You are given the following information, but you may prefer to do some research 
#  for yourself.
# 
#     - 1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     - A leap year occurs on any year evenly divisible by 4, 
#     but not on a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
# 
# 

import datetime as dt 

def p19_solver():
    sundays = [(m, y) for m in range(1,13) for y in range(1901, 2001)\
                         if dt.date(y, m, 1).weekday() == 6  ]

    return  len(sundays) 

if __name__ == '__main__':
    print(p19_solver())
