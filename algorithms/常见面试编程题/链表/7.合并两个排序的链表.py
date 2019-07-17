#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 7.合并两个排序的链表.py
@time: 2019/7/12 21:55
"""
"""
剑指offer：合并两个排序的链表
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 时间复杂度为O(n)，空间复杂度为O(n)
        head = ListNode(90)
        p = head
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                pHead2 = pHead2.next
            p = p.next

        if pHead1:
            p.next = pHead1
        if pHead2:
            p.next = pHead2
        return head.next
