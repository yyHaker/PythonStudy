#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 20.二叉树的下一个结点.py
@time: 2019/7/11 15:34
"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# 思路：三种情况
#     1.该结点为空，则返回空
#     2.该结点的右孩子存在，则返回该结点右孩子的最左子结点
#     3.该结点的右孩子不存在，找到该结点的父结点：如果该结点是左孩子，则直接返回父结点；
#             如果是右孩子，继续向上遍历其父亲结点，重复之前的判断，返回结果。
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next


