#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 007.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: find the 10001th prime number
"""

import doctest


def is_prime(n):

    '''
    >>> is_prime(2)
    True
    '''
    k = int(n**0.5)
    if n < 2:
        return False
    else:
        for i in xrange(2, k + 1):
            if n % i == 0:
                return False
    return True


def get_prime(k):
    '''
    >>> get_prime(6)
    13
    >>> get_prime(10001)
    104743
    '''
    the_prime = 2
    counter = 0
    while 1:
        if is_prime(the_prime):
            counter += 1
        if counter >= k:
            break
        the_prime += 1
    return the_prime


if __name__ == "__main__":
    doctest.testmod()
