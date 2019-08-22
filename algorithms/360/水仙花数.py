#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 水仙花数.py
@time: 2019/8/15 15:34
"""
def is_num(num):
    m = num // 100
    n = (num - 100 * m) // 10
    p = num % 10
    return pow(m, 3) + pow(n, 3) + pow(p, 3) == num

def get_num(m, n):
    res = []
    for k in range(m, n+1):
        if is_num(k):
            res.append(k)
    return res

nums = [int(e) for e in input().split(" ")]
m, n = nums[0], nums[1]
res = get_num(m, n)
if len(res) == 0:
    print("no")
else:
    print(" ".join(map(str, res)))
