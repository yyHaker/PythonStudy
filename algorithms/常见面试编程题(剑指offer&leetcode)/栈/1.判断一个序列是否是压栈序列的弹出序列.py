#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.判断一个序列是否是压栈序列的弹出序列.py
@time: 2019/7/13 18:59
"""
"""
剑指offer：题目：栈的压入、弹出序列
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # 思路：利用一个辅助栈，依次将压栈序列压入到辅助栈中，每次判断辅助栈的栈顶元素与弹出序列是否相等。
        # 若相等，将该元素从辅助栈中弹出，弹出序列指针右移；若不想等，继续将压栈序列压入到辅助栈中，直到压完。
        # 最后若栈为空，返回True；否则返回False。
        stack = []
        for e in pushV:
            stack.append(e)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)  # 指针右移
        if not stack and not popV:
            return True
        else:
            return False
