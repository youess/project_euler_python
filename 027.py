#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
n^2 + an + b产生n-1个consentive prime value

1. 当n = 0时, b, 则b一定是质数
2. 当n = 1时，a + b + 1是质数 > 0，a > - 1 - b
3. n * (n + a) + b，由于b是质数 => b是奇数 => n * (n + a)是偶数
=> 当n是奇数时，n + a 一定是偶数 => a是奇数
=> 当n是偶数时，n + a 一定是奇数 => a是奇数
'''

import doctest


def is_prime(n):
    k = n**0.5
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in xrange(2, n):
            if n % i == 0:
                return 0
    return 1


def max_count_quadratic_prime_coef_prod():
    '''
    >>> max_count_quadratic_prime_coef_prod()
    -59231
    '''
    N = 1000
    maxn = 0
    for b in xrange(1, N):
        if is_prime(b):
            for a in xrange(-b, N):
                if a & 1:
                    n = 0
                    quadratic_prime = b
                    while quadratic_prime > 0 and is_prime(quadratic_prime):
                        n += 1
                        quadratic_prime = n * (n + a) + b
                    if maxn < n:
                        maxn = n
                        res = a * b
    return res


if __name__ == '__main__':
    doctest.testmod()
