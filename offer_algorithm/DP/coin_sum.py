# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def coin_sum(coins, amount):
    """
    给定不同面值的硬币（数值存放在数组coins）
    和一个金额总值amount。编写函数计算凑齐金额总值所最少需要的硬币数目。如果使用已有的硬币无法凑齐指定的金额，返回-1。
    :param coins:
    :param amount:
    :return:
    """
    # 其中dp[x]代表凑齐金额x所需的最少硬币数。
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for j in range(len(coins)):
            if coins[j]<=i:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    if dp[amount] > amount:
        print -1
    else:
        print dp[amount]

coin_sum([1,2,5], 11)
a = (1, 'a', 3)


class Cartesian():
    def __init__(self, datagroup):
        self.datagroup = datagroup
        self.counter_index = len(datagroup)-1
        self.counter = [0]*len(datagroup)

    def counter_length(self):
        length = 1
        for i in range(len(self.datagroup)):
            length *= len(self.datagroup[i])
        return length

    def handle(self):
        self.counter[self.counter_index] += 1
        if self.counter[self.counter_index] >= len(self.datagroup[self.counter_index]):
            self.counter[self.counter_index] = 0
            self.counter_index -= 1
            if self.counter_index >= 0:
                self.handle()

            self.counter_index = len(self.datagroup)-1

    def assembel(self):
        length = self.counter_length()
        for i in range(length ):
            tmp = []
            for j in range(len(self.datagroup)):
                tmp.append(self.datagroup[j][self.counter[j]])
            print tmp
            self.handle()

data = [['aa1'], ['bb1', 'bb2'], ['cc1', 'cc2', 'cc3']]
ctr = Cartesian(data)
ctr.assembel()












