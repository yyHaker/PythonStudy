#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 判断二叉树结构是否相同.py
@time: 2019/7/7 19:46
"""
"""
leetcode100, 题目: 给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:  #两二叉树皆为空，递归边界，两者皆为空返回真
            return True
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.left)  #递归，每次重新从函数入口处进行，每次进行递归边界判断
            r = self.isSameTree(p.right, q.right)
            return l and r  # and操作，需要l与r皆为true时，才返回真。只用最后一次递归边界return值
        else:
            return False

