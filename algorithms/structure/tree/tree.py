#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: tree.py
@time: 2019/6/18 20:27
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def inorder(root):
            if root is not None:
                inorder(root.left)
                res.append(root.val)
