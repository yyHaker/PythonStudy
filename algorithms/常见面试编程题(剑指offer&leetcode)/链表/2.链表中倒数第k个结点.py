#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.链表中倒数第k个结点.py
@time: 2019/7/12 10:00
"""
"""
剑指offer：链表中倒数第k个结点
思路：快慢指针，快指针先走k步，然后两个指针一起走
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 设置双指针
        if head == None:
            return None
        if k <= 0:
            return None
        p1 = head
        p2 = head
        count = 1
        while p2.next != None and count < k:
            p2 = p2.next
            count += 1
        if count < k:
            return None
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        return p1
