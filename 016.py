#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest


'''
if programming lang do not support big integer processing, 
you need use a array to store each byte.

http://www.cnblogs.com/herbert/archive/2011/02/13/1953943.html

try use array like array[0], array[1] to represent 46788765

array[0], 4678
array[1], 8765

'''


def BMul(x, y):
    '''try to store x^y in arr'''
    arr = [0] * (y / 3 / 4 + 1)        # 2^3 = 8 < 10 and use 4 digits to store
    arr[0] = 1
    pos = 1              # pos指示x的y次方占用的段数
    tmp = 0

    for yt in xrange(y):
        incse = 0        # 记录进位信息
        for at in xrange(pos):
            tmp = arr[at]
            arr[at] *= x         # 第at段乘上x
            arr[at] += incse     # 加上at-1段的进位
            if arr[at] > 9999:
                if at == pos - 1:     # 首段溢出
                    arr[pos] = arr[at] / 10000
                    arr[at] %= 10000
                    pos += 1
                    break
                else:
                    incse = arr[at] / 10000
                    arr[at] %= 10000
            else:
                incse = 0
    # 逆序
    arr = arr[::-1]
    return arr


def digits_sum_power(N):
    '''
    >>> digits_sum_power(1000)
    1366L
    '''
    a = 2 ** N
    c = 0
    while a:
        c += a % 10
        a /= 10
    return c


if __name__ == '__main__':
    num = BMul(2, 1000)
    print num
    digits_sum = 0
    while num:
        tmp = num.pop()
        while tmp:
            digits_sum += tmp % 10
            tmp /= 10
    print digits_sum
    doctest.testmod()
