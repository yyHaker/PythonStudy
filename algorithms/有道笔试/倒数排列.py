#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 倒数排列.py
@time: 2019/8/3 15:24
"""
import copy
res = []
from itertools import permutations

n = int(input())
nums = [int(e) for e in input().split(" ")]
# 求解
init = [i for i in range(1, n+1)]
res = [list(e) for e in permutations(init)]
index = res.index(nums)
out = res[len(res)-1-index]
print(" ".join(map(str, out)))

