#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.无重复字符的最长子串.py
@time: 2019/7/25 10:13
"""
"""
leetcode3: 无重复字符的最长子串
思路：滑动窗口
"""
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思路：滑动窗口, 维护一个窗口为[i,j)的字符串，并使用hashset存储出现的字符，
        # 若s[j]不在hashset，j后移，更新不重复字符串的最大长度；若s[j]在hashset，i后移，继续维护下一个窗口。
        # 时间复杂度为O(2n)=O(n), 空间复杂度为O(min(m,n))
        res = 0
        chars = set()
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                chars.remove(s[i])
                i += 1
        return res

class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思路：优化的滑动窗口, 维护一个窗口为[i,j]的字符串，并使用hashset存储出现的字符到索引的一个映射。
        # 如果s[j]在hashset中，i直接跳到该重复字符的下一个位置；每轮均会更新当前最大无重复字符串的最大长度，并添加字符到hashset
        # 时间复杂度为O(n), 空间复杂度为O(min(m,n))
        res = 0
        chars = {}
        i, j = 0, 0
        for j in range(len(s)):
            if s[j] in chars:
                i = max(chars[s[j]] + 1, i)
            res = max(res, j - i + 1)
            chars[s[j]] = j
        return res


s = "abcabcbb"
solution = Solution1()
res = solution.lengthOfLongestSubstring(s)
print(res)