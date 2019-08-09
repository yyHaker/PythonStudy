#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 按照之子形打印二叉树.py
@time: 2019/7/11 19:08
"""
"""
剑指offer：题目：按照之子形打印二叉树
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        # 层序遍历+设置一个flag
        if not pRoot:
            return []
        res = []
        q = []
        q.append(pRoot)
        flag = True  # 表示向右
        while q:
            tmp = []  # 记录每一层的结果
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if flag:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
            res.append(tmp)
            flag = not flag
        return res




