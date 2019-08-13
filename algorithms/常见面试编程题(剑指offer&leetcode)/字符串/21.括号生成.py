#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 21.括号生成.py
@time: 2019/8/5 09:41
"""
"""
leetcode22: 括号生成
思路：回溯法
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, n, n, "")
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + "(")
        # (的个数大于等于)的个数时，添加右括号
        if left < right:
            self.dfs(res, left, right - 1, path + ")")

