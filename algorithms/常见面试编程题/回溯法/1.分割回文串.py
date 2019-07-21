#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.分割回文串.py
@time: 2019/7/21 11:39
"""
"""
leetcode131: 分割回文串
思路： 使用回溯法
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 定义一个列表，返回最终结果
        split_result = []

        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return
            for end in range(start, len(s)):
                split_s = s[start:end + 1]
                # 如果当前字符串为回文串，则可以继续递归
                if split_s == s[start:end + 1][::-1]:
                    back(end + 1, res + [split_s])

        back()
        return split_result

