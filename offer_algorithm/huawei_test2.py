# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

第一题: 有序的二维数组的查找
def find_num(array, value):
    """
    问题:  二维有序的数组中查找是否包含value。
    思路: 首先选取数组右上角的数字，如果该数字等于要查找的数字，则查找结束；如果该数字大于要查找的数字，
    剔除这个数字所在的列，如果该数字小于要查找的数字，剔除这个数字所在的行。这样每一步都可以剔除一行或一列。
    :param array: 输入的二维数组
    :param value: 查找的目标值
    :return:包含返回True 不包含返回False
    """
    if array is None:
        return False
    i = 0
    j = len(array[0]) - 1
    max_i = len(array) - 1
    while i <= max_i and j >= 0:
        if array[i][j] == value:
            return True
        elif array[i][j] > value:
            j = j - 1
        else:
            i = i + 1
    return False


第二题: TB级的数据排序
"""
文件的大小为TB级的，整数个数为N，整数之间用空格分开。首先分多次从该文件中读取M（十万级）个整数，

每次将M个数据在内存中使用快排序之后存入临时文件，然后使用多路归并将临时文件中的数据排好序

存入输出文件。

下面代码是基于以上思想对包含大整数文件的从小到大排序的一个简单实现，这里没有使用内存缓

冲区，在归并时简单使用一个数组来存储每个临时文件的第一个元素。
"""

/*********使用多路归并进行外排序的类*************/

//ExternSort.h

/*
* 大数据量的排序
* 多路归并排序
* 以千万级整数从小到大排序为例
* 一个比较简单的例子，没有建立内存缓冲区
*/

#ifndef EXTERN_SORT_H
#define EXTERN_SORT_H

#include <cassert>

class ExternSort
{
public:
        void sort()
        {
                time_t start = time(NULL);

                //将文件内容分块在内存中排序，并分别写入临时文件
                int file_count = memory_sort();

                //归并临时文件内容到输出文件
                merge_sort(file_count);

                time_t end = time(NULL);
                printf("total time:%f\n", (end - start) * 1000.0/ CLOCKS_PER_SEC);
        }

        //input_file:输入文件名
        //out_file:输出文件名
        //count: 每次在内存中排序的整数个数
        ExternSort(const char *input_file, const char * out_file, int count)
        {
                m_count = count;
                m_in_file = new char[strlen(input_file) + 1];
                strcpy(m_in_file, input_file);
                m_out_file = new char[strlen(out_file) + 1];
                strcpy(m_out_file, out_file);
        }
        virtual ~ExternSort()
        {
                delete [] m_in_file;
                delete [] m_out_file;
        }

private:
        int m_count; //数组长度
        char *m_in_file;   //输入文件的路径
        char *m_out_file; //输出文件的路径
protected:
        int read_data(FILE* f, int a[], int n)
        {
                int i = 0;
                while(i < n && (fscanf(f, "%d", &a[i]) != EOF)) i++;
                printf("read:%d integer\n", i);
                return i;
        }
        void write_data(FILE* f, int a[], int n)
        {
                for(int i = 0; i < n; ++i)
                        fprintf(f, "%d ", a[i]);
        }
        char* temp_filename(int index)
        {
                char *tempfile = new char[100];
                sprintf(tempfile, "temp%d.txt", index);
                return tempfile;
        }
        static int cmp_int(const void *a, const void *b)
        {
                return *(int*)a - *(int*)b;
        }

        int memory_sort()
        {
                FILE* fin = fopen(m_in_file, "rt");
                int n = 0, file_count = 0;
                int *array = new int[m_count];
                //每读入m_count个整数就在内存中做一次排序，并写入临时文件
                while(( n = read_data(fin, array, m_count)) > 0)
                {
                        qsort(array, n, sizeof(int), cmp_int);
                        char *fileName = temp_filename(file_count++);
                        FILE *tempFile = fopen(fileName, "w");
                        free(fileName);
                        write_data(tempFile, array, n);
                        fclose(tempFile);
                }
                delete [] array;
                fclose(fin);

                return file_count;
        }

        void merge_sort(int file_count)
        {
                if(file_count <= 0) return;
                //归并临时文件
                FILE *fout = fopen(m_out_file, "wt");
                FILE　**farray = new FILE*[file_count];
                int i;
                for(i = 0; i < file_count; ++i)
                {
                        char* fileName = temp_filename(i);
                        farray[i] = fopen(fileName, "rt");
                        free(fileName);
                }

                int *data = new int[file_count];//存储每个文件当前的一个数字
                bool *hasNext = new bool[file_count];//标记文件是否读完
                memset(data, 0, sizeof(int) * file_count);
                memset(hasNext, 1, sizeof(bool) * file_count);

                for(i = 0; i < file_count; ++i)
                {
                        if(fscanf(farray[i], "%d", &data[i]) == EOF)//读每个文件的第一个数到data数组
                                hasNext[i] = false;
                }
                while(true)
                {
                        //求data中可用的最小的数字，并记录对应文件的索引
                        int max = data[0];
                        int j = 0;
                        for(i = 0; i < file_count; ++i)
                        {
                                if(hasNext[i] && max > data[i])
                                {
                                        max = data[i];
                                        j = i;
                                }
                        }
                        if(j == 0 && !hasNext[0]) break; //没有可取的数字，终止归并

                        if(fscanf(farray[j], "%d", &data[j]) == EOF) //读取文件的下一个元素
                                hasNext[j] = false;
                        fprintf(fout, "%d ", max);

                }

                delete [] hasNext;
                delete [] data;

                for(i = 0; i < file_count; ++i)
                {
                        fclose(farray[i]);
                }
                delete [] farray;
                fclose(fout);
        }
};

#endif

/**************测试主函数文件*****************************************/

/*
* 大文件排序
* 数据不能一次性全部装入内存
* 排序文件里有多个整数，整数之间用空格隔开
*/

#include <iostream>
#include <ctime>
#include <fstream>
#include "ExternSort.h"
using namespace std;

const unsigned int count = 100000000; // 文件里数据的行数

const unsigned int number_to_sort = 1000000; //在内存中一次排序的数量

const char *unsort_file = "unsort_data.txt"; //原始未排序的文件名

const char *sort_file = "sort_data.txt"; //已排序的文件名

void init_data(unsigned int num); //随机生成数据文件

int main(int argc, char* *argv)
{
        srand(time(NULL));
        init_data(count);
        ExternSort extSort(unsort_file, sort_file, number_to_sort);
        extSort.sort();
        system("pause");
        return 0;
}

void init_data(unsigned int num)
{
        FILE* f = fopen(unsort_file, "wt");
        for(int i = 0; i < num; ++i)
                fprintf(f, "%d ", rand());
        fclose(f);
}


第三题：
答案：赢的比赛数占所有的比赛数的比例为1:2
原因：根据题意每天进行k次比赛的概率p= 1/2的k次幂，服从几何分布，所以期望为２，即平均每天比两次有一次获胜，所以赢的比赛数占所有的比赛数的比例为1:2
