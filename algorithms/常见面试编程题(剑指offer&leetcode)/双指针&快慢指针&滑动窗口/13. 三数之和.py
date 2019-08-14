#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 13. 三数之和.py
@time: 2019/8/13 22:15
"""
"""
leetcode15: 三数之和
思路：排序+双指针
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 思路: 排序 + 双指针
        N = len(nums)
        nums.sort()
        res = []
        for t in range(N-2):
            if t > 0 and nums[t] == nums[t-1]:
                continue
            i, j = t+1, N-1
            # 双指针
            while i < j:
                tmp = nums[t] + nums[i] + nums[j]
                if tmp == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # 去重
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1
                elif tmp < 0:
                    i += 1
                else:
                    j -= 1
        return res
