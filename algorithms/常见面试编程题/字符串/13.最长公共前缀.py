#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 13.最长公共前缀.py
@time: 2019/7/26 17:02
"""
"""
leetcode14: 最长公共前缀
思路：横向扫描
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 思路：LCP(s1, s2, ...,sn) = LCP(LCP(LCP(s1, s2), s3))
        # 时间复杂度为O(nm)
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            # 求strs[i]和prefix的公共前缀
            s = strs[i]
            j = 0
            while j < len(s):
                if j < len(prefix) and s[j] == prefix[j]:
                    j += 1
                else:
                    break
            prefix = prefix[0:j]
        return prefix



