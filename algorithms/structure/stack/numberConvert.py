#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: numberConvert.py
@time: 2019/2/17 15:10
"""
from stack import Stack

def divideBy2(number):
    """
    二进制转换
    :param number:
    :return:
    """
    stack = Stack()
    while number > 0:
        res = number % 2
        stack.push(res)
        number = number // 2

    binStr = ""
    while not stack.isEmpty():
        binStr = binStr + str(stack.pop())
    return binStr

def divideByBase(number, base):
    """
    十进制转换
    :param number:
    :param base:
    :return:
    """
    data = "0123456789ABCDEF"
    stack = Stack()
    while number > 0:
        res = number % base
        stack.push(res)
        number = number // base

    binStr = ""
    while not stack.isEmpty():
        binStr = binStr + str(data[stack.pop()])
    return binStr

if __name__ == "__main__":
    binStr = divideBy2(42)
    print(binStr)

    binStr = divideByBase(233, 8)
    print(binStr)

    binStr = divideByBase(233, 8)
    print(binStr)
