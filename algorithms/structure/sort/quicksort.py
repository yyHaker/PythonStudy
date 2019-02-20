#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: quicksort.py
@time: 2019/2/20 21:42
"""
def quickSort(alist):
    """
    快速排序，时间复杂度为O(nlogn)，最坏的情况为O(n^2)
    :param alist:
    :return:
    """
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    """计算划分点
    :param alist:
    :param first:
    :param last:
    :return:
    """
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    finish = False
    while not finish:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while rightmark >= leftmark and alist[rightmark] > pivotvalue:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            finish = True
        else:
            # swap
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # swap first and rightmark
    temp = alist[rightmark]
    alist[rightmark] = alist[first]
    alist[first] = temp

    return rightmark

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
