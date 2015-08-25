#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: 018.py
Author: dengl
Email: denis_lton@hotmail.com
Github: youess.github.com
Description: try to find the path which the sum is maximum of all routes.

http://www.mathblog.dk/project-euler-18/

finding the maximum path seems to use dynamic programming will
always be enough to do the jobs

"""


def max_path_sum(triangle):
    '''use list of list to store the triangle data'''

    lines_num = len(triangle)
    for i in xrange(lines_num - 2, -1, -1):
        for j in xrange(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # for i in xrange(lines_num):
        # print ' '.join(map(str, triangle[i]))
    return triangle[0][0]


if __name__ == '__main__':
    with open('./triangle_data_018.txt') as f:
        data = f.read()
    data = [i.strip().split(' ') for i in data.split('\n')[:-1]]
    data = [map(int, i) for i in data]
    print max_path_sum(data)
