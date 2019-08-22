#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.子集II.py
@time: 2019/8/7 11:28
"""
"""
leetcode90: 子集II
思路：回溯法，注意重复的情况
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯法，注意重复情况处理
        res = []
        nums = sorted(nums)
        self.dfs(0, [], nums, res)
        return res

    def dfs(self, start, sub, nums, res):
        if len(sub) <= len(nums):
            res.append(sub[:])

        for i in range(start, len(nums)):
            # 在每次递归求解的过程中，剪枝
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.dfs(i + 1, sub + [nums[i]], nums, res)

