#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 20.有效的括号.py
@time: 2019/8/5 09:43
"""
"""
leetcode20: 有效的括号
"""
class Solution:
    def isValid(self, s: str) -> bool:
        # 思路：使用栈，依次将字符串中的字符入栈，当碰到右括号时，
        # 判断栈顶字符是否匹配，若匹配，弹出栈；若不匹配，则直接返回False；
        inflect = {")": "(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            if ch in ")]}":
                if len(stack) == 0 or stack.pop() != inflect[ch]:
                    return False
        return not stack