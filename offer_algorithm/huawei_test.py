# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'


def is_subsequence(list_a, list_b):
    """
    判断list_A是否是list_B的子序列，算法的时间复杂度为O(m*n),　m,n分别为list_a list_b的长度
    :param list_a:
    :param list_b:
    :return:是子序列返回True，否则返回False
    """
    # 对list_a list_b的输入合法性作判别
    if list_a is None or list_b is None:
        return False
    if len(list_a) > len(list_b):
        return False

    sub_seq_sign = False

    if not isinstance(list_a, list) or not isinstance(list_b, list):
        print "place input list type"
        return False

    len_a = len(list_a)
    len_b = len(list_b)
    index_a = 0
    for b_index in range(0, len_b):
        # 遍历list_b的，找到list_b中包含list_a中的第一个元素的元素
        try:
            if list_a[index_a] in list_b[b_index]:
                # 记录list_b中包含list_a的第一个元素的位置
                index_a+=1
        except Exception, e:
            print "place ensure every element is string!"
            return False
    if index_a == len(a):
        return True
    else:
        return False


def analyse_config_file(config_file):
    """
    一个简单的配置文件解释器, 时间复杂度O(n)　n为配置文件的行数
    :param config_file: 配置文件的名称,默认在当前的目录下
    :return: 打印每行注释的key value
    """
    try:
        with open(config_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "#" in line:
                    line_split = line.split("#")
                    if len(line_split)>0:
                        # 当注释作为整行时
                        if "=" in line_split[0]:
                            try:
                                key_val = line_split[0].split("=")
                                print key_val[0].strip(), key_val[1].strip()
                            except Exception, e:
                                print "split error"

                        # 当注释出现在行尾时
                        if "=" in line_split[1]:
                            try:
                                key_val = line_split[1].split("=")
                                print key_val[0].strip(), key_val[1].strip()
                            except Exception, e:
                                print "split error"
                else:
                    splits = line.split("=")
                    if len(splits)==2:
                        print splits[0].strip(), splits[1].strip()

    except Exception, e:
        print "error is", e


import os
import re
import fcntl
import multiprocessing


def trace_file(root_dir):
    """
    遍历rootDir目录下的所有文件，匹配noah-整数并相加计数
    :param rootDir:
    :return:
    """
    count = 0
    for root, dirs, files in os.walk(root_dir):
        for filespath in files:
            # 通过with方式可以读取大文件，即每次只读取缓冲区大小的文件到内存中
            # 加锁确保任意时刻只有一个进程读取该指定文件
            print os.path.join(root, filespath)
            try:
                with open(os.path.join(root, filespath), 'r') as f:
                    # 对文件加上排它锁与非阻塞锁，即在某时刻该文件只能被一个进程读取，当还有其他进程读取文件时会非阻塞的立即返回
                    # fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)

                    # lines = f.readlines()
                    for line in f:
                        # 在文件的每行中正则提取noah-整数
                        results = re.findall(r'noah-[0-9]+', line)
                        if len(results) > 0:
                            for item in results:
                                try:
                                    count += int(item.split("-")[1])
                                except Exception, e:
                                    print "count error", e
            except Exception, e:
                print "read file error", e
    return count

print trace_file("/home/wtq/test_classes")
# trace_file函数可以实现遍历指定目录下所有大文件并匹配noah-数字,并对所有数字求和的问题。因为文件数量很多所以使用多进程提高文件的读取速度。


def multi_process_read_file(root_dir):
    """
    使用多进程加载trace_file函数，计算所有文件的noah-整数之和
    :param root_dir:
    :return:
    """
    count = 0
    # 申请读取文件时的锁
    lock = multiprocessing.Lock()
    # 设置最大并发进程数为４
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in range(5):
        result.append(pool.apply_async(trace_file, (root_dir, lock)))

    pool.close()
    pool.join()
    for res in result:
        count += res.get()
    return count


if __name__ == "__main__":
    # trace_file("/home/wtq/scripts")
    a = ["123","234","345","5676"]
    b = ["123232","1234","2345","345","5676"]
    print is_subsequence(a, b)
    analyse_config_file("config")
