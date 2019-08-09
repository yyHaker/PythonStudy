#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 21. 二叉树的序列化和反序列化.py
@time: 2019/7/11 16:30
"""
"""
leetcode297: 题目二叉树的序列化和反序列化
剑指offer：序列化二叉树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)

    def Deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        strlist = data.split(",")
        return self.deserializeTree(strlist)

    def deserializeTree(self, strlist):
        # 反序列化二叉树
        if len(strlist) == 0:
            return None
        val = strlist.pop(0)
        root = None
        if val != "null":
            root = TreeNode(int(val))
            root.left = self.deserializeTree(strlist)
            root.right = self.deserializeTree(strlist)
        return root
