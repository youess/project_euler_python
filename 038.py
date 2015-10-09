#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 038.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:

    192 * 1 = 192
    192 * 2 = 384
    192 * 3 = 576

192384576 is pandigital.

find the largest 1 to 9 digital 9-digit number

that can be made through this way.

let a denote number like 192, n is the multipler.

c be the result number.

Analysis:

    first, c should begins with 9.
    then, a should not be 2 digits like 90, when n = 3,
    c would be 8 digits, and n = 4, c would be 11 digits.

    similar, we could know that a should be a four digits number
    and n = 2.
"""


import doctest
from timeit import default_timer as timer


def is_pandigit(n):

    strn = ''.join(sorted(list(str(n))))
    return 1 if strn == '123456789' else 0


def do2(n):

    return int(str(n) + str(n * 2))


def solution():
    '''
    >>> solution()
    932718654
    '''
    res = [do2(i) for i in xrange(9999, 9000, -1)]
    return max([i for i in res if is_pandigit(i)])


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
