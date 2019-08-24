#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.两数相除.py
@time: 2019/8/17 15:49
"""
"""
leetcode29: 两数相除
思路：按照题目的意思，要求只能通过加法、减法来实现除法，
为了加速运算，可以考虑使用依次将被除数减去1，2，4，8的倍数
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 思路：按照题目的意思，要求只能通过加法、减法来实现除法，
        # 为了加速运算，可以考虑使用依次将被除数减去1，2，4，8的倍数
        MAX_INT = 2**31 -1
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            # k控制2的指数
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                # res累加结果
                res += 1 << k
                tmp <<= 1
                k += 1
        res = sign * res
        return min(res, MAX_INT)
