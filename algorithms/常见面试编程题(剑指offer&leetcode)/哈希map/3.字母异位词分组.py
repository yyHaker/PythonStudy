#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 9.字母异位词分组.py
@time: 2019/7/23 20:58
"""
"""
leetcode49: 字母异位词分组
思路：哈希表，26个字母的计数作为哈希值
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []
            res[tuple(count)].append(s)
        return res.values()