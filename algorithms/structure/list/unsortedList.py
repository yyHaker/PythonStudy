#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: unsortedList.py
@time: 2019/2/17 19:22
"""
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        """在链表头部添加节点
        :param item:
        :return:
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

    def search(self, item):
        """ if item in UnorderedList.
        :param item:
        :return:
        """
        current = self.head
        found = False
        while current != None:
            data = current.getData()
            if data == item:
                found = True
                break
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """remove item in UnorderedList. (前提是item在链表中)
        :param item:
        :return:
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 删除的是第一个节点
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
