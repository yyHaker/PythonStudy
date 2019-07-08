#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8. 二叉树的自下而上分层遍历.py
@time: 2019/7/8 10:40
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        q = [] # 队列
        q.append(root)
        while q:
            length = len(q) # 每一层结点的个数
            data = [] # 保存每层结点的值
            for i in range(length):
                node = q.pop(0)
                data.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res = [data] + res
        return res
