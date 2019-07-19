#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.旋转数组中查找指定数字.py
@time: 2019/7/18 10:30
"""
"""
leetcode33: 在旋转有序数组中搜索指定的数字，找到了返回索引，没找到返回-1.
思想：二分法, 时间复杂度为O(logn)
注意边界，具体问题，具体分析
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            # 判断mid是在前面一段还是后面一段
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


