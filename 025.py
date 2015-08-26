#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 025.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: find the index of fibonacci sequence which
the number had over 1000 digits
"""


import doctest


def fib():
    '''
    >>> s = fib()
    >>> s.next()
    2
    >>> s.next()
    3
    '''
    a, b = 1, 1
    while 1:
        a, b = a + b, a
        yield a


def get_digits_num(n):
    '''
    >>> get_digits_num(1000000)
    7
    '''
    nd = 1
    while n / 10:
        nd += 1
        n /= 10
    return nd


def get_fib_index_by_digits(limit):
    '''
    >>> get_fib_index_by_digits(3)
    12
    >>> get_fib_index_by_digits(1000)
    4782
    '''
    s = fib()
    index = 2
    while 1:
        sn = s.next()
        index += 1
        if get_digits_num(sn) >= limit:
            break
    return index

if __name__ == "__main__":
    doctest.testmod()
