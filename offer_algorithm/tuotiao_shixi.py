# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'
import sys


def FirstNotRepeatingChar():
    # write code here
    a = raw_input()
    print type(a)
    print a.split(" ")[0]
    sys.stdout.write(a)
    float(a)


def test():

    store = set()

    line = sys.stdin.readline()
    m = int(line.strip())
    for i in range(m):
        tmp = sys.stdin.readline()
        tmp = int(tmp.strip())
        store.add(tmp)

    line = sys.stdin.readline()
    n = int(line.strip())
    ans = []
    for i in range(n):
        tmp = sys.stdin.readline()
        tmp = int(tmp.strip())
        if tmp in store:
            ans.append(tmp)
    for i in ans:
        print i,

def second():
    input = sys.stdin.readline()
    input = input.strip()
    input = input.split(" ")
    print input
    style = []
    ans = []
    for i in range(3):
        nums = []
        if i == 0:

            for j in range(5):
                if j == 0 or j ==4:
                    nums.append("***")
                else:
                    nums.append("* *")

        elif i == 1:
            for j in range(5):
                nums.append(" * ")
        elif i == 2:
            for j in range(5):
                if j == 0 or j == 2 or j == 4:
                    nums.append("***")
                elif j == 1:
                    nums.append("  *")
                else:
                    nums.append("*  ")

        style.append(nums)

    nums = []
    for i in range(5):
        if i == 2:
            nums.append("***")
        else:
            nums.append(" * ")
    style.append(nums)

    nums = []
    for i in range(5):
        if i == 1 or i == 3:
            nums.append("***")
        else:
            nums.append("   ")
    style.append(nums)

    for i in input:
        print i, type(i)
        if i == "=":
            ans.append(style[4])
        if i == "+":
            ans.append(style[3])
        else:
            try:
                ans.append(style[int(i)])
            except Exception, e:
                #ans.append(style[4])
                print e

    for i in range(5):
        str = ""
        for j in ans:
            str = str+j[i]
            str += "  "
        print str


def test_algorithm():
    import time
    a = [i for i in range(10000000)]
    sign = 0
    time1 = time.time()
    for i in range(1000):
        if i in a:
            sign = 1
    time2 = time.time()
    print time2-time1

    use = {}
    for i in range(10000000):
        use[i] = 0
    time3 = time.time()
    for i in range(1000):
        if i in use:
            sign = 1
    time4 = time.time()
    print time4 - time3

    store = set([i for i in range(10000000)])
    time5 = time.time()
    for i in range(1000):
        if i in store:
            sign = 1
    time6 = time.time()
    print time6 - time5


if __name__ == "__main__":
    # FirstNotRepeatingChar()
    # test()
    second()
    # test_algorithm()

