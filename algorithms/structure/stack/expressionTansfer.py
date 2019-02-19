#!/usr/bin/python
# coding:utf-8

"""使用栈来处理表达式转换问题
@author: yyhaker
@contact: 572176750@qq.com
@file: expressionTansfer.py
@time: 2019/2/17 15:59
"""

from stack import Stack

def infixToPostfix(infixexpr):
    """
    中缀表达式---->后缀表达式
    :param infixexpr:
    :return:
    """
    # 优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prec[")"] = 1
    stack = Stack()

    postfixList = []  # 保存结果
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            topToken = stack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = stack.pop()
        else:
            while not stack.isEmpty() and stack.peek() in "*/+-" and prec[stack.peek()] >= prec[token]:
                postfixList.append(stack.pop())
            stack.push(token)

    # 清空栈中剩余的运算符
    while not stack.isEmpty():
        postfixList.append(stack.pop())

    return " ".join(postfixList)

if __name__ == "__main__":
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("( A + B ) * C"))
