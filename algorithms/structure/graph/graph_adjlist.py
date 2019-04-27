#!/usr/bin/python
# coding:utf-8

"""使用邻接表实现图. （该处实现的是有向图）
@author: yyhaker
@contact: 572176750@qq.com
@file: graph.py
@time: 2019/4/11 21:54
"""
class Vertex(object):
    def __init__(self, key):
        self.id = key  # the id of vertex
        self.connectedTo = {}

    def addNeighbor(self, key, weight=0):
        """add neighbor vertex"""
        self.connectedTo[key] = weight

    def getWeight(self, key):
        """get vertex weight"""
        return self.connectedTo[key]

    def getId(self):
        """get vertex name"""
        return self.id

    def getConnections(self):
        """get all connected vertexes"""
        return self.connectedTo.keys()

class Graph(object):
    """Graph ADT"""
    def __init__(self):
        self.vertexList = {}  # vertex name -> vertex object dict
        self.numVertexes = 0

    def addVertex(self, key):
        """add new vertex"""
        self.numVertexes = self.numVertexes + 1
        new_vertex = Vertex(key)
        self.vertexList[key] = new_vertex
        return new_vertex

    def addEdge(self, f, t, weight=0):
        """add new Edge"""
        if f not in self.vertexList:
            f = self.addVertex(f)
        if t not in self.vertexList:
            t = self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], weight)

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def getAllVertexes(self):
        """get all vertexes"""
        return self.vertexList.keys()


