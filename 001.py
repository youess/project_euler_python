#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest


def sumRangeNums(base_num, N):
    """
    >>> sumRangeNums([3, 5], 1000)
    233168
    """
    total = 0
    for i in xrange(1, N):
        base = [i % x for x in base_num]
        try:
            base.index(0)
            total += i
        except ValueError:
            continue
    return total


if __name__ == "__main__":
    doctest.testmod()
