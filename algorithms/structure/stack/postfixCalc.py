#!/usr/bin/python
# coding:utf-8

"""使用栈计算后缀表达式
@author: yyhaker
@contact: 572176750@qq.com
@file: postfixCalc.py
@time: 2019/2/17 16:53
"""

from stack import Stack

def postfixEval(postfixExpr):
    stack = Stack()

    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            res = doMath(token, operand1, operand2)
            stack.push(res)
    return stack.pop()

def doMath(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    else:
        raise Exception("not supported operation!")


if __name__ == "__main__":
    print(postfixEval('7 8 + 3 2 + /'))
