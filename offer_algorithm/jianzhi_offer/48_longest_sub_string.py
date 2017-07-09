# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

def get_max_sub_string(s):
    cur_length = 0
    max_len = 0
    pos = [-1]*26
    for i in range(len(s)):
        cur_index = pos[s[i]-'a']

