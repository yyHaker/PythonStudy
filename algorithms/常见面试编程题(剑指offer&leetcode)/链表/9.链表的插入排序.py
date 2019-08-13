#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 9.链表的插入排序.py
@time: 2019/8/9 20:11
"""
"""
leetcode147: 链表的插入排序
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 思路：对链表进行插入排序
        if not head or not head.next:
            return head
        newhead = TreeNode(0)
        newhead.next = head
        while head.next:
            if head.val < head.next.val:
                head = head.next
            else:
                # 插head.next
                temp = head.next
                head.next = head.next.next # 向后挪一位
                q = newhead
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return newhead.next

