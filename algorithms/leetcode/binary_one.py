#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: binary_one.py
@time: 2019/6/20 19:47
"""
def NumberOf1(n):
    # write code here
    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        count += 1
        n = n & (n-1)
    return count

n = -1
res = NumberOf1(n)
print(-1 & -1)




