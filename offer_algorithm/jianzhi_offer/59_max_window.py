# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

def get_max_val(data, n):
    """

    :param data:
    :return:
    """
    if len(data) < n:
        return
    window = []
    for i in range(n):
        window.append(data[i])
    print max(window)

    for i in range(n,len(data)):
        window.pop(0)
        window.append(data[i])
        print max(window)

data = [2,3,4,2,6,2,5,1]
get_max_val(data, 3)
