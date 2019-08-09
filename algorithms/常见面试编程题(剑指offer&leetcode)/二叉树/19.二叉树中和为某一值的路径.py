#!/usr/bin/python
# coding:utf-8
"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 19. 二叉树中和为某一值的路径.py
@time: 2019/7/11 14:40
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路：递归思想
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in left + right:
            res.append([root.val] + i)
        return res
