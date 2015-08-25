#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 019.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description:
    count the sundays on the first of month  每月第一天
    from 1 Jan 1901 to 31 dec 2000

more details refer this site

http://m.blog.csdn.net/blog/zhongyifly/16349113

"""


import doctest
import datetime


def get_weekday(dstr, dformat):

    dt = datetime.datetime.strptime(dstr, dformat)
    return datetime.date.weekday(dt)


def first_month_sunday_count(yfrom, yto):
    '''
    >>> first_month_sunday_count(1901, 2000)
    171
    '''
    count = 0
    for year in xrange(yfrom, yto + 1):
        for month in xrange(1, 13):
            date_str = '%d-%d-01' % (year, month)
            if get_weekday(date_str, '%Y-%m-%d') == 6:
                count += 1
    return count


if __name__ == "__main__":
    doctest.testmod()
