#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: mergeSort.py
@time: 2019/2/20 21:23
"""
def mergeSort(alist):
    """
    归并排序，时间复杂度为O(nlogn)
    :param alist:
    :return:
    """
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        # merge left and right
        i = 0
        j = 0
        k = 0  # merge后的下标
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        # left有剩余
        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1
        # right有剩余
        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)