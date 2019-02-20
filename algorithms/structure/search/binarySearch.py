#!/usr/bin/python
# coding:utf-8

"""二分查找
@author: yyhaker
@contact: 572176750@qq.com
@file: binarySearch.py
@time: 2019/2/20 10:49
"""
def binarySearch(alist, item):
    """普通版本的二分查找
    :param alist:
    :param item:
    :return:
    """
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        elif item > alist[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return found

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

if __name__ == "__main__":
    print(binarySearch_fz([1, 2, 3, 4, 5, 6, 7], 8))
