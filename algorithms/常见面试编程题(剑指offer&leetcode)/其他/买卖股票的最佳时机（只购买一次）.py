#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 买卖股票的最佳时机.py
@time: 2019/8/16 20:49
"""
"""
leetcode121: 买卖股票的最佳时机
思路：依次遍历数组，遍历的过程中维护i位置之前的最小值，计算截止到i位置的最大收益
时间复杂度为O(n)，空间复杂度为O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 思路：依次遍历数组，遍历的过程中维护i位置之前的最小值，计算截止到i位置的最大收益，
        if len(prices) < 2:
            return 0
        minv = prices[0]
        max_res = 0
        for i in range(1, len(prices)):
            if prices[i] - minv > max_res:
                max_res = prices[i] - minv
            # update miv
            if prices[i] < minv:
                minv = prices[i]
        return max_res
