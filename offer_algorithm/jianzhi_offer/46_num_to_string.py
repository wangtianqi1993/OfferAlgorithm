# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

#
# def num_to_words(num):
#     """
#     输入的数字按照0->a,1->b转化字母，求对于一个数字而言有多少种转换方式
#     :param num:
#     :return:
#     """

def printMatrix(matrix):
        # write code here
    return_list = []
    while len(matrix):
        return_list.extend(matrix.pop(0))
        if len(matrix) == 0:
            break
        row = len(matrix[0])
        col = len(matrix)
        new_matrix = []
        for i in range(row):
            tmp = []
            for j in range(col):
                tmp.append(matrix[j].pop())
            new_matrix.append(tmp)
        matrix = new_matrix
    return return_list

matrix = [[1,2,3],[2,3,4],[3,4,5]]
print printMatrix(matrix)
