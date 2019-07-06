#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: first_missing_positive.py
@time: 2019/6/19 21:53
"""


def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    i = 0
    while i < length:
        if nums[i] <= 0 or nums[i] == i + 1 or nums[i] > length:
            i = i + 1
        else:
            # swap nums[i] and nums[nums[i] - 1]
            temp = nums[i]
            nums[i] = nums[temp - 1]
            nums[temp - 1] = temp
            # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    # find first != pos number
    for i in range(length):
        if nums[i] != i + 1:
            return i + 1

nums = [3, 4, -1, 1]
res = firstMissingPositive(nums)
print(res)
