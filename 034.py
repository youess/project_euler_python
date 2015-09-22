#!/usr/bin/env python
# -*- coding: utf-8 -*-


import doctest
from operator import mul
from timeit import default_timer as timer

"""
File: 034.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:

    similar with euler problem 30

first make sure the up bound of each digits factorial

"""


def factorial(n):
    if n == 0:
        return 1
    return reduce(mul, xrange(1, n+1))


def solution():
    '''
    >>> solution()
    40730
    '''

    # 1 - 9! sum upper limit
    facs = [factorial(i) for i in xrange(0, 10)]
    bitn = 1
    while 1:
        limit = int('9' * bitn)
        if limit >= facs[9] * bitn:
            limit = facs[9] * bitn
            break
        bitn += 1

    res = 0
    for i in xrange(10, limit+1):
        num = i
        sum_digits = 0
        while num:
            sum_digits += facs[num % 10]
            num /= 10
        if sum_digits == i:
            res += i

    return res


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
