#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 006.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: sum square difference, (1+2+3)^2 - (1^2 + 2^2 + 3^2)
"""

import doctest


def square_difference(n):
    """
    >>> square_difference(10)
    2640
    >>> square_difference(100)
    25164150
    """

    diff = 0
    while n:
        diff += 2 * n * sum(xrange(1, n))
        n -= 1
    return diff

if __name__ == "__main__":
    doctest.testmod()
