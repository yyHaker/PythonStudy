#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7.求Pow(x, n).py
@time: 2019/8/18 15:22
"""
"""
leetcode50: 求Pow(x)
思路：将结果表示成指数相乘的形式，时间复杂度为O(logn)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 思路：位运算，例如求x^10 = x^(2^3) * x^(2^1)
        res = 1
        # 指数为负数
        if n < 0:
            x = 1.0 / x
            n = -n
        # 将结果表示成指数相乘的形式，时间复杂度为O(logn)
        res = 1.0
        while n > 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n >> 1
        return res
