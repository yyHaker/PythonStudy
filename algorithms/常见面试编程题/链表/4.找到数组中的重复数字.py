#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.找到数组中的重复数字.py
@time: 2019/7/12 10:07
"""
"""
leetcode287: 找到一个数组中的重复数字(只有一个重复数字，但是可以重复多次)， 例如[1,3,4,2,2,2].
思路：快慢指针，转换成判断链表是否有环的问题，且找出入口点(时间复杂度O(n))
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        slow = nums[slow]
        fast = nums[slow]
        # 慢指针走一步，快指针走两步，直到相遇
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        # 找出入口点
        second = 0
        while slow != second:
            slow = nums[slow]
            second = nums[second]
        return slow
