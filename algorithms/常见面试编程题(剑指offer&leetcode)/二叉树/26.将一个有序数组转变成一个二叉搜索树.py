#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 26.将一个有序数组转变成一个二叉搜索树.py
@time: 2019/7/12 09:49
"""
"""
leetcode108: 将一个有序数组转变成一个二叉搜索树
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 递归的构造BST，首先找到根结点，递归的构造左右子结点
        length = len(nums)
        if length == 0:
            return None
        index = length // 2
        root = TreeNode(nums[index])
        root.left = self.sortedArrayToBST(nums[0:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        return root
