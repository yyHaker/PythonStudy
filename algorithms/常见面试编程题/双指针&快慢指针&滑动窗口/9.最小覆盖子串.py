#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 9.最小覆盖子串.py
@time: 2019/7/26 09:11
"""
"""
leetcode76: 最小覆盖子串
思路：滑动窗口
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 思路：滑动窗口, 维护一个子字符串[i,j),使用两个哈希表来判断窗口中的字符是否满足要求，
        # 如果满足要求从左边缩小窗口，否则就从右边扩大窗口.
        # 时间复杂度为O(M+2N)=O(N)，空间复杂度为O(N)
        from collections import Counter
        if not s or not t:
            return ""
        # 两个计数器
        need = Counter(t)
        window = {}
        # 记录window中已经满足字符的个数
        match = 0

        # 最小子串的位置和长度
        start, sub_len = 0, float('inf')

        l, r = 0, 0
        while r < len(s):
            if s[r] in need:
                # 添加字符到窗口
                if s[r] not in window:
                    window[s[r]] = 1
                else:
                    window[s[r]] += 1
                # 判断字符是否满足要求了
                if window[s[r]] == need[s[r]]:
                    match += 1
            r += 1

            # windows中的字符已经符合要求了, 移动左指针
            while match == len(need):
                # 更新最子串的位置和长度
                if r - l < sub_len:
                    start = l
                    sub_len = r - l
                if s[l] in need:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1
        # 返回结果
        if sub_len == float('inf'):
            return ""
        else:
            return s[start:start + sub_len]

