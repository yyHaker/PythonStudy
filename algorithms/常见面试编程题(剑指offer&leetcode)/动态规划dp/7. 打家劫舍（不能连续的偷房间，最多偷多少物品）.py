#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7. 打家劫舍（不能连续的偷房间，最多偷多少物品）.py
@time: 2019/8/19 15:52
"""
"""
leetcode198: 打家劫舍（不能连续的偷房间，最多偷多少物品）
思路：动态规划
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：动态规划，令d[i]表示遍历到第i个位置时能取到的最大值，则有
        # d[0] = nums[0], i==0
        # d[1] = max(nums[0], nums[1]), i==1
        # d[i] = max(d[i-2]+nums[i], d[i-1]), i>=2
        # 时间复杂度为O(n)，空间复杂度为O(n)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        d = [0] * len(nums)
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            d[i] = max(d[i-2]+nums[i], d[i-1])
        return d[len(nums)-1]

class Solution2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：动态规划+优化使用空间,保存前两个值即可
        # 时间复杂度为O(n), 空间复杂度为O(1)
        prev, cur = 0, 0
        for i in range(len(nums)):
            prev, cur = cur, max(prev+nums[i], cur)
        return cur
