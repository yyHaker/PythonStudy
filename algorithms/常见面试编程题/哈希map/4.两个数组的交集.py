#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.两个数组的交集.py
@time: 2019/7/23 21:36
"""
"""
leetcode349: 求两个数组的交集
思路：
1.哈希表
2.内置函数set交集
"""
class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 思路：哈希表
        #  时间复杂度为O(m+n), 空间复杂度为O(n)
        res = []
        count = {}
        for n in nums1:
            if n not in count:
                count[n] = n
        nums2 = list(set(nums2))
        for n in nums2:
            if n in count:
                res.append(n)
        return res


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 思路2：内置函数
        # 时间复杂度为O(m+n)，最坏情况O(mn); 空间复杂度为O(m+n)
        set1 = set(nums1)
        set2 = set(nums2)
        return set1 & set2
