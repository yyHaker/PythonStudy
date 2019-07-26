#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.找到字符串中所有字母异位词.py
@time: 2019/7/26 10:25
"""
"""
leetcode438: 找到字符串中所有字母异位词
思路：滑动窗口
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 思路：滑动窗口, 维护一个字符串窗口[l,r], 用哈希表判断是否是字母异位词
        # 时间复杂度为O(2N)=O(N), 空间复杂度为O(K)
        from collections import Counter
        res = []
        l, r = 0, 0
        # 两个哈希表辅助判断是否是字母异位词
        need = Counter(p)
        window = {}
        match = 0

        while r < len(s):
            if s[r] in need:
                if s[r] not in window:
                    window[s[r]] = 1
                else:
                    window[s[r]] += 1
                if window[s[r]] == need[s[r]]:
                    match += 1
            r += 1
            # 满足要求，从左边缩小窗口
            while match == len(need):
                if r - l == len(p):
                    res.append(l)
                if s[l] in need:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1
        return res
