#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: heap.py
@time: 2019/7/14 10:35
"""
# 使用python的库heapq
import heapq

data = [5, 8, 6, 3, 4, 7, 0, 1, 2, 9]
heap = []
for i in data:
    heapq.heappush(heap, i)
print(heap)

# 添加元素
heapq.heappush(heap, 0.5)
print(heap)

# 查看堆顶的元素
res = heapq.nlargest(1, heap)
print(res)

# 弹出元素
res = heapq.heappop(heap)
print(res)

res = heapq.heappop(heap)
print(res)

res = heapq.heappop(heap)
print(res)
print(heap)

heapq.heappushpop(heap, 1)
print(heap)

res = heapq.nlargest(3, heap)
print("res: ", res)

res = heapq.nsmallest(3, heap)
print("res: ", res)
