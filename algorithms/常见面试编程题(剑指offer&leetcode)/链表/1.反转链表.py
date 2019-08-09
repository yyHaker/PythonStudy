#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 反转链表.py
@time: 2019/7/8 12:23
"""
"""
剑指offer题目：反转链表
# 思路：持续使用连个指针，前面指针保存反转链表的首结点，后面指针保存原链表的首结点
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None  # 始终指向反转链表的首结点
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pre
