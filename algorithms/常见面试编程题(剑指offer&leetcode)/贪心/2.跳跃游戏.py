#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.跳跃游戏.py
@time: 2019/8/20 11:29
"""
"""
leetcode55：跳跃游戏
思路：贪心
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 思路：贪心，维护一个变量reach，表示目前能到达的最远位置，若当前位置i>reach，表示无论如何达不到当前位置，直接返回False；
        # 若遍历完能到达所有位置，则返回True
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True
