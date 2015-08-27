#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
find the number spiral diagonals in clockwise direction matrix

1001 * 1001

calculate the four vertex of the matrix layer by layer

'''

import doctest


def sum_diagonal_value(n):
    '''
    >>> sum_diagonal_value(5)
    101
    >>> sum_diagonal_value(1001)
    669171001
    '''
    half_row = n / 2 + 1
    total = 0
    last_num = n**2
    d = n - 1
    for i in xrange(half_row):
        if d != 0:
            total += 4 * last_num - 6 * d
        else:
            total += 1
        last_num -= 4 * d
        d -= 2
    return total


if __name__ == "__main__":
    doctest.testmod()
