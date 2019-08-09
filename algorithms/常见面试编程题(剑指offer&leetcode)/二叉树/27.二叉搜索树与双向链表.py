#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 27.二叉搜索树与双向链表.py
@time: 2019/7/17 09:37
"""
"""
剑指offer: 二叉搜索树与双向链表
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.listhead = None
        self.listtail = None

    def Convert(self, pRootOfTree):
        # write code here
        # 思路：按照中序遍历的顺序将链表拼接起来;左子树递归求解，链接根结点，右子树递归求解
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.listtail:
            self.listhead = pRootOfTree
            self.listtail = pRootOfTree
        else:
            self.listtail.right = pRootOfTree
            pRootOfTree.left = self.listtail
            self.listtail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listhead
