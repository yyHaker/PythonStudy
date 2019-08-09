#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 14.求一个字符串的最长回文子串.py
@time: 2019/7/26 22:51
"""
"""
leetcode5: 求一个字符串的最长回文子串
思路： 动态规划
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：动态规划， d[i,j] = s[i] == s[j] , if j-i<=1;
        #               d[i,j] = s[i] == s[j] and d[i+1,j-1], if j-i > 1
        # 时间复杂度为O(N^2)，空间复杂度为O(N^2)
        res = ""
        sub_length = 0
        d = [[0] * len(s) for _ in range(len(s))]
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        d[i][j] = 1
                else:
                    if s[i] == s[j] and d[i + 1][j - 1]:
                        d[i][j] = 1
                # 更新最长回文子串
                if d[i][j] and j - i + 1 > sub_length:
                    sub_length = j - i + 1
                    res = s[i:j + 1]
        return res


