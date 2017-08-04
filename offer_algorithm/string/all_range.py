# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


class AllRange():
    def swap(self, data, s1, s2):
        try:
            tmp = data[s1]
            data[s1] = data[s2]
            data[s2] = tmp
        except Exception, e:
            print "error", e

    def isswap(self, data, s1, s2):
        try:
            if data[s2] in data[s1:s2]:
                return False
            else:
                return True
        except Exception, e:
            print "error", e
            return False

    def all_range_core(self, data, start, end):
        if start == end - 1:
            tmp = "".join(data)
            print tmp
        else:
            for i in range(start, end):
                if self.isswap(data, start, i):
                    self.swap(data, start, i)
                    self.all_range_core(data, start + 1, end)
                    # 通过下一个swap交换回来，确保下一次交换就在原字符串的基础上交换
                    self.swap(data, start, i)

    def all_range(self, str):
        data = [i for i in str]
        self.all_range_core(data, 0, len(data))


class AllCom():
    def combination(self, s):
        if s is None:
            return
        len_s = len(s)
        sum_num = 1<<len_s
        for i in range(1, sum_num):
            index = []
            for j in range(len_s):
                if i&(1<<j):
                    index.append(j)
            if len(index)>0:
                tep = [s[p] for p in index]
                print "".join(tep)

if __name__ == "__main__":
    ranges = AllRange()
    ranges.all_range("113")

    com = AllCom()
    com.combination("123")
