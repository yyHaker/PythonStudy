#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.两个数组的交集II.py
@time: 2019/7/23 21:52
"""
"""
leetcode350: 两个数组的交集II（输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致）
思路： 思路：哈希表，建立一个数字->出现次数的哈希表
时间复杂度为O(m+n), 空间复杂度为(n)
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        count = {}
        for n in nums1:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n in nums2:
            if n in count and count[n] >= 1:
                res.append(n)
                count[n] -= 1
        return res
