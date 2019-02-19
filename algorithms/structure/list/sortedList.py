#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: sortedList.py
@time: 2019/2/18 11:26
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


class OrderedList(object):
    """
    默认升序.
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        """在链表中添加节点
        :param item:
        :return:
        """
        current = self.head
        previous = None
        # 寻找插入节点的位置
        while current !=None and current.getData() < item:
            previous = current
            current = current.getNext()
        # 找到插入节点的位置
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

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
            if current.getData() == item:
                found = True
                break
            else:
                if current.getData() > item:
                    found = False
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
