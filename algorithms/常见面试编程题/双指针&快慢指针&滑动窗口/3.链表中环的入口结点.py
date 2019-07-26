#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.链表中环的入口结点.py
@time: 2019/7/12 10:04
"""
"""
剑指offer：链表中环的入口结点
思路：快慢指针
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 快慢指针
        if not pHead or not pHead.next:
            return None
        slow = pHead
        fast = slow.next
        while slow.val != fast.val:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if not fast:
                return None
        second = pHead
        slow = slow.next
        while second.val != slow.val:
            slow = slow.next
            second = second.next
        return slow