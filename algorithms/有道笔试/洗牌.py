#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 洗牌.py
@time: 2019/8/3 13:40
"""
T = int(input())
array_list = []
n, k = [int(e) for e in input().split()]
for x in range(T):
    digs = [int(e) for e in input().split()]
    array = digs[0:2 * n]
    res = [None] * (2 * n)
    # 每一次洗牌：把前n个数放在偶数位置，后n个数放在奇数位置
    for t in range(k):
        res[::2] = array[:n]
        res[1::2] = array[n:]
        array = res
    # 下一组数据
    n, k = digs[-2:]
    print(" ".join(map(str, res)))
