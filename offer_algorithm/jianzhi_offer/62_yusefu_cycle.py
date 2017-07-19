# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

def last_remaining(data, m):
    """
    约瑟夫环问题，０到n-1形成一个环，每次从0开始删除第m个数字，求圆圈中最后一个字
    :param data:
    :param m:
    :return:
    """
    current = 0
    while len(data) > 1:
        for i in range(m-1):
            current += 1
            if current >= len(data):
                current = 0

        data.pop(current)
        if current >= len(data):
            current = 0
    print data[0]

last_remaining([0,1,2,3,4],3)

