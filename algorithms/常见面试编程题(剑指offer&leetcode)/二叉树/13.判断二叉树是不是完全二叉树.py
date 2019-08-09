#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 17.判断二叉树是不是完全二叉树.py
@time: 2019/7/11 09:01
"""
"""
题目：判断二叉树是不是完全二叉树
思路：完全二叉树是指最后一层可以不是满的，但是必须集中在左边，右边可能慢也可能不满，然后其余层都是满的。
根据这个特性，利用层遍历。如果我们当前遍历到了NULL结点，如果后续还有非NULL结点，
说明是非完全二叉树
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsCompleteBinaryTree(self, root):
        if not root:
            return None
        # 队列
        q = []
        q.append(root)
        flag = True
        while q:
            node = q.pop(0)
            if node:
                if not flag:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                flag = False
        return True



