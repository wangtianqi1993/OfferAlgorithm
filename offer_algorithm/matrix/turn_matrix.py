# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def convert_matrix(data, size, num, offset):
    """
    矩阵的逆时针填充
    :param data:
    :param size:
    :param num:
    :param offset:
    :return:
    """
    if size == 0:
        return
    if size == 1:
        data[offset][offset] = num
        return
    for i in range(size-1):
        data[offset+i][offset] = num+i
        data[offset+size-1][offset+i] = num+(size-1)+i
        data[offset+size-1-i][offset+size-1] = num + 2*(size-1)+i
        data[offset][offset+size-1-i] = num+3*(size-1)+i
        print data
    convert_matrix(data, size-2, num+4*(size-1), offset+1)



data = []
for i in range(5):
    data.append([0]*5)
convert_matrix(data, 5, 1, 0)
for i in data:
    print i
