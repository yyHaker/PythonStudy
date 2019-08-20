#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.寻找峰值.py
@time: 2019/8/18 15:48
"""
"""
leetcode162: 寻找峰值
思路：二分查找，判断是在上坡还是下坡来缩小查找空间
时间复杂度为O(logn)
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：二分查找，判断是在上坡还是下坡来缩小查找空间
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l
