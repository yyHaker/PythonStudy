#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 翻转单词序列.py
@time: 2019/7/5 21:27
"""
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0 or len(s) == 1:
            return s
        s = s.split(" ")
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return " ".join(s)