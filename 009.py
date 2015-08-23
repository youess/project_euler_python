#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 009.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: special pyhagorean tripplet, direct solution not clever
"""

import doctest
import operator


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def is_right_angle(a, b, c):
    if is_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 \
                or b**2 + c**2 == a**2:
            return True
    return False


def solution():
    n = 1000
    for i in xrange(1, n):
        for j in xrange(1, n):
            if n - i - j > 0:
                if is_right_angle(i, j, n - i - j):
                    return (i, j, n - i - j)


if __name__ == "__main__":
    print reduce(operator.mul, solution())
    doctest.testmod()
