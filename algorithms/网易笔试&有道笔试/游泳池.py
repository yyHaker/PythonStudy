#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 游泳池.py
@time: 2019/8/11 15:13
"""

def getwater(m, t, m1, t1, m2, t2):
    cur = 0
    add_flag = True
    del_flag = True
    for time in range(1, t + 1):
        # 判断水量
        if add_flag:
            cur += m1
        if del_flag:
            cur -= m2

        if cur < 0:
            cur = 0
        if cur > m:
            cur = m

        if time >= t1 and time % t1 == 0:
            add_flag = not add_flag
        if time >= t2 and time % t2 == 0:
            del_flag = not del_flag
    return cur


T = int(input())
for _ in range(T):
    nums = [int(e) for e in input().split(" ")]
    m, t, m1, t1, m2, t2 = nums[0], nums[1], nums[2], nums[3], nums[4], nums[5]
    res = getwater(m, t, m1, t1, m2, t2)
    print(res)
