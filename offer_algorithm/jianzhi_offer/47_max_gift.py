# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

def get_max_val(values):
    """

    :param values:[[]]
    :return:
    """

    if values is None:
        return
    rows = len(values)
    cols = len(values[0])
    max_val = []
    for i in range(rows):
        max_val.append([0]*cols)

    for i in range(rows):
        for j in range(cols):
            left = 0
            up = 0
            if i>0:
                up = max_val[i-1][j]
            if j>0:
                left = max_val[i][j-1]
            max_val[i][j] = max(left, up) + values[i][j]
    print max_val[-1][-1]

vals = [[1,2,3],[5,6,7],[7,8,9]]
get_max_val(vals)
