#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 9.电话号码的字母组合.py
@time: 2019/8/7 10:36
"""
"""
leetcode 17 : 电话号码的字母组合
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        d = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
             "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        self.dfs(0, "", digits, d, res)
        return res

    def dfs(self, i, sub, digits, d, res):
        if i == len(digits):
            res.append(sub[:])
        else:
            for ch in d[digits[i]]:
                self.dfs(i + 1, sub + ch, digits, d, res)
