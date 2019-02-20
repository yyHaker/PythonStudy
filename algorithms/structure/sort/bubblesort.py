#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: bubblesort.py
@time: 2019/2/20 18:34
"""
def bubbleSort(alist):
    """冒泡排序，时间复杂度O(n^2)
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):  # i表示迭代次数
        for j in range(len(alist) - i):  # j表示下标
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

def shortBubbleSort(alist):
    """短冒泡排序，如果发现列表已经排序，则提前停止列表
    :param alist:
    :return:
    """
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1




if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)

