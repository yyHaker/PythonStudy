#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 15. 移动零.py
@time: 2019/8/14 10:29
"""
"""
leetcode283: 移动零
思路：双指针
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：双指针
        # 时间复杂度为O(n), 空间复杂度为O(1)
        new_tail = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                new_tail += 1
                nums[new_tail] = nums[i]
        for i in range(new_tail + 1, len(nums)):
            nums[i] = 0

