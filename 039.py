#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 039.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:

    p, perimeter of a right angle triangle with integral length sides, {a, b, c}
    eg:
        p = 120, three solutions:
            {20, 48, 52}, {24,45,51}, {30,40,50}

        for which value of p less than 1000,
        is the number of solutions maximised?

    analysis:
        a^2 + b^2 = c^2
        a + b + c = p => c = p - a - b
    => a^2 + b^2 = (p - a - b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab
    => b = (p^2 - 2pa) / (2p - 2a)

    if both a, b is even, => c is even => p is even
    else if a or b is even => c is odd => p is even
    else a, b is odd => c is odd => p is even

    a < c, b < c, a <= b => a < p / 3

"""

import doctest
from timeit import default_timer as timer


def solution():
    '''
    >>> solution()
    840
    '''
    mp = 0
    ms = 0
    for p in xrange(4, 1001, 2):
        tmp = 0
        for a in xrange(2, p / 3):
            if p*(p - 2*a) % (2 * (p - a)) == 0:        # b must be integral
                tmp += 1
        if tmp > ms:
            ms = tmp
            mp = p
    return mp


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
