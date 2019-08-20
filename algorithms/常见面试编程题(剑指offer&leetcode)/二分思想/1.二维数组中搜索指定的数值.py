#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.二维数组中的查找.py
@time: 2019/7/14 10:02
"""
"""
 剑指offer： 二维数组中的查找
 leetcode240: 搜索二维矩阵 II
 leetcode74: 搜索二维矩阵
 思想： 二分思想
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 思路：从左下角开始查找，遇大则右移，遇小则上移。
        rows = len(array)
        column = len(array[0])
        i, j = rows - 1, 0
        while i >= 0 and j <= column - 1:
            if target > array[i][j]:
                j = j + 1
            elif target < array[i][j]:
                i = i - 1
            else:
                return True
        return False
