#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7.构建乘积数组.py
@time: 2019/7/17 10:21
"""
"""
剑指offer：构建乘积数组
"""
class Solution:
    def multiply(self, A):
        # write code here
        # 思路：B[i]表示A数组中不包含位置i的所有数据的乘积, 使用两个for循环，
        # 一个累积前面的乘积值，一个累积后面的乘积值；时间复杂度为O(n)
        if len(A) == 0:
            return []
        B = [None] * len(A)
        B[0] = 1
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]

        tmp = 1
        for j in range(len(A) - 2, -1, -1):
            tmp = tmp * A[j + 1]
            B[j] = B[j] * tmp
        return B