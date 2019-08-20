#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.最大子序和.py
@time: 2019/8/19 14:32
"""
"""
leetcode53: 最大子序和
思路：动态规划
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：动态规划，令d[i]表示表示以nums[i]结尾的最大连续子数组的和，
        # 则有d[i] = max(d[i-1]+nums[i], nums[i])
        # 时间复杂度为O(n),空间复杂度为O(n)
        res = nums[0]
        d = [float("inf")] * len(nums)
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = max(d[i-1]+nums[i], nums[i])
            if d[i] > res:
                res = d[i]
        return res
