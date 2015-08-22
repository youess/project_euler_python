#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 003.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: get the largest prime factor(既是质数又是因素) of a given number
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


def get_largest_prime_factor(num):
    """
    >>> get_largest_prime_factor(600851475143)
    6857
    """
    a = int(num**0.5) + 1
    max_pf = 0
    while a:
        if num % a == 0 and is_prime(a):
            max_pf = a
            break
        a -= 2
    return max_pf


if __name__ == "__main__":
    doctest.testmod()
