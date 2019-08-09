#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 16.由中序遍历序列和后序遍历序列重建二叉树.py
@time: 2019/7/11 08:51
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 递归构造树
        if len(postorder) == 0:
            return None
        elif len(postorder) == 1:
            return TreeNode(postorder[-1])
        else:
            root = TreeNode(postorder[-1])
            idx = inorder.index(postorder[-1])
            root.left = self.buildTree(inorder[0: idx], postorder[0: idx])
            root.right = self.buildTree(inorder[idx+1: ], postorder[idx: -1])
            return root