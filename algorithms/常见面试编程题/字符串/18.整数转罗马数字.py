#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 18.整数转罗马数字.py
@time: 2019/8/3 22:38
"""
"""
leetcode12: 整数转罗马数字
思路：直接映射
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        # 思路：依次按位求除数，得到相应位的结果
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", 'CCC', "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
