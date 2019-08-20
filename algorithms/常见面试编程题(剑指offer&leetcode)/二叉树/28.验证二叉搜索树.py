#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 28.验证二叉搜索树.py
@time: 2019/8/15 14:25
"""
"""
leetcode98: 验证二叉搜索树
思路：根据BST的定义，左子树的值要在(min,mid)之间，
    右子树的值在(mid,max)之间，这个mid值并不是中位数而是当前节点的值
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 思路：根据BST的定义，左子树的值要在(min,mid)之间，右子树的值在(mid,max)之间，这个mid值并不是中位数而是当前节点的值
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.dfs(root.left, min, root.val) and self.dfs(root.right, root.val, max)
