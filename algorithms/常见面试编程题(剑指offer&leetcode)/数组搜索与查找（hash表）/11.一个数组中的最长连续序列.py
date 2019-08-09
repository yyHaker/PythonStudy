#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.最长连续序列.py
@time: 2019/7/19 13:49
"""
"""
leetcode128: 找一个数组中的最长连续序列
思路：使用HashSet，因为查找是O(1)。依次遍历每个数字num，如果num-1不在HashSet，序列长度设为1，
        再判断num+1在不在，并递增序列长度；如果num-1在HashSet，直接pass；（因为遍历num-1的时候会计算）
        每次遍历都会更新当前最长的序列长度，最后返回最大的即可。时间复杂度为O(n)，空间复杂度为O(n)。
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_len = 1
                current_num = num

                while current_num + 1 in nums_set:
                    current_len += 1
                    current_num += 1

                res = max(res, current_len)
        return res
