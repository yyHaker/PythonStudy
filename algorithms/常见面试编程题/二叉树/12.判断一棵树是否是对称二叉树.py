#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 判断对称二叉树.py
@time: 2019/7/11 17:20
"""
"""
剑指offer：题目：对称的二叉树
leetcode101: 对称二叉树
思路：判断两棵树是否是对称相等
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isEqual(pRoot.left, pRoot.right)

    def isEqual(self, root1, root2):
        # 判断两棵树是否对称相等
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.isEqual(root1.left, root2.right) and self.isEqual(root1.right, root2.left)
        else:
            return False
