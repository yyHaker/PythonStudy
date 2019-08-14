#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 88. 合并两个有序数组.py
@time: 2019/8/14 15:02
"""
"""
leetcode88: 合并两个有序数组
思路：双指针
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 思路：双指针，倒序遍历两个数组，把大的数字依次放到nums1的后面，
        # 若nums1先遍历完，把nums2中剩余的数字直接拷贝到nums1中。
        # 时间复杂度为O(m+n), 空间复杂度为O(1)
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1