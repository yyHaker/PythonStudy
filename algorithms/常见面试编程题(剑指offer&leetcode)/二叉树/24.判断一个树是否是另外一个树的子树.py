#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 18.树的子结构.py
@time: 2019/7/11 10:53
"""
"""
剑指offer：题目：判断一个树是不是另外一个树的子树？
思路：
    如果A、B有一个为空，直接返回False；如果A、B均不为空，以A、B为根结点判断B是否是A的子树；
      以A的左结点、B为根结点判断B是否是A的子树；以A的右结点、B判断是否是A的子树。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                         pRoot2)

    def isSubTree(self, root1, root2):
        # 以root1、root2为根结点判断root2是否是root1的子树
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.isSubTree(root1.left, root2.left) and self.isSubTree(root1.right, root2.right)

