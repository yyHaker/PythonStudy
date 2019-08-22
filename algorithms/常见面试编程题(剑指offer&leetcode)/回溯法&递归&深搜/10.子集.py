#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.子集.py
@time: 2019/8/7 11:08
"""
"""
leetcode78: 子集合
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯法, 依次求长度为i(1<=i<=n)的组合
        res = []
        self.dfs(0, [], nums, res)
        return res

    def dfs(self, start, sub, nums, res):
        if len(sub) <= len(nums):
            res.append(sub[:])

        for i in range(start, len(nums)):
            self.dfs(i + 1, sub + [nums[i]], nums, res)