#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.求一个数组的最长连续子序列的长度.py
@time: 2019/8/22 19:47
"""
"""
例如：[1, 2, 3, 2, 5, 5, 6, 7, 8]的最长连续子序列为[5, 6, 7, 8], 长度为4
思路：
【1】直接遍历，记录当前连续长度最长的
【2】动态规划
"""
class Solution(object):
    def las(self, nums):
        # 思路：动态规划，令dp[i]表示以nums[i]结尾的最长连续递增子序列的长度, dp[i] = dp[i-1] + 1, if nums[i] > nums[i-1]
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)

nums = [1, 2, 3, 2, 5, 5, 6, 7, 8]
solution = Solution()
res = solution.las(nums)
print(res)
