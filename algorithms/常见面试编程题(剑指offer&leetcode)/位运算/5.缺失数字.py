#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.缺失数字.py
@time: 2019/8/23 21:35
"""
"""
leetcode268: 缺失数字
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路一：求和，减法
        # Time:O(n), Space: O(1)
        n = len(nums)
        num_sum = sum(nums)
        return n * (n+1) / 2 - num_sum


class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路二：异或操作, 相同为0不同为1
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

