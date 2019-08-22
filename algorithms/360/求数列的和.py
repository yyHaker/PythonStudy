#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 求数列的和.py
@time: 2019/8/15 15:07
"""
import math
nums = [int(e) for e in input().split(" ")]
n, m = nums[0], nums[1]
def get_sum(n, m):
        res = []
        res.append(n)
        for _ in range(m-1):
            t = math.sqrt(res[-1])
            res.append(t)
        return '{:.2f}'.format(sum(res))

res = get_sum(n, m)
print(res)