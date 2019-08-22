#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 29.填充每个节点的下一个右侧结点指针.py
@time: 2019/8/21 11:33
"""
"""
leetcode116:填充每个节点的下一个右侧结点指针
思路：
层序遍历，前一个结点指向后一个结点即可
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 思路：层序遍历，前一个结点指向后一个结点即可
        if not root:
            return None
        q = []
        q.append(root)
        while q:
            length = len(q) # 当前层的个数
            pre = None
            for i in range(length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # 添加next
                if i == 0:
                    pre = node
                else:
                    pre.next = node
                    pre = node
        return root


