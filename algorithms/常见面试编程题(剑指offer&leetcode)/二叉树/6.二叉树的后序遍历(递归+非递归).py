#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4. 二叉树的前序遍历(递归+非递归).py
@time: 2019/7/7 20:24
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归解法
        if root == None:
            return []
        res = []
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res

        # 非递归解法
        # 思路：先序遍历->根左右，后序遍历->左右根， 所以把先序遍历换成->根右左再把最后的结果反过来就是左右根
        res = []
        stack = []
        seq = []
        while root or stack:
            while root:
                seq.append(root.val)
                stack.append(root)
                root = root.right
            if stack:
                t = stack.pop()
                root = t.left
        # 反转
        while seq:
            res.append(seq.pop())
        return res
