# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

def get_repeat_num(data):
    if data is None or len(data) == 0 or len(data) == 1:
        return False
    for i in range(len(data)):
        while data[i] != i:
            if data[i] == data[data[i]]:
                print data[i]
                return True
            index = data[i]
            data[i], data[index] = data[index], data[i]

get_repeat_num([2,3,1,0,2,5,3])

