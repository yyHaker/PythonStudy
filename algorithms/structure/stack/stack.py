#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: stack.py
@time: 2018/12/16 22:05
"""
class Stack(object):
    def __init__(self):
        super(Stack, self).__init__()
        self.items = []    # 右边是栈顶，左边是栈底

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)




