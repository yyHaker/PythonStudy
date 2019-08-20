#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 买卖股票的最佳时机III（可以购两次）.py
@time: 2019/8/16 21:44
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 思路：双指针，维护两个指针i, j；i之前的买一次，i-j买一次
        # 时间复杂度为 O(n^2), （超时没过）
        max_res = 0
        i, j = 0, 0
        # 移动i
        mini = float("inf")
        while i < len(prices):
            if prices[i] < mini:
                mini = prices[i]
            ans1 = prices[i] - mini
            max_res = max(max_res, ans1)

            i += 1

            # 移动j
            j = i
            minj = float("inf")
            while j < len(prices):
                if prices[j] < minj:
                    minj = prices[j]
                ans2 = prices[j] - minj
                max_res = max(max_res, ans1 + ans2)
                j += 1
        return max_res


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 思路：遍历两次prices， 从左到右遍历，LM[i]表示i之前的最大收益；
        # 从右到左遍历，RM[i]表示i之后的最大收益;
        # 最后再遍历一遍，取LM[i] + RM[i+1]的最大值
        # 时间复杂度为O(n), 空间复杂度为O(n)
        LM = [0] * len(prices)
        minval = float('inf')
        cur_max = 0
        for i in range(len(prices)):
            if prices[i] < minval:
                minval = prices[i]
            cur_max = max(cur_max, prices[i] - minval)
            LM[i] = cur_max

        RM = [0] * len(prices)
        max_val = -1
        cur_max = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_val:
                max_val = prices[i]
            cur_max = max(cur_max, max_val - prices[i])
            RM[i] = cur_max

        max_res = 0
        for i in range(len(prices)):
            if i + 1 < len(prices):
                max_res = max(max_res, LM[i] + RM[i + 1])
            else:
                max_res = max(max_res, LM[i])
        return max_res


nums = [0, 3, 7, 5, 9, 1, 100]
nums2 = [3, 3, 5, 0, 0, 3, 1, 4]
nums3 = [3, 2, 6, 5, 0, 3]
solution = Solution2()
res = solution.maxProfit(nums3)
print(res)
