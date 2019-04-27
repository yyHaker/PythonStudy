#!/usr/bin/python
# coding:utf-8

"""图的广度优先搜索
@author: yyhaker
@contact: 572176750@qq.com
@file: BFS.py
@time: 2019/4/21 09:45
"""
# 广度优先搜索的思路
"""
BFS(graph G, start vertex s):
    //all nodes initially unexplored
    mark s as explored
    let Q = queue data structure, initialized with s
    while Q is non-empty:
        remove the first node of Q, call it v
        for each edge(v, w):
            if w unexplored:
                mark w explored
                add w to Q
"""
# 图的存储结构：
G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F', 'D'],
     'D': ['B', 'C'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

def bfs(graph, start):
    explored, queue = [], [start]
    explored.append(start)
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.append(w)
                queue.append(w)
    return explored

print(bfs(G, 'A'))

