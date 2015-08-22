#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest


def is_palindrom(s):
    """
    >>> is_palindrom(9009)
    True
    """
    s = str(s)
    ss = s[::-1]
    return ss == s


def get_largest_palindrom(N):
    '''
    >>> get_largest_palindrom(999)
    906609
    '''
    # l = [x * y for x in range(100, 1000) for y in range(100, 1000)
    #      if is_palindrom(x * y)]
    # l.sort()
    # return l[-1]
    largest_palindrom = 0
    for i in xrange(1000, 100, -1):
        for j in xrange(1000, 100, -1):
            if i * j <= largest_palindrom:
                break
            if is_palindrom(i * j):
                largest_palindrom = i * j
    return largest_palindrom


if __name__ == "__main__":
    doctest.testmod()
