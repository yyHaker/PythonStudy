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
leetcode103: 二叉树的锯齿形层次遍历
思路：使用队列，锯齿形层次遍历, 遍历每一层的时候设定一个flag控制方向
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

# 二刷
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 锯齿形层次遍历, 遍历每一层的时候设定一个flag控制方向
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        flag = False
        while q:
            length = len(q)
            tmp = []
            flag = not flag
            for _ in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.val)
            if not flag:
                tmp = tmp[::-1]
            res.append(tmp)
        return res




