#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 30.二叉树中的最大路径和.py
@time: 2019/8/22 13:43
"""
"""
leetcode124: 二叉树中的最大路径和
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 思路：递归求解，递归求解以某一个结点为起始结点的最大路径和，
        # 它等于当前结点的值+max(以左子结点为起始结点的最大路径和，以右子结点为起始结点的最大路径和)；
        # 在递归的过程中，更新最大的路径和的值，它等于当前结点的值+左子结点的最大路径和+右子结点的最大路径和
        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.res = max(self.res, left + root.val + right)
        return max(left, right) + root.val