#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.不用加减乘除做加法.py
@time: 2019/7/18 10:09
"""
"""
剑指offer: 不用加减乘除做加法
"""
class Solution:
    def Add(self, num1, num2):
        # write code here
        # 思路：第一步：两个数按位取异或。获得的值为不考虑进位时的和。
        #      第二步：两个数按位取与。获得的值位两个数求和时需要进位的位置。每次将该数左移一位，表示进位后。
        #      第三步：循环一、二步，直至两数的和没有进位为止。
        # 注意正负数和数字溢出的情况
        while num2:
            minPart = num1^num2
            num2 = (num1&num2)<<1
            num1 = minPart&0xFFFFFFFF
        # 判断是否溢出
        if num1 >> 31 == 0:
            return num1
        else:
            return num1 - 4294967296

num1 = -3
num2 = 30
solution = Solution()
res = solution.Add(num1, num2)
print(res)

# print(pow(2, 32))
