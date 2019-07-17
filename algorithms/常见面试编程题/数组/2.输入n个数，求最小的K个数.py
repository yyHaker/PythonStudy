#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.输入n个数，求最小的K个数.py
@time: 2019/7/14 10:30
"""
"""
剑指offer：输入n个数，求最小的K个数
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 将前k个数建立最大堆，然后遍历后len(tinput)-k个数加入到堆中，最后返回这个堆即可，时间复杂度为O(nlogk)
        if tinput == None or len(tinput) == 0 or k <= 0 or len(tinput) < k:
            return []
        heap = Heap()
        for i in range(len(tinput)):
            if i < k:
                heap.push(tinput[i])
            else:
                if tinput[i] < heap.top():
                    heap.pop()
                    heap.push(tinput[i])
        return sorted(heap.heap)


class Heap(object):
    # max heap
    def __init__(self):
        self.heap = []

    def top(self):
        return self.heap[0]

    def push(self, x):
        self.heap.append(x)
        self.swim(0, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.sink(0, len(self.heap) - 2)
        return self.heap.pop()

    def sink(self, low, high):
        i = low
        j = 2 * i + 1
        while j <= high:
            if j + 1 <= high and self.heap[j] < self.heap[j + 1]:
                j += 1
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
            j = 2 * i + 1

    def swim(self, low, high):
        j = high
        i = (j - 1) / 2
        while i >= low:
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            j = i
            i = (j - 1) / 2
