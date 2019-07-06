#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 求1+2+3+...+n.py
@time: 2019/7/5 22:05
"""
class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        if n > 0:
            res += self.Sum_Solution(n-1)
        return res
