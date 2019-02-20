#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: insertsort.py
@time: 2019/2/20 19:38
"""

def insertSort(alist):
    """
    插入排序算法
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):
        cv = alist[i]
        j = i
        # 插入cv
        while j > 0 and cv < alist[j-1]:
            alist[j] = alist[j-1]  # 后移
            j = j - 1
        alist[j] = cv

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertSort(alist)
    print(alist)


