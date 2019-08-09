#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.二叉树的镜像.py
@time: 2019/7/8 11:32
"""
"""
leetcode226： 题目：求二叉树的镜像
剑指offer：二叉树的镜像
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        # 递归的交换左右结点
        node = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(node)
        return root