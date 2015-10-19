#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 040.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: champernowne's constant


here is one irrational decimal fraction number

0.123456789101112131415161718192021...

which consisted of the positive integers


d_n represents the n^th digit of fraction part,

output:

    d_1 * d_10 * d_100 * ... * d_1000000

"""

import doctest
from timeit import default_timer as timer


def get_digits_num(n):
    return len(str(n))


def irrational_seq():
    i = 1
    while 1:
        s = list(str(i))
        for j in xrange(len(s)):
            yield int(s[j])
        i += 1


def solution():
    """
    >>> solution()
    210
    """
    ind = [10**i for i in xrange(7)]
    #  print ind
    iseq = irrational_seq()
    i = 0
    res = 1
    while i < ind[-1]:
        n = iseq.next()
        i += 1
        if i in ind:
            res *= n
    return res


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
