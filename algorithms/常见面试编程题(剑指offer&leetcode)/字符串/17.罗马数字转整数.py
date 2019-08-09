#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 17.罗马数字转整数.py
@time: 2019/8/3 22:23
"""
"""
leetcode13: 罗马数字转整数
思路：从后向前遍历，依次累加值
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = roman[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res