#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 032.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:  pandigital products

39 * 186 = 7254, 1 ~ 9 numbers used, find all sum of all products
which are 1 through 9 pandigits.


analysis:

first we could use a table to known how to get a 9 digits number,
then we observed that only 2*3, 1*4 could result a 9 digits number.

   1   2   3     4
1 3-4 5-6 7-8   9-10
2  -  7-8 9-10  11-12
3  -   -  11-12 13-14
4  -   -   -    15-16

"""

from timeit import default_timer as timer
import doctest


def is_pandigit(multiplicand, multiplier):

    '''
    >>> is_pandigit(39, 186)
    1
    '''
    product = multiplicand * multiplier
    pandigits = sorted(''.join(map(str, [multiplicand, multiplier, product])))
    targets = map(str, range(1, 10))
    if pandigits == targets:
        return 1
    return 0


def solution():

    '''
    >>> solution()
    45228
    '''
    products = []
    for i in xrange(12, 100):
        for j in xrange(123, 1000):
            if is_pandigit(i, j):
                products.append(i * j)

    for i in xrange(1, 10):
        for j in xrange(1234, 10000):
            if is_pandigit(i, j):
                products.append(i * j)

    return sum(set(products))


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time

if __name__ == '__main__':
    print_time_cost()
