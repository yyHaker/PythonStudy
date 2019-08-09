#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 14.求一个字符串中第一个唯一的字符.py
@time: 2019/7/20 18:14
"""
"""
leetcode387: 求一个字符串中第一个唯一的字符
思路：使用hash map
时间复杂度为O(N), 空间复杂度为O(N)
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(s)

        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1