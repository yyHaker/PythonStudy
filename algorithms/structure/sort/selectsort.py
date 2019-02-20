#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: selectsort.py
@time: 2019/2/20 19:13
"""

def selectSort(alist):
    """
    选择排序，时间复杂度是O(n^2)
    :param alist:
    :return:
    """
    for i in range(1, len(alist)):  # passnum
        max_idx = 0
        for j in range(1, len(alist) - i+1):
            if alist[j] > alist[max_idx]:
                max_idx = j
        # swap
        temp = alist[max_idx]
        alist[max_idx] = alist[len(alist) - i]
        alist[len(alist) - i] = temp


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectSort(alist)
    print(alist)


