#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.求二叉树的最小深度.py
@time: 2019/7/7 20:14
"""
"""
LeetCode111: 题目：Minimum Depth of Binary Tree 给定一个二叉树，找出其最小深度。 最小深度
是从根节点到最近叶子节点的最短路径上的节点数量。
# 思路：递归求解
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1
