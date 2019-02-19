#!/usr/bin/python
# coding:utf-8

"""使用队列处理约瑟夫问题
@author: yyhaker
@contact: 572176750@qq.com
@file: josephproblem.py
@time: 2019/2/17 17:25
"""
from MyQueue import Queue

def hotPotato(nameList, num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)

    # 模拟
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


if __name__ == "__main__":
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

