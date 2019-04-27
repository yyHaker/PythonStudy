#!/usr/bin/python
# coding:utf-8

"""图的深度优先搜索
@author: yyhaker
@contact: 572176750@qq.com
@file: DFS.py
@time: 2019/4/14 21:08
"""
# 深度优先搜索的思路
"""
DFS(graph G, start vertex s):
    // all nodes initially unexplored
    mark s as explored
    for every edge (s, v):
    if v unexplored:
        DFS(G, v)
"""
# 图的存储结构：
G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F', 'D'],
     'D': ['B', 'C'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

# 深搜(使用stack实现)
def dfs(graph, start):
    explored, stack = [], [start]
    while stack:
        v = stack.pop()
        explored.append(v)
        for w in graph[v]:
            if w not in explored:
                stack.append(w)
                break    # find one should break
    return explored

# 深搜(使用递归实现)
def dfs_(graph, start, explored):
    explored.append(start)
    for w in graph[start]:
        if w not in explored:
            dfs_(graph, w, explored)
    return explored

print(dfs(G, 'A'))
print("*"*20)
print(dfs_(G, 'A', []))


