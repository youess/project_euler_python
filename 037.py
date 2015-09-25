#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 037.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: 

left and right trucable primes

3797 -> 379 -> 37 -> 3, left-trucable

"""

import doctest
from timeit import default_timer as timer


def is_prime(n):

    '''
    >>> is_prime(3797)
    1
    '''
    if n < 2:
        return 0 
    if n < 4:
        return 1 
    if n % 2 == 0 or n % 3 == 0:
        return 0
    k = int(n**0.5) + 1 
    for i in xrange(5, k, 6):
        if n % i == 0 or n % (i+2) == 0:
            return 0
    return 1


def is_prime_trucable(n):
    '''
    >>> is_prime_trucable(3797)
    1
    '''

    if not is_prime(n):
        return 0
    strn = str(n)
    if strn[0] not in '2357' or strn[-1] not in '2357':
        return 0
    # left trucable primes
    ln = len(strn)
    lnums = [int(strn[i:]) for i in xrange(1, ln)]
    rnums = [int(strn[:-i]) for i in xrange(1, ln)]
    for i in lnums:
        if not is_prime(i):
            return 0
    for i in rnums:
        if not is_prime(i):
            return 0
    return 1
    
	
def solution():

    '''
    >>> solution()
    748317
    '''
    return sum([i for i in xrange(11, 1000001) 
        if is_prime_trucable(i)])

	
def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()	
