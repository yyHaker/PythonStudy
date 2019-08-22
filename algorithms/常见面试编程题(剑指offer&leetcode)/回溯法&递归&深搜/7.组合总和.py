#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7.组合总和.py
@time: 2019/8/6 09:54
"""
"""
leetcode39: 组合综合
"""
class Solution:
    def combinationSum(self, candidates, target):
        # 思路：回溯法，依次添加数字, 每次从start位置进行搜索(这个可以保证每个数字仅仅使用一次并且方便利用剪枝防止重复)
        # 注意：防止重复;并且保证每个数字只能添加一次
        res = []
        cur = []
        candidates = sorted(candidates)
        start = 0
        self.dfs(candidates, cur, start, target, res)
        return res

    def dfs(self, candidates, cur, start, target, res):
        if sum(cur) == target:
            res.append(cur[:])
            return
        else:
            for i in range(start, len(candidates)):
                # 剪枝，防止chongfu
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                m = candidates[i]
                if sum(cur) + m <= target:
                    self.dfs(candidates, cur + [m], i + 1, target, res)

solution = Solution()
res = solution.combinationSum([2, 5, 2, 1, 2], 5)
print(res)
