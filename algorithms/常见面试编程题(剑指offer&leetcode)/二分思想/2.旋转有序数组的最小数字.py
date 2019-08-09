#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.旋转数组的最小数字.py
@time: 2019/7/14 10:26
"""
"""
剑指offer：旋转数组的最小数字
思路：二分法，旋转数组实际上是两个有序的数组, 时间复杂度为O(logn)
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid = (l + r) // 2
            if rotateArray[mid] > rotateArray[r]:
                l = mid + 1
            elif rotateArray[mid] < rotateArray[r]:
                r = mid
            else:
                l = l + 1
        return rotateArray[l]

