#!/usr/bin/python
# coding:utf-8

"""使用栈处理符号匹配问题
@author: yyhaker
@contact: 572176750@qq.com
@file: signmatching.py
@time: 2019/2/17 14:44
"""

from stack import Stack

def signMatching(sign):
    stack = Stack()
    balance = False
    for s in sign:
        if s in "[{(":
            stack.push(s)
        elif s in "]})":
            # stack can not be empty
            if stack.isEmpty():
                return False
            cur = stack.pop()
            if isMatch(cur, s):
                balance = True
            else:
                balance = False
                break
    if stack.isEmpty() and balance:
        return True
    else:
        return False


def isMatch(s1, s2):
    left = "[{("
    right = "]})"
    return left.index(s1) == right.index(s2)


if __name__ == "__main__":
    print(signMatching("{{([][])}()}"))
    print(signMatching("{{([][)}()}"))


