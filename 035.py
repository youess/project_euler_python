#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 035.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: circular primes under 1 million

197, 971, 719 all primes

"""

import doctest
import sets
from timeit import default_timer as timer
from collections import deque


def is_prime(n):
    k = int(n**0.5) + 1
    if n == 1:
        return 0
    else:
        for i in xrange(2, k):
            if n % i == 0:
                return 0
    return 1


def shifter(n):
    '''
    >>> [i for i in shifter(197)]
    [197, 719, 971]
    '''
    strnum = deque(str(n))
    for i in xrange(len(strnum)):
        yield int(''.join(strnum))
        strnum.rotate()


def solution():
    '''
    >>> solution()
    55
    '''
    N = 1000000
    return sum([1 for i in xrange(2, N)
                if all(is_prime(k) for k in shifter(i))])


def solution2():
    '''
    >>> solution2()          # although cost too much time when use a loop
    55
    '''
    N = 1000000
    counter = 13
    ccp = sets.Set(xrange(100, N))
    while ccp:
        num = ccp.pop()
        nums = [i for i in shifter(num)]
        if all([is_prime(i) for i in nums]):
            counter += len(nums)
            if nums:
                for i in nums[1:]:
                    ccp.remove(i)
    return counter


def print_time_cost():
    start = timer()
    doctest.testmod()
    elapsed_time = (timer() - start) * 1000  # s -> ms
    print 'elapsed time is: %dms' % elapsed_time


if __name__ == '__main__':
    print_time_cost()
