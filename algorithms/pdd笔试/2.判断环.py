#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.判断环.py
@time: 2019/7/28 15:36
"""

import sys

def is_cycle(strs):
    # 存字符串，判断头和尾
    res = {}
    for s in strs:
        h, t = s[0], s[-1]
        res[h] = t
    # 判断是否有环
    h, t = strs[0][0], strs[0][-1]
    tag = h
    while t != tag:
        if t not in res:
            print("false")
            return
        else:
            t = res[t]
    print("true")

line = sys.stdin.readline().strip()
strs = line.split(" ")
# strs = "CAT TIGER RPC".split()
# strs2 = "CAT RPC".split()

is_cycle(strs)