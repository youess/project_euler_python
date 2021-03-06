#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 010.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: summation of primes
"""

import doctest


"""
def is_prime(n):
    '''
    >>> is_prime(5)
    True
    '''
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True
"""


def is_prime(n):

    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        k = int(n**0.5)
        f = 5
        while f <= k:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6

    return True


def summation_prime(N):
    '''
    >>> summation_prime(2000000)
    142913828922
    '''
    total = 2 + 3
    for i in xrange(5, N, 2):
        if is_prime(i):
            total += i
    return total


if __name__ == "__main__":
    doctest.testmod()
