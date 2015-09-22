#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 033.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:

49 / 98 = 4 / 8 remains correct when cancels the 9s.

30 / 50 = 3 / 5 will be a trial examples.

If the product of these four fractions is given in
its lowest common terms, find the value of the denominator


solution:

设定1 <= a < b <= 9, 需要去除的数为1 <= i <= 9

符合要求的4种形式：

1. (10i + a) / (10i + b) = a / b

=> a = b, wrong

2. (10a + i) / (10b + i) = a / b

=> a = b, wrong

3. (10i + a) / (10b + i) = a / b

=> 9b(a - i) = i(b - a)

=> a > i due to left side be positive

=> a - i = i / 9 * (1 - a / b)

=> 左边由于是整数所以是>=1的，右边肯定是小于1的，所以wrong

4. (10i + a) / (10b + i) 是唯一的一种形式

=> 9a(b - i) = i(a - b)

=> b < i

"""

import doctest
from timeit import default_timer as timer


def gcd(a, b):

    '''
    >>> gcd(18, 27)
    9
    '''
    while b:
        a, b = b, a % b
    return a


def solution():
    '''
    >>> solution()
    100
    '''
    den_product = nom_product = 1

    for i in xrange(1, 10):
        for b in xrange(1, i):
            for a in xrange(1, b):
                if 9 * a * (b - i) == i * (a - b):
                    den_product *= b
                    nom_product *= a

    den_product /= gcd(nom_product, den_product)
    return den_product


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
