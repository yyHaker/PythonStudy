#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 14. 删除链表中的倒数第k个结点.py
@time: 2019/8/14 09:42
"""
"""
leetcode19: 删除链表的倒数第N个结点
思路：双指针
时间复杂度为O(L)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 思路：双指针
        slow, fast = head, head
        pre = head
        # 快指针走n步
        for _ in range(n - 1):
            fast = fast.next
        # 双指针移动
        while fast.next != None:
            fast = fast.next
            pre = slow
            slow = slow.next
        # 删除结点
        if slow == head:
            return head.next
        else:
            pre.next = slow.next
        return head
