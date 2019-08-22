#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 拔栏杆.py
@time: 2019/8/17 20:31
"""

def get_len(n, k, nums):
    minval = float("inf")
    min_idx = -1
    for i in range(n-k):
        cur = sum(nums[i: i+k])
        if cur < minval:
            minval = cur
            min_idx = i
    return min_idx+1

def get_length(n, k, nums):
    slow, fast = 0, 0
    minval = float("inf")
    min_idx = -1
    cur = 0
    #  fast
    for _ in range(k):
        cur += nums[fast]
        fast += 1
    # slow and fast
    while fast < n:
        if cur < minval:
            minval = cur
            min_idx = slow
        fast += 1
        if fast >= n:
            break
        cur += nums[fast]
        cur -= nums[slow]
        slow += 1
    return min_idx+1

p = [int(e) for e in input().split(" ")]
n, k = p[0], p[1]
nums = [int(e) for e in input().split(" ")]
res = get_length(n, k, nums)
print(res)
