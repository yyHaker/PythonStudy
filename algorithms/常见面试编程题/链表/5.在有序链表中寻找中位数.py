#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 在有序链表中寻找中位数.py
@time: 2019/7/6 21:27
"""
"""
    思路：快慢指针。让快指针的速度保持为慢指针的两倍，这样当快指针达
到链表最后的时候，慢指针正好到达链表的中间。注意判断链表有奇数个
节点还是偶数个节点，若奇数个节点，则慢指针的值就是所求；若偶数个节
点，则慢指针和慢指针下一个的值的平均数就是所求。
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findMiddle(self, pHead):
        if not pHead:
            return None
        slow = pHead
        fast = pHead
        while fast:
            if fast.next == None:
                return slow.val
            elif fast.next != None and fast.next.next == None:
                return (slow.val + slow.next.val) / 2
            else:
                slow = slow.next
                fast = fast.next
                fast = fast.next

# test samples
x1 = ListNode(1)
x2 = ListNode(3)
x3 = ListNode(5)
x4 = ListNode(8)
x1.next = x2
x2.next = x3
x3.next = x4

# x5 = ListNode(10)
# x4.next = x5

solution = Solution()
res = solution.findMiddle(x1)
print(res)