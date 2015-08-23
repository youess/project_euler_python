#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 013.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: large number sum, not as c/c++, you need create your own bigInt,
in python just sum the integer.
"""

import doctest


def get_large_num_sum(l):

    return sum(l)


def top(num, k):

    return str(num)[:k]


def tail(num, k):

    return str(num)[(-k):]


if __name__ == "__main__":
    with open("./numbers_013.txt") as f:
        a = f.read()
    a = a.split("\n")[:-1]
    print len(a), len(a[0])
    a = get_large_num_sum(map(int, a))
    print top(a, 10)
    print tail(a, 10)
    doctest.testmod()
