#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 22.二叉搜索树的第k个结点.py
@time: 2019/7/11 16:54
"""
"""
剑指offer：二叉搜索树的第k个结点
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 中序遍历的第k个序列即为结果
        self.res = []
        self.inorder(pRoot)
        if len(self.res) == 0 or k <= 0 or len(self.res) < k:
            return None
        return self.res[k - 1]

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.res.append(root)
            self.inorder(root.right)