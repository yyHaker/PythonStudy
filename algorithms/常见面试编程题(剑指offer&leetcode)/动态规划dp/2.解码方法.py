#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.解码方法.py
@time: 2019/8/3 22:02
"""
"""
leetcode91: 解码方法
思路：动态规划
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        # 思路：动态规划，令dp[i]表示到第i-1位时的字符串的解码方法总数，dp[i] = dp[i-1] + dp[i-2]；
        # 另外，s[i-1]单独解码，方法数量为dp[i-1];
        #      s[i-2:i]拼接解码，若10<=s[i-2:i]<=26，双字符合格，解码方法数量为dp[i-2],不合格则为0
        # 初始化, dp[0] = dp[1] = 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

solution = Solution()
s = "12"
res = solution.numDecodings(s)
print(res)
