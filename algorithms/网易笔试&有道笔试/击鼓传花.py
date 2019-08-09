#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 击鼓传花.py
@time: 2019/8/3 20:17
"""
N, K = [int(e) for e in input().split(" ")]
res = 1
for i in range(1, N):
    if i == 1:
        res = res * (K-1)
    else:
        res = res * (K-2)
print(res % 1000000007)
