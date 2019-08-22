#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.通配符匹配.py
@time: 2019/8/20 09:56
"""
"""
leetcode44: 通配符匹配
思路：动态规划
参考：https://blog.csdn.net/weixin_41958153/article/details/80981191
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 思路：动态规划，令dp[i][j]表示s的前i个字符是否与p的前j个字符匹配
        # 时间复杂度为O(mn), 空间复杂度为O(mn)
        # 初始化dp表为False
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True

        # 先填充dp表的第0行和第0列
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        # 继续填充dp表
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    # * 匹配空字符，一个字符，多个字符
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == "?") and dp[i - 1][j - 1]
        return dp[len(s)][len(p)]

