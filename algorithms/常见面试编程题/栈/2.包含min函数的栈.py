#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.包含min函数的栈.py
@time: 2019/7/13 19:19
"""
"""
剑指offer： 题目：包含min函数的栈
"""

import sys
class Solution:
    def __init__(self):
        self.list = []
        self.minStack = [sys.maxsize]  # 保存最小值的栈

    def push(self, node):
        self.list.append(node)
        if node < self.top():
            self.minStack.append(node)

    def pop(self):
        # write code here
        if self.list:
            popNum = self.list.pop()
            if popNum == self.top():
                self.minStack.pop()
        else:
            return None

    def top(self):
        # write code here
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

    def min(self):
        # write code here
        return self.top()
