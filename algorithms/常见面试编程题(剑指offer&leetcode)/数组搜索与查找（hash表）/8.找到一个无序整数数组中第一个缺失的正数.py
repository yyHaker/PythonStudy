#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.找到一个无序整数数组中第一个缺失的正数.py
@time: 2019/7/18 20:24
"""
"""
leetocde41: 找到一个无序整数数组中第一个缺失的正数
思路：遍历数组，如果第i个数字length>=nums[i]>0, 放到第nums[i]-1的位置;
最后再遍历一次数组，判断第i个位置的数字nums[i]是否等于i+1，从而找到第一个缺失的正数.
时间复杂度为O(n)，空间复杂度为O(1)
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        # find first != pos number
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length + 1