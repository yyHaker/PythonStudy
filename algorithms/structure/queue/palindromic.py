#!/usr/bin/python
# coding:utf-8

"""使用双端队列来检查回文字符串
@author: yyhaker
@contact: 572176750@qq.com
@file: palindromic.py
@time: 2019/2/17 18:58
"""
from MyQueue import Deque

def palChecker(aString):
    queue = Deque()

    for ch in aString:
        queue.addRear(ch)

    stillEqual = True

    while queue.size() > 1 and stillEqual:
        first = queue.removeFront()
        last = queue.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

if __name__ == "__main__":
    print(palChecker("lsdkjfskf"))
    print(palChecker("radar"))

