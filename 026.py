#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 026.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: calculate the longest recurring cycle in its decimal fraction part
under 1000


if a decimal fraction is not recurring cycle, its denominator
must be mod by 2 or 5 == 0

http://blog.sina.com.cn/s/blog_9f26be1d01012nyv.html

"""

import doctest


def get_base(num):
    '''
    >>> get_base(5)
    1
    >>> get_base(11)
    11
    '''
    base = num
    while base % 2 == 0:
        base /= 2
    while base % 5 == 0:
        base /= 5
    return base


def get_recycle_num(num):

    '''
    >>> get_recycle_num(3)
    1
    >>> get_recycle_num(7)
    6
    '''
    base = get_base(num)
    if base == 1:
        return 0
    start = 9
    count = 1
    while start % base != 0:
        count += 1
        start = start * 10 + 9
    return count


def get_max_recycling_num(n):
    '''
    >>> get_max_recycling_num(1000)
    983
    '''
    ml = [get_recycle_num(i) for i in xrange(1, n)]
    return ml.index(max(ml)) + 1


if __name__ == "__main__":
    doctest.testmod()
