#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 008.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: find the largest product in a series of numbers
"""

import doctest


def prod(l):
    '''
    >>> prod([1, 2, 3])
    6
    '''
    res = 1
    while l:
        k = l.pop()
        res *= k
    return res


def get_series_prod(l, k):

    n = len(l)
    maxP = 0
    for i in xrange(0, n - k):
        window = l[i:(i + k)]
        maxP = max(prod(window), maxP)
    return maxP


if __name__ == "__main__":

    a = open('./series_number_008.txt').read()
    a = list(''.join(a.split('\n')))
    a = map(int, a)
    print 'four adjacent prod value: %d' % get_series_prod(a, 4)
    print 'thirteen adjacent prod value: %d' % get_series_prod(a, 13)
    doctest.testmod()
