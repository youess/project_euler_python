#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 041.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: largest pandigital primes

brute-force

n is divisible by 3 if each digits sum is divisible by 3
sum(xrange(1, 10)) = 45   /  not prime
sum(xrange(1, 9)) = 36    / not
sum(xrange(1, 8)) = 28    / start here

"""


import doctest
from timeit import default_timer as timer

from p010 import is_prime


def solution():
    """
    >>> solution()
    7652413
    """
    from itertools import permutations
    # if not use tricks
    for i in range(9, 0, -1):
        pandigits = permutations(xrange(i, 0, -1))
        for p in pandigits:
            p = int(''.join(map(str, p)))
            if is_prime(p):
                return p


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
