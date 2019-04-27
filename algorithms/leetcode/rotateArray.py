#!/usr/bin/python
# coding:utf-8

"""旋转数组的最小值
@author: yyhaker
@contact: 572176750@qq.com
@file: rotateArray.py
@time: 2019/3/17 20:59
"""


def minNumberInRotateArray(rotateArray):
    # write code here
    # 二分法
    if len(rotateArray) == 0:
        return 0
    l = 0
    r = len(rotateArray) - 1
    while l < r:
        if rotateArray[l] < rotateArray[r]:
            return rotateArray[l]
        mid = (l + r) // 2
        if rotateArray[mid] > rotateArray[r]:
            l = mid + 1
        elif rotateArray[mid] < rotateArray[r]:
            r = mid
        else:
            l = l + 1
    return rotateArray[l]

A = [3, 4, 5, 1, 2]
print(minNumberInRotateArray(A))

