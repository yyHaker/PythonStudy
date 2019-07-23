#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.有效的字母异位词.py
@time: 2019/7/23 20:33
"""
"""
leetcode242: 有效的字母异位词
思路：哈希表，维护一个26个字母出现次数的数组，然后统计s字符串中字母的出现频率，
        用t减少计数器中出现字母的计算器，最后判断计数器是否回到0.(注意counter可以使用哈希)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if counter[i] != 0:
                return False
        return True

