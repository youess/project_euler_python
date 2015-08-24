#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 014.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: find the longest collatz sequence number under 1 million
"""


import doctest


def get_longest_collatz(n):
    '''
    >>> get_longest_collatz(1000000)
    (524, 837799)
    '''

    if n <= 0:
        raise "must be a positive integer"
    if n <= 2:
        return n
    cache = [0] * n
    max_len, start_num = (1, 1)
    for i in xrange(2, n):
        m = i
        k = 0
        while m >= i and m != 1:
            if m & 1:
                m = 3 * m + 1
            else:
                m = m / 2
            k += 1
        cache[i] = k + cache[m]
        if cache[i] > max_len:
            max_len = cache[i]
            start_num = i
    return max_len, start_num


if __name__ == "__main__":
    doctest.testmod()
