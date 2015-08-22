#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 005.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: get the number which is evenly divisible by all given numbers
"""

import doctest


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


def get_smallest_multiples(n):
    '''
    >>> get_smallest_multiples(20)
    232792560
    '''

    myPrime = [i for i in xrange(2, n+1) if is_prime(i)]
    results = 1

    for i in myPrime:
        j = 1
        while i**j <= n:
            j += 1
        results = results * i ** (j - 1)
    return results


if __name__ == "__main__":
    doctest.testmod()
