# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wtq'

import os


def beibao_0_1_core(val, wt, bao_store):
    N = len(wt)
    V = []

    for i in range(N+1):
        temp = [0]*(bao_store+1)
        V.append(temp)

    for item in range(1, N+1):
        for weight in range(1, bao_store+1):
            if wt[item-1] <= weight:
                V[item][weight] = max(val[item-1]+V[item-1][weight-wt[item-1]], V[item-1][weight])
            else:
                V[item][weight] = V[item-1][weight]

    for item in V:
        print item


def more_sample_beibao(val, wt, bao_store):
    V = [0]*(bao_store+1)
    N = len(wt)

    for item in range(1, N+1):
        for weight in range(bao_store, 0, -1):
            if wt[item-1] <= weight:
                V[weight] = max(V[weight], V[weight-wt[item-1]]+val[item-1])
    print V[-1]


if __name__ == "__main__":
    val = [10,40,30,50]
    wt = [5,4,6,3]
    bao_store = 10
    beibao_0_1_core(val, wt, bao_store)
    more_sample_beibao(val, wt, bao_store)
    a = set([1,2,3,4])
    a.remove(1)
    print 5&1
