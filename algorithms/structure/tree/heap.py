#!/usr/bin/python
# coding:utf-8

"""使用列表实现二叉堆
@author: yyhaker
@contact: 572176750@qq.com
@file: heap.py
@time: 2019/2/21 14:12
"""
class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def buildHeap(self, alist):
        """build a heap with list. O(n)
        :param alist:
        :return:
        """
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        # 调整heap
        i = self.currentSize // 2  # (叫什么点？)
        while i > 0:
            # 将根节点和最小的子节点进行交换
            mark = i
            while 2 * mark <= self.currentSize:
                mc = self._minChild(mark)
                if self.heapList[mark] > self.heapList[mc]:
                    tmp = self.heapList[mark]
                    self.heapList[mark] = self.heapList[mc]
                    self.heapList[mc] = tmp
                mark = mc
            i = i - 1

    def insert(self, k):
        """insert a item.  O(logn)
        (如果新添加的项比它的父节点小，那么就将项与其父项交换)
        :param k:
        :return:
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        # maintain heap
        mark = self.currentSize
        while mark // 2 > 0:
            if self.heapList[mark] < self.heapList[mark // 2]:
                tmp = self.heapList[mark]
                self.heapList[mark] = self.heapList[mark // 2]
                self.heapList[mark // 2] = tmp
            mark = mark // 2

    def delMin(self):
        """del the root item.
        :return:
        """
        # 将根节点和最小的子节点进行交换
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # 将根节点和最小的子节点进行交换
        mark = 1
        while (2 * mark) <= self.currentSize:
            mc = self._minChild(mark)
            if self.heapList[mark] > self.heapList[mc]:
                tmp = self.heapList[mark]
                self.heapList[mark] = self.heapList[mc]
                self.heapList[mc] = tmp
            mark = mc
        return root

    def _minChild(self, i):
        """
         找到最小的子节点.
        :param i:
        :return:
        """
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2 + 1

if __name__ == "__main__":
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())



