#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.四数相加II.py
@time: 2019/8/19 11:02
"""
"""
leetcode454: 四数相加II
思路：哈希表+二分思想
"""
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 思路：求AB和的所有组合，并构建成map，key-val分别表示和和出现次数；
        # 再求CD的所有组合并取反， 统计在map中出现的次数和
        # 时间复杂度为O(n^2)
        res = 0
        dic = {}
        for a in A:
            for b in B:
                if a+b not in dic:
                    dic[a+b] = 1
                else:
                    dic[a+b] += 1
        for c in C:
            for d in D:
                if -(c+d) in dic:
                    res += dic[-(c+d)]
        return res
