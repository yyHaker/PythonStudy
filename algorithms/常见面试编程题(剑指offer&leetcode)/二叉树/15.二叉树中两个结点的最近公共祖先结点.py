#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.二叉树中两个结点的最低公共祖先结点.py
@time: 2019/7/8 21:51
"""
"""
leetcode236: 二叉树中两个结点的最低公共祖先结点
思路：
         递归解法：
        （1）如果两个节点分别在根节点的左子树和右子树，则返回根节点
        （2）如果两个节点都在左子树，则递归处理左子树；如果两个节点都在右子树，则递归处理右子树
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
        # 递归解法：
        # （1）如果两个节点分别在根节点的左子树和右子树，则返回根节点
        # （2）如果两个节点都在左子树，则递归处理左子树；如果两个节点都在右子树，则递归处理右子树
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left == None:
            return right
        else:
            return left
