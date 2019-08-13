#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.全排列.py
@time: 2019/8/5 20:18
"""
"""
leetcode46: 全排列

注意：
【1】python切片复制、浅拷贝、较深拷贝、深拷贝: https://blog.csdn.net/a5186050/article/details/78055718
"""
class Solution:
    def permute(self, nums):
        # 思路：回溯法
        res = []
        sub = []
        self.dfs(nums, sub, res)
        return res

    def dfs(self, nums, sub, res):
        if len(sub) == len(nums):
            res.append(sub[:])
            return
        else:
            for m in nums:
                if m in sub:
                    continue
                sub.append(m)
                self.dfs(nums, sub, res)
                sub.remove(m)

solution = Solution()
nums = [1, 2, 3]
res = solution.permute(nums)
print(res)


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 思路：回溯法, 基于交换的思想
        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, m, res):
        if m == len(nums) - 1:
            res.append(nums[:])
        else:
            for i in range(m, len(nums)):
                nums[i], nums[m] = nums[m], nums[i]
                self.dfs(nums, m + 1, res)
                nums[i], nums[m] = nums[m], nums[i]





