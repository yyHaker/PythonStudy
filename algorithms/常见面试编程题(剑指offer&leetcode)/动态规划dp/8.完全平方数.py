#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.完全平方数.py
@time: 2019/8/19 17:00
"""
"""
leetcode279: 完全平方数
思路：动态规划
思考：有点像背包问题
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路：动态规划，维护一个长度为n+1的数组，第i位存储和为i的最少整数个数，则d[i]只与i之前的数组有关
        # 时间复杂度为O(n^2),空间复杂度为O(n)
        if n == 0:
            return 0
        d = [float("inf")] * (n+1)
        d[0] = 0
        d[1] = 1
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                d[i] = min(d[i], d[i-j*j]+1)
                j = j + 1
        return d[n]
