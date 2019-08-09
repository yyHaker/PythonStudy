#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: binary_tree.py
@time: 2019/7/7 18:44
"""
"""
剑指offer题目：
    输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def reConstructBinaryTree(self, pre, tin):
        # 思路：递归构造树的思想
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            tree_root = TreeNode(pre[0])
            tree_root.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0])+1], tin[0: tin.index(pre[0])])
            tree_root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])

