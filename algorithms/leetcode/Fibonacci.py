#!/usr/bin/python
# coding:utf-8

"""斐波那契数列的计算
@author: yyhaker
@contact: 572176750@qq.com
@file: Fibonacci.py
@time: 2019/3/17 21:16
"""
#
# def Fibonacci(n):
#     # write code here
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)

def Fibonacci(n):
    # write code here
    nums = []
    for i in range(n + 1):
        if i == 0:
            nums.append(0)
        if i == 1:
            nums.append(1)
        if i >= 2:
            nums.append(nums[i - 1] + nums[i - 2])
    return nums[n]

print(Fibonacci(100))

