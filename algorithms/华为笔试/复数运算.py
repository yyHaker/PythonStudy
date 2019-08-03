#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 复数运算.py
@time: 2019/7/24 19:22
"""
import sys
# line = sys.stdin.readline().strip()

# line = "(1000, 1000) - (500, 2000)"

import sys


def judge(inputs):
    inputs1 = inputs.split(' ')
    if len(inputs1) != 5:
        return None
    else:
        i1, i2, i3, i4, i5 = inputs1
        i1 = int(i1[1:-1])
        i2 = int(i2[:-1])
        i4 = int(i4[1:-1])
        i5 = int(i5[:-1])
        return i1, i2, i3, i4, i5

def get_res(line):
    # a, b, x, y, op
    try:
        res = judge(line)
        if not res:
            return "NaN"
        # print("res:", res)
        a, b, op, x, y = res
        l, r = 0, 0
        if op == "+":
            l = a + x
            r = b + y
        elif op == "-":
            l = a - x
            r = b - y
        elif op == "*":
            l = a * x - b * y
            r = a * y + b * x
        elif op == "/":
            l = (a * x + b * y) / (x * x + y * y)
            r = (b * x - a * y) / (x * x + y * y)
        else:
            return "NaN"
        return "(" + str(l) + "," + str(r) + ")"
    except:
        return "NaN"

# line = "(1000, 1000) - (5003, 2)"
# line = "(1000, 1000) - (500, 2000)"
# judge(line)
line = sys.stdin.readline().strip()
res = get_res(line)
print(res)

