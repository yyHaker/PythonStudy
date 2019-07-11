#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 13.二叉搜索树的最近公共祖先.py
@time: 2019/7/10 11:35
"""
"""
leetcode235: 给定一个二叉搜索树和两个结点，寻找两个结点的最近公共祖先
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 常规解法
        # if not root or root == p or root == q:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     return root
        # if not left:
        #     return right
        # else:
        #     return left

        # 利用二叉搜索树的特性可以寻找p和q的位置
        if not root or root == p or root == q:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
