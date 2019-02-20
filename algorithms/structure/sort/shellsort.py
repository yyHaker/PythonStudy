#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: shellsort.py
@time: 2019/2/20 20:26
"""

"""
希尔排序的实质就是分组插入排序，该方法又称缩小增量排序，因DL．Shell于1959年提出而得名。
该方法的基本思想是：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。
"""

def shellSort(alist):
    """
    希尔排序.  时间复杂度落在O(n) 和 O(n^2)
    :param alist:
    :return:
    """
    gap = len(alist) // 2
    while gap > 0:
        # 分组插入排序
        for s in range(gap):
            gapInsertSort(alist, s, gap)
        gap = gap // 2

def gapInsertSort(alist, start, gap):
    """
    增量插入排序.
    :param alist:
    :param start:
    :param gap: 增量
    :return:
    """
    for i in range(start+gap, len(alist), gap):
        cv = alist[i]
        position = i
        while position >= gap and cv < alist[position - gap]:
            alist[position] = alist[position - gap]  # 右移
            position = position - gap
        alist[position] = cv

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)
