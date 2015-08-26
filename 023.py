#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 023.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: non-abundant sums

perfect num = sum of the proper divisors of its own
abundant num > ...
deficient num < ...

any num > 28123 cuold be expressed as two abundant sums


find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers

"""


import doctest


"""
def sumOfProperDivisors(n):
    '''
    >>> sumOfProperDivisors(28)
    28
    >>> sumOfProperDivisors(12)
    16
    '''
    if n < 2:
        return 0

    r = int(n ** 0.5)
    if r**2 == n:
        total = 1 + r
        r -= 1
    else:
        total = 1

    if n & 1:
        f = 3
        step = 2
    else:
        f = 2
        step = 1

    while f <= r:
        if n % f == 0:
            total += f + n / f
        f += step
    return total
"""


def sumOfDivisors(n):

    total = 1
    p = 2
    while p**2 <= n and n > 1:
        if n % p == 0:
            j = p**2
            n /= p
            while n % p == 0:
                j *= p
                n /= p
            total *= j - 1
            total /= p - 1

        if p == 2:
            p = 3
        else:
            p += 2

    if n > 1:
        total *= n + 1
    return total


def sumOfProperDivisors(n):
    '''
    >>> sumOfProperDivisors(28)
    28
    >>> sumOfProperDivisors(12)
    16
    '''
    return sumOfDivisors(n) - n


def get_abundant_under(n):
    return [i for i in xrange(2, n) if sumOfProperDivisors(i) > i]


def sum_non_abundant(n):
    '''
    >>> sum_non_abundant(28123)
    4179935
    '''
    abundant_num = get_abundant_under(n)
    # use dict could be better for space and query effiency
    '''
    abundant_sum = [i + j for i in abundant_num for j in abundant_num
                    if i + j < n]
    abundant_sum = list(set(abundant_sum))
    total = 0
    for i in xrange(1, n):
        try:
            abundant_sum.index(i)
        except:
            total += i
    '''
    abundant_sum = {}
    for i, k in enumerate(abundant_num):
        for j in xrange(i):
            abundant_sum[k + abundant_num[j]] = 1
    total = 0
    for i in xrange(1, n):
        if not abundant_sum.has_key(i):
            total += i
    return total

if __name__ == "__main__":
    doctest.testmod()
