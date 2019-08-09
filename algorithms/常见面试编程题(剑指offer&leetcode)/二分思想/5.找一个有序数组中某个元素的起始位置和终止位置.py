#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.找一个有序数组中某个元素的起始位置和终止位置.py
@time: 2019/7/18 11:44
"""
"""
leetcode34: 找一个有序数组中某个元素的起始位置和终止位置
思想：二分法, 时间复杂度为O(logn)
分别使用两个二分查找找到起始位置和终止位置
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        # find left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if left > len(nums) - 1 or nums[left] != target:
            return [-1, -1]
        start = left

        # find right
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        end = right
        return [start, end]
