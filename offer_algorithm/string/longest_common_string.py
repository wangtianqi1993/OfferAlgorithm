# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

# 利用动态规划问题来求解数组中的一些问题


def get_longest_common_sequence(s1, s2):
    """
    * 求s1 s2的最长公共子序列
    * 构造二维数组c[][]记录X[i]和Y[j]的LCS长度 (i,j)是前缀
    * c[i][j]=0; 当 i = j = 0;
    * c[i][j]=c[i-1][j-1]+1; 当 i = j > 0; Xi == Y[i]
    * c[i][j]=max(c[i-1][j],c[i][j-1]); 当 i = j > 0; Xi != Y[i]
    * 需要计算 m*n 个子问题的长度 即 任意c[i][j]的长度
    * -- 填表过程
    :param s1:
    :param s2:
    :return:
    """

    max_store = []
    for item in range(len(s1)+1):
        temp_store = [0]*(len(s2)+1)
        max_store.append(temp_store)

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                max_store[i][j] = max_store[i-1][j-1] + 1
            else:
                max_store[i][j] = max(max_store[i-1][j], max_store[i][j-1])
    print max_store


def get_longest_common_string(s1, s2):
    """
    计算s1 s2中的最长的公共子串（与公共子序列不同的是公共子串必须是连续的）
    :param s1:
    :param s2:
    :return:
    """
    max_store = []
    for item in range(len(s1)+1):
        max_store.append([0]*(len(s2)+1))

    max_string_len = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                max_store[i][j] = max_store[i-1][j-1] + 1
                max_string_len = max(max_string_len, max_store[i][j])
    print max_string_len


def get_longest_increace_seq1(s):
    """
    计算s中最长的单调递增的子序列
    :param s1:
    :param s2:
    :return:
    """
    max_len = 1
    s_len = len(s)
    dp = [0]*s_len
    dp[0] = 1

    for i in range(1, s_len):
        dp[i] = 1
        for j in range(i-1, -1, -1):
            if dp[j]+1 > dp[i] and s[j] < s[i]:
                dp[i] = dp[j] + 1
        if dp[i] > max_len:
            max_len = dp[i]
    print dp, max_len


def get_longest_increace_seq2(data):
    """
    第二种方法求解最长递增子序列，即对data升序排序得到data2
    求data与data2的最长公共递增子序列
    :param data:
    :return:
    """
    remove_index = []
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            remove_index.append(i)

    new_data = [data[i] for i in range(len(data)) if i not in remove_index]
    data_s = sorted(new_data)
    dp = []
    for i in range(len(new_data)+1):
        dp.append([0]*(len(new_data)+1))

    for i in range(1, len(new_data)+1):
        for j in range(1, len(new_data)+1):
            if new_data[i-1]==data_s[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print dp


get_longest_increace_seq2([1,2,3,-1,0,0,2,1])


# s1 = "ABCDEFGH"
# s2 = "ABCFFFFFF"
# get_longest_common_string(s1, s2)
# get_longest_common_sequence(s1, s2)

def get_max_mut_string_baoli(s):
    """
    给一个浮点数序列，取最大乘积连续子串的值，
    例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。也就是说，上述数组中，
    3 0.5 8这3个数的乘积3 0.5 8=12是最大的，而且是连续的。
    暴力方法求解
    :param s:
    :return:
    """
    if s is None:
        return
    if len(s) == 0:
        return

    max_result = s[0]
    for i in range(len(s)):
        x = 1
        for j in range(i, len(s)):
            x *= s[j]
            if x > max_result:
                max_result = x
    print max_result

test = [-2.5, 4, 0, 3, 0.5, 8, -1]
get_max_mut_string_baoli(test)


def get_max_mut_string_dp(a):
    """
    动态规划求解
    :param s:
    :return:
    """
    max_end = a[0]
    min_end = a[0]
    max_result = a[0]
    for i in range(1, len(a)):
        end1 = max_end*a[i]
        end2 = min_end*a[i]
        max_end = max(max(end1, end2), a[i])
        min_end = min(min(end1, end2), a[i])
        max_result = max(max_result, max_end)
    print max_result
# get_max_mut_string_dp(test)

ring_state = [0]*100
for i in range(100):
    for j in range(0, 100, i+1):
        if ring_state[j] == 0:
            ring_state[j] = 1
        elif ring_state[j] == 1:
            ring_state[j] = 0
print ring_state


