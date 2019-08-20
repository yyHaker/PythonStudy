#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5. 不同路径.py
@time: 2019/8/19 14:52
"""
"""
leetcode62：不同路径
思路：动态规划
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 思路：动态规划，令d[i][j]表示机器人能够到达位置(i, j)的路径条数，
        # 则有d[i][j] = max(d[i-1][j], d[i][j-1])
        # 时间复杂度为O(mn),空间复杂度为O(mn)
        d = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]