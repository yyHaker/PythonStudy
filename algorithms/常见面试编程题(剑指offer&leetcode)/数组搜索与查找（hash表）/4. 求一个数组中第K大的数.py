#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4. 求一个数组中第K大的数.py
@time: 2019/7/14 22:23
"""
"""
leetcode:215：求一个数组中第k大的数
思路：快速选择，利用快排的第一步思想。平均时间复杂度为O(n), 空间复杂度为O(1)
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        n = len(nums)
        while low <= high:
            p = self.partition(nums, low, high)
            if p == n - k:
                return nums[p]
            elif p > n - k:
                high = p - 1
            else:
                low = p + 1

    def partition(self, nums, low, high):
        # 二路划分
        pivot = nums[high]
        start = low
        for i in range(low, high):
            if nums[i] < pivot:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
        nums[start], nums[high] = nums[high], nums[start]
        return start
