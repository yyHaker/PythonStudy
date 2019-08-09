#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.求二叉树中结点个数.py
@time: 2019/7/7 20:03
"""
"""
题目：求二叉树中结点的个数
思路：递归解法： （1）如果二叉树为空，节点个数为0 （2）如果不为空，二叉树节点个数 = 左子树节点个数 + 右子树节点个数 + 1
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getNodeNumber(self, root):
        if not root:
            return 0
        else:
            return self.getNodeNumber(root.left) + self.getNodeNumber(root.right) + 1
