#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.求一个整数数组的乘积最大子序列.py
@time: 2019/8/19 15:25
"""
"""
leetcode152: 求一个整数数组的乘积最大子序列
思路：动态规划
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：动态规划，分析发现某个位置可能会出现0或者负数，当遇到0的时候，整个乘积会变为0；
        # 当遇到负数的时候，当前的最大乘积会变为最小乘积，最小乘积会变为最大乘积；
        # 令f[i]表示以nums[i]结尾的乘积最大的连续子序列，g[i]表示以nums[i]结尾的乘积最小的连续子序列，
        # 则f[i] = max(f[i-1]*nums[i], nums[i], g[i-1]*nums[i])
        #   g[i] = max(g[i-1]*nums[i], nums[i], f[i-1]*nums[i])
        # 时间复杂度为O(n)，空间复杂度为O(n)
        res = nums[0]
        f = [float('-inf')] * len(nums)
        g = [float('inf')] * len(nums)
        f[0] = nums[0]
        g[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            g[i] = min(g[i - 1] * nums[i], nums[i], f[i - 1] * nums[i])
            res = max(res, f[i])
        return res

