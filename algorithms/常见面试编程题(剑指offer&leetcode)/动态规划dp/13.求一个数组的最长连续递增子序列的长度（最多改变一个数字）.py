#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 13.求一个数组的最长连续子序列的长度（最多改变一个数字）.py
@time: 2019/8/22 19:48
"""
"""
例如：[1, 2, 3, 2, 5, 5, 6, 7, 8]的最长连续子序列为[2, 3, 6, 7, 8], 长度为6
思路：动态规划真的是太神奇了！
"""
class Solution(object):
    def las(self, nums):
        # 思路：动态规划，令pre[i]表示以nums[i]结尾的最大连续递增子序列的长度，
        # 令last[i]表示以nums[i]为起点的最大连续递增子序列的长度，比较下标i-1位置和i+1位置的元素差值是否大于2，如果大于2则拼接长度
        # 时间复杂度为O(n)，空间复杂度为O(n)
        #
        pre = [1] * len(nums)
        last = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pre[i] = pre[i-1] + 1

        for j in range(len(nums)-2, -1, -1):
            if nums[j] < nums[j+1]:
                last[j] = last[j+1] + 1

        res = 1
        for i in range(1, len(nums)-2):
            res = max(res, pre[i])
            res = max(res, last[i])
            if nums[i+1] - nums[i-1] >= 2:
                res = max(res, pre[i-1] + 1 + last[i+1])
        return res

nums = [1, 2, 3, 2, 5, 5, 6, 7, 8]
solution = Solution()
res = solution.las(nums)
print(res)




