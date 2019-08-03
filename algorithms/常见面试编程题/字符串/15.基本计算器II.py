#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 15.基本计算器II.py
@time: 2019/7/28 10:53
"""
"""
leetcode227: 基本计算器II
思路：使用栈
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思路：使用栈。依次遍历字符串，用num保存上一数字，用pre_op保存上一个运算符，按照pre_op符号判断
        num = 0
        pre_op = "+"
        stack = []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = 10 * num + int(ch)
            if i == len(s) - 1 or ch in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop() * num)
                elif pre_op == "/":
                    tmp = stack.pop()
                    if tmp < 0:
                        stack.append(int(tmp / num))
                    else:
                        stack.append(tmp // num)
                # 更新上一个数字和字符
                num = 0
                pre_op = ch
        return sum(stack)

s = "3+2*2"
s2 = "14-3/2"
solution = Solution()
res = solution.calculate(s2)
print(res)
