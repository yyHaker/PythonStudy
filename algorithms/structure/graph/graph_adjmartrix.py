#!/usr/bin/python
# coding:utf-8

"""使用一个二维数组实现图,(无向有权图)
@author: yyhaker
@contact: 572176750@qq.com
@file: graph_adjmartrix.py
@time: 2019/4/11 22:27
"""
class Graph(object):
    def __init__(self, vertex_nums):
        self.vertex_nums = vertex_nums
        self.graph = [[0] * vertex_nums for i in range(vertex_nums)]  #

    def add_edge(self, u, v, w=0):
        self.graph[u - 1][v - 1] = w
        self.graph[v - 1][u - 1] = w

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')

g = Graph(5)
g.add_edge(1, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 5, 5)
g.add_edge(2, 5, 2)
g.add_edge(5, 3, 3)
g.show()
