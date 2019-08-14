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
leetcode142: 环形链表
思路：快慢指针
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 首先判断是否有环，然后找环的入口结点
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # 判断是否有环
        if not fast or not fast.next:
            return None
        second = head
        while second != fast:
            fast = fast.next
            second = second.next
        return fast

