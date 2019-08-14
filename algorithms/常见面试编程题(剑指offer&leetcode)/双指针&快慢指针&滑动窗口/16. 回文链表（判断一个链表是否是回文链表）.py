#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 16. 回文链表.py
@time: 2019/8/14 11:14
"""
"""
leetcode234: 回文链表
思路：双指针 + 反转链表
时间复杂度为O(n), 空间复杂度为O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 思路：双指针+反转链表
        # 注意不用判断链表个数为奇数的时候，想想为什么？(刚好两个链表最后不用判断中间的那个数)
        # 时间复杂度为O(n), 空间复杂度为O(1)
        if head == None or head.next == None:
            return True
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # 反转slow之后的链表
        cur = slow.next
        slow.next = None
        pre = None
        while cur != None:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t

        # 判断回文
        while pre != None and head != None:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
