#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.分割回文串II（寻找最小的分割次数）.py
@time: 2019/7/22 09:47
"""
"""
leetcode132: 分割回文串II（寻找最小的分割次数）
思路：使用动态规划，d[i][j]表示字符串i-j是否构成回文串，如果是则为1，如果不是则为0；
在求解d的过程中，维护cut,cut[i]表示第i个字符到最后一个字符所构成的子串的最小分割次数
cut[i] = min(1+cut[j+1], cut[i]), if d[i][j] == 1
时间复杂度为O(N^2),空间复杂度为O(N^2)
参考题解：https://blog.csdn.net/Jin_Kwok/article/details/51423222
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [[0] * len(s) for _ in range(len(s))]
        cut = [len(s)] * (len(s) + 1)
        cut[len(s)] = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s), 1):
                if s[i] == s[j] and (j - i <= 1 or d[i + 1][j - 1] == 1):
                    d[i][j] = 1
                    cut[i] = min(1 + cut[j + 1], cut[i])
        return cut[0] - 1
