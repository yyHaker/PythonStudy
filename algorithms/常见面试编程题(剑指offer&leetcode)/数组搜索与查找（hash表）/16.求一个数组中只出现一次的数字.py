#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 16.求一个数组中只出现一次的数字.py
@time: 2019/8/23 15:19
"""
"""
leetcode136: 求一个数组中只出现一次的数字
思路：异或运算
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：异或运算，得到所有元素的异或结果，即只出现一次
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
