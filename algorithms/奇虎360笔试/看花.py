#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 看花.py
@time: 2019/8/15 16:55
"""
def get_flowers(l, r, flowers):
    return len(set(flowers[l: r+1]))

p = [int(e) for e in input().split(" ")]
n, m = p[0], p[1]
flowers = [int(e) for e in input().split(" ")]
flowers.insert(0, 0)
Q = int(input())
for _ in range(Q):
    q = [int(e) for e in input().split(" ")]
    l, r = q[0], q[1]
    res = get_flowers(l, r, flowers)
    print(res)