#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: queue.py
@time: 2019/2/17 17:10
"""

class Queue(object):
    def __init__(self):
        self.items = []   # 左边是队尾部, 右边是队首

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Deque(object):
    def __init__(self):
        self.items = []  # 双端队列, 左边是队尾，右边是队首

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
