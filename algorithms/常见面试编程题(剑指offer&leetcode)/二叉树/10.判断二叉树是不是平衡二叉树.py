#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.判断二叉树是不是平衡二叉树.py
@time: 2019/7/8 11:07
"""
"""
leetcode110 题目：判断二叉树是不是平衡二叉树
思路：递归解法： （1）如果二叉树为空，返回真 （2）如果二叉树不为空，
如果左子树和右子树高度相差不大于1且左子树和右子树都是AVL树，返回真，其他返回假
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
