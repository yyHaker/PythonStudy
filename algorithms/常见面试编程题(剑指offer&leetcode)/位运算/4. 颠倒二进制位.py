#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4. 颠倒二进制位.py
@time: 2019/8/23 20:08
"""
"""
leetcode190: 颠倒二进制位
思路：颠倒二进制位置
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 思路一：使用函数bin和int，直接操作
        bins = bin(n)[2:][::-1]
        rev = (bins + '0' * (32 - len(bins)))
        return int(rev, 2)

class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 思路二：移位运算， 每次看n的末尾数字是多少，
        # 然后拼接到res的最前面。这样循环32次，则把n的所有数字进行了逆序操作。
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res




