#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7. 二叉树的层序遍历.py
@time: 2019/7/8 10:03
"""
"""
leetcode102： 题目：二叉树的层序遍历（输出多行）
剑指offer：题目：把二叉树打印成多行（从上而下）
剑指offer：题目：从上往下打印二叉树（输出一行）
思路：使用队列
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 使用队列进行二叉树的层序遍历
        if root is None:
            return []
        res = []
        # 模拟一个队列
        q = []
        q.append(root)
        while q:
            tmp = []  # 记录同层结点
            length = len(q)  # 同层结点个数
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        return res
