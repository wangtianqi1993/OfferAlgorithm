# !usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


def com_n_m(nums, k):
    """
    nums 数列中选择ｋ个元素, 求所有k个元素的组合
    :param nums:
    :param k:
    :param tmp_num:
    :return:
    """
    nums_len = len(nums)
    if nums_len < k:
        return

    nums_index = [0]*nums_len
    for i in range(k):
        nums_index[i] = 1

    while 1:
        sign = 0
        # print nums_index
        tmp = [nums[i] for i in range(nums_len) if nums_index[i] == 1]
        print tmp
        # 找到第一个数组中的第一个10变为01
        for i in range(nums_len-1):
            if nums_index[i] == 1 and nums_index[i+1] == 0:
                sign = 1
                break

        if sign == 0:
            break
        nums_index[i], nums_index[i+1] = nums_index[i+1], nums_index[i]

        # 将10变01后左边的所有1全部移动到数组的最左端
        if nums_index[0] == 1:
            continue

        if 1 not in nums_index[:i]:
            continue

        zero_count = 1
        for j in range(1, i):
            if nums_index[j] == 0:
                zero_count += 1
            else:
                break

        tmp = nums_index[zero_count:i]+nums_index[0:zero_count]
        nums_index = tmp + nums_index[i:]


def get_min_sub_array(s, nums):
    start, end = 0, 0
    sum = 0
    nums_len = len(nums)
    min_len = nums_len+1

    while end < nums_len:
        while end < nums_len and sum<s:
            sum += nums[end]
            end += 1
        while start < end and sum>=s:
            min_len = min(min_len, end-start)
            sum -= nums[start]
            start += 1
    print min_len

nums = [1,2,2,3,4,5,1,2,3]
get_min_sub_array(7, nums)

