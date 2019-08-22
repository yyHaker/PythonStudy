#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 字符串的解码.py
@time: 2019/8/20 19:18
"""

def decode(s):
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]

s = input().strip()
res = decode(s)
print(res)
