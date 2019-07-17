#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.删除链表中重复的结点.py
@time: 2019/7/12 11:14
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 思路：快慢指针
        # 用一个指针保存头结点
        first = ListNode(-1)
        first.next = pHead
        slow = first
        fast = pHead
        while fast and fast.next:
            # 检测是否有重复结点
            if fast.val == fast.next.val:
                value = fast.val
                while fast.next and fast.next.val == value:
                    fast = fast.next
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return first.next

