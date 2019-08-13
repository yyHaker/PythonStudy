#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.合并区间.py
@time: 2019/8/10 11:51
"""
"""
leetcode56: 合并区间
思路：先按照区间第一个元素进行排序，然后依次合并
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 思路：先按照区间第一个元素进行排序，然后依次合并
        # 时间复杂度O(nlogn)
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for idx, inter in enumerate(intervals):
            if idx == 0:
                res.append(inter)
            else:
                # 判断是否重叠
                if inter[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], inter[1])
                else:
                    res.append(inter)
        return res

