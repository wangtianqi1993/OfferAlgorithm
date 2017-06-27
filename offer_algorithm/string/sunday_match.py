# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def sunday_match(s, obj):
    """
    高效的sunday字符串匹配算法
    首先原字符串和子串左端对齐，发现“T”与“E”不匹配之后，检测原字符串中下一个字符（在这个例子中是“IS”后面的那个空格）
    是否在子串中出现，如果出现移动子串将两者对齐，如果没有出现则直接将子串移动到下一个位置。
    这里空格没有在子串中出现，移动子串到空格的下一个位置“A”
    :param s:
    :param obj:
    :return:
    """
    cur_obj = 0
    len_obj = len(obj)
    len_s = len(s)
    s_index = 0
    s_head = 0
    obj_index = 0
    sign = 0
    dis = 0
    find_sign = 0

    while s_index<len_s:

        if obj_index == len_obj -1:
            return True
        if sign == 1:
            sign = 0
            s_index = s_head+dis
            s_head = s_index
            obj_index = 0
            print s_index, s[s_index]

        # print s[s_index], obj[obj_index]
        if s[s_index] == obj[obj_index]:
            s_index += 1
            obj_index += 1
        else:
            sign = 1
            if s_head + len_obj <= len_s-1:
                cur_s = s[s_head+len_obj]
                for i in range(len_obj-1, -1, -1):
                    if obj[i] == cur_s:
                        find_sign = 1
                        break
                if find_sign == 0:
                    dis = len_obj-i+1
                else:
                    dis = len_obj-i
                    find_sign = 0
                # print dis, cur_s
            else:
                return False
    return False

s = "this is a simple example"
obj = "example"
s1 = "abcdefabcdp"
obj1 = "abcdp"
result = sunday_match(s1, obj1)
print result
import itertools
tt = list(itertools.combinations([1,2,3,4,5], 2))
for i in tt:
    print sum(i)
