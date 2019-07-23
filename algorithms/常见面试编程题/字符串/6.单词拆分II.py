#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.单词拆分II.py
@time: 2019/7/23 14:51
"""
"""
leetcode140: 单词拆分II
思路：一般像求解所有结果使用递归。定义一个dfs，表示字符串s能被字典中的元素构成的所有字符串（中间以空格分开）
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = {}
        return self.dfs(s, wordDict, res, memo)

    def dfs(self, s, wordDict, res, memo):
        if s in memo:
            return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for r in self.dfs(s[len(word):], wordDict, res, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res
