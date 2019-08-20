#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 买股票的最佳时机II（可购买无限次数）.py
@time: 2019/8/16 20:56
"""
"""
leetcode122: 买股票的最佳时机II（可购买无限次数）
思路：双指针，贪心算法购买
时间复杂度为O(n), 空间复杂度为O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 思路：双指针，贪心算法购买
        # 时间复杂度为O(n), 空间复杂度为O(1)
        res = 0
        slow = 0
        fast = 0
        while fast < len(prices):
            # move fast
            while fast + 1 < len(prices) and prices[fast] < prices[fast + 1]:
                fast = fast + 1
            res += prices[fast] - prices[slow]
            # move slow
            slow = fast + 1
            fast = fast + 1
        return res

