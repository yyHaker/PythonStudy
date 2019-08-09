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
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 思路： 回溯法, 依次遍历字符串，如果当前子串是回文串，继续递归
        res = []
        self.dfs(0, [], s, res)
        return res

    def dfs(self, start, sub, s, res):
        if start == len(s):
            res.append(sub[:])
        else:
            for end in range(start, len(s)):
                sub_str = s[start:end + 1]
                if sub_str == sub_str[::-1]:
                    self.dfs(end + 1, sub + [sub_str], s, res)


