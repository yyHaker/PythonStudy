#!/usr/bin/python
# coding:utf-8

"""使用栈处理括号匹配问题
------------
思路：从左到右扫描字符串，如果是左括号就压栈，如果是右括号就pop判断是否匹配，
直到栈空全部匹配就返回True，否则返回False.
@author: yyhaker
@contact: 572176750@qq.com
@file: parenthesisMatching.py
@time: 2018/12/18 11:25
"""

from stack import Stack


def parenthesis_matching(s):
    """
    :param s: string
    :return:
    """
    stack = Stack()
    for c in list(s):
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.isEmpty():
                return False
            t = stack.pop()
            if t != "(":
                return False
    if stack.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = '((()))'
    s2 = '(()'
    s3 = '(()))'
    print(parenthesis_matching(s1))
    print(parenthesis_matching(s2))
    print(parenthesis_matching(s3))



