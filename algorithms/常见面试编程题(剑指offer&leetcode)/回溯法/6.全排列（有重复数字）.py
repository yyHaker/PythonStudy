#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.全排列（有重复数字）.py
@time: 2019/8/5 22:21
"""
"""
leetcode47: 全排列II，
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯法, 基于交换的思想, 依次交换数字，由于有重复，将处理的数字放到一个list中，如果之前已经出现过，就不需要处理
        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, m, res):
        if m == len(nums) - 1:
            res.append(nums[:])
        else:
            flag = []
            for i in range(m, len(nums)):
                if nums[i] not in flag:
                    flag.append(nums[i])
                    # 交换
                    nums[i], nums[m] = nums[m], nums[i]
                    self.dfs(nums, m + 1, res)
                    nums[m], nums[i] = nums[i], nums[m]

