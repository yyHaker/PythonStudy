#!/usr/bin/python
# coding:utf-8

"""二分查找
@author: yyhaker
@contact: 572176750@qq.com
@file: binarySearch.py
@time: 2019/2/20 10:49
"""
def binarySearch(alist, k):
    """普通版本的二分查找
    :param alist:
    :param k:
    :return:
    """
    left = 0
    right = len(alist) - 1
    while left <= right:
        mid = (left + right) // 2
        if k == alist[mid]:
            return mid
        elif k < alist[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binarySearch_fz(alist, item):
    """分治版本的二分查找，时间复杂度O(logn)
    :param alist:
    :param item:
    :return:
    """
    if len(alist) == 0:
        return False
    else:
        first = 0
        last = len(alist) - 1
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item > alist[mid]:
            return binarySearch_fz(alist[mid+1:], item)
        else:
            return binarySearch_fz(alist[:mid], item)

def binarySearch_yesleft(alist, k):
    """
    找到并且返回最左边的位置, 没有找到就返回右边最接近的位置.
    :param alist:
    :param k:
    :return:
    """
    left = 0
    right = len(alist) - 1
    while left <= right:
        mid = (left + right) // 2
        if k <= alist[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left

def binarySearch_yesright(alist, k):
    """
    找到并且返回最右边的位置，没有找到就返回左边最接近的位置.
    :param alist:
    :param k:
    :return:
    """
    left = 0
    right = len(alist) - 1
    while left <= right:
        mid = (left + right) // 2
        if k < alist[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right


if __name__ == "__main__":
    nums = [1, 2, 2, 4, 4, 8, 10]
    nums = [4, 4]
    res = binarySearch(nums, 3)
    print(res)
    print("*"*5)
    res = binarySearch_yesright(nums, 3)
    print(res)
