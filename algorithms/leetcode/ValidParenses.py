# -*- coding: utf-8 -*-
"""
判断一个字符串括号是否有效的问题，思路：使用stack,  如果是左括号就放
进stack，如果是右括号就判断是否匹配，匹配则出栈，否贼返回False.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '[': ']', '{': '}'}
        if len(s) % 2 == 1:
            return False
        stack = []
        for ch in s:
            if ch in dict:
                stack.append(ch)
            else:
                if len(stack)>0 and dict[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return stack == []