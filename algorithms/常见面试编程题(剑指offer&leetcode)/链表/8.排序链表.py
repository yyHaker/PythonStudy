#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.排序链表.py
@time: 2019/8/9 19:36
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 思路：利用归并排序的思想，现将列表等分成两部分，分别对两部分进行排序，最后再合并这两个有序的链表.
        # 如何划分链表？利用快慢指针，当快指针到达末尾时，慢指针刚好到达链表中间
        if not head or not head.next:
            return head
        slow, fast = head, head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        # 合并两个有序链表
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return head.next
