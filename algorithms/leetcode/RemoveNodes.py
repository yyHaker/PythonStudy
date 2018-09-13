# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 维护两个指针，指针的距离是n
        if head.next == None and n ==1:
            return None
        start, end = head, head
        gap = 0
        while(1):
            if end.next != None:
                end = end.next
                gap = gap +1
                if gap > n:
                    start = start.next
            else:
                break
        # 删除头节点的情况
        if start == head and gap < n:
            head = start.next
        else:
            start.next = start.next.next
        return head
