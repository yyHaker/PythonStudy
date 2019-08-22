#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.正则表达式匹配.py
@time: 2019/8/20 10:48
"""
"""
leetcode10. 正则表达式匹配
思路：动态规划
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 思路：动态规划，令dp[i][j]表示s的前i个字符与p的前j个字符是否匹配
        # 时间复杂度为O(n^2), 空间复杂度为O(n^2)
        # 初始化dp表为False
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                if j >= 2:
                    dp[0][j] = dp[0][j - 2]
        # 依次填充dp表
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    # * 匹配0个或者多个前面的那一个元素: 匹配0个，匹配1个，匹配多个
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or (
                                dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == "."))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
        return dp[len(s)][len(p)]
