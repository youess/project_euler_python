#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 030.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: digits fifth powers


first, we want the numbers = sum of each digits fifth powers


it's import to know the up bound,

(9)->^5 = 59049
(99)->^5 = 118098
(999)->^5 = ...
....

when (999...) > (999...)->5, the up bound bits number we could get.

"""


import doctest


def get_bit_num(index):
    '''
    >>> get_bit_num(5)
    6
    '''
    bitn = 1
    up_bound = 9
    while up_bound < sum([int(i)**index for i in str(up_bound)]):
        bitn += 1
        up_bound = up_bound * 10 + 9
    return bitn


def digits_power_sum(n):
    '''
    >>> digits_power_sum(4)
    19316
    >>> digits_power_sum(5)
    443839
    '''
    bitn = get_bit_num(n)
    up_bound = 10**bitn
    total = 0
    for i in xrange(2, up_bound):
        if i == sum([int(j)**n for j in str(i)]):
            total += i
    return total


if __name__ == "__main__":
    doctest.testmod()
