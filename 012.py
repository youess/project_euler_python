#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 012.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: highly divisible triangle number

** why only calculate sqrt(n) **

eg, number N, had a divisor k > sqrt(N), so m = N / k must be a divisor of N,

and m <  N / sqrt(N) = sqrt(N), so N had twice of divisors in [0, sqrt(N)]

"""


import doctest


def triangle_number_generator(n=1):

    while 1:
        yield (n + 1) * n / 2
        n += 1


def get_divisor_number(num):

    if num <= 0:
        return -1
    elif num <= 2:
        return num
    else:
        count = 2
        for i in xrange(2, int(num**0.5) + 1):
            if num % i == 0:
                count += 1

    return 2 * count


def solution():
    '''
    >>> solution()
    76576500
    '''
    limit = 500
    tg = triangle_number_generator(7)
    tnum = tg.next()
    while 1:
        divisor_num = get_divisor_number(tnum)
        if divisor_num >= limit:
            break
        tnum = tg.next()
    return tnum


if __name__ == "__main__":
    doctest.testmod()
