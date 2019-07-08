#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4. 二叉树的前序遍历(递归+非递归).py
@time: 2019/7/7 20:24
"""
"""
leetcode94: 题目：二叉树的非递归中序遍历
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归的方法
        # if root == None:
        #     return []
        # res = []
        # res += self.inorderTraversal(root.left)
        # res.append(root.val)
        # res += self.inorderTraversal(root.right)
        # return res

        # 非递归的方法
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                res.append(t.val)
                root = t.right
        return res
