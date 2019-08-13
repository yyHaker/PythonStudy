#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 二进制计数.py
@time: 2019/8/11 14:47
"""

def getBinaryCount(num):
    count = 0
    while num:
        if num % 2 == 1:
            count += 1
        num = num // 2
    return count

def classify(nums):
    d = {}
    for m in nums:
        c = getBinaryCount(m)
        if c not in d:
            d[c] = c
    return len(d.keys())

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [int(e) for e in input().split(" ")]
    res = classify(nums)
    print(res)

