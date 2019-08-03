#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.搭积木.py
@time: 2019/7/28 16:22
"""


def dajimu(N, L, W):
    s = []
    for l, w in zip(L, W):
        s.append((l, w))
    s = sorted(s, key=lambda x: x[0], reverse=True)
    # 依次搭积木
    count = 0
    for i, b in enumerate(s):
        l, w = b[0], b[1]

    return None



N = 10
L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
W = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]
res = dajimu(N, L, W)
print(res)