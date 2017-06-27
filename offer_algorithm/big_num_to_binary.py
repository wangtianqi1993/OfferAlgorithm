# !usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'


def change_ten_to_binary_once(ten_s):
    shang = []
    temp_yu = 0
    print ten_s
    for i in ten_s:
        num = int(i)
        current_num = num + temp_yu*10
        temp_shang = current_num / 2
        temp_yu = current_num % 2
        # 最高位的商为0时不保存
        if len(shang)>0:
            shang.append(temp_shang)
        else:
            if temp_shang != 0:
                shang.append(temp_shang)

    return shang, temp_yu


def change_ten_to_binary(ten_s):
    """
    任意长的大数转化为2进制数，字符串存储大数字每次求解得到一个余数，求解过程为change_ten_to_binary_once
    由高到地位每一位对2取余， 上一位余数乘10加上本位作为当前位数，得到的商也由高到低位存储。最后将商与最后一位剩数返回
    将商作为当前数在进行计算。最后商没有数据时结束
    :param ten_s:
    :return:
    """
    binary = []
    is_first = True

    while 1:
        if len(ten_s) == 0:
            break

        res = change_ten_to_binary_once(ten_s)
        ten_s = res[0]
        binary.append(res[1])

    binary.reverse()
    print binary

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline()
    change_ten_to_binary(input.strip())
