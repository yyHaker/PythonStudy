#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 14.求二叉树的直径.py
@time: 2019/7/10 22:33
"""
"""
leetcode543： 求二叉树的直径
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 维护一个全局变量ans（表示二叉树的直径），依次遍历树中每个结点，递归求左子树和右子树的最大深度，并更新res
        self.ans = 0
        self.depth(root)
        return self.ans

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        # update ans
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
