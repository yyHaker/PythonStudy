#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7.反转字符串.py
@time: 2019/7/23 20:00
"""
"""
leetcode344: 字符串反转
思路：双指针
时间复杂度为O(N),空间复杂度为O(1)
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
