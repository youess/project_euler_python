#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 020.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: factorial digits sum of 100!

1. you should store big integer of this results
2. efficient to calculate the results
"""


import doctest


def factorial(n):
    '''
    >>> factorial(10)
    3628800
    '''
    res = 1
    while n:
        res *= n
        n -= 1
    return res


def sum_digits(num):
    '''
    >>> sum_digits(factorial(10))
    27
    >>> sum_digits(factorial(100))
    648L
    '''
    total = 0
    while num:
        total += num % 10
        num /= 10
    return total


if __name__ == "__main__":
    doctest.testmod()
