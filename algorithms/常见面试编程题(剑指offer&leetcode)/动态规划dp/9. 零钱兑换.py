#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 9. 零钱兑换.py
@time: 2019/8/19 17:34
"""
"""
leetcode322: 零钱兑换

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 思路：动态规划，令d[i]表示以i为总金额的最少的硬币的个数
        # 则有d[i] = min(d[i], d[i-j]+1)
        d = [float("inf")] * (amount + 1)
        d[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if j <= i:
                    d[i] = min(d[i], d[i - j] + 1)
        if d[amount] == float("inf"):
            return -1
        else:
            return d[amount]
