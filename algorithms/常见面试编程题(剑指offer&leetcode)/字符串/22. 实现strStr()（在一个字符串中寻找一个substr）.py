#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 22. 实现strStr()（在一个字符串中寻找一个substr）.py
@time: 2019/8/14 15:29
"""
"""
leetcode28：实现strStr()（在一个字符串中寻找一个substr）
思路：
【1】暴力匹配，时间复杂度为O((m-n)n)
【2】KMP算法，时间复杂度为O(m+n)
参考：https://www.zhihu.com/question/21923021
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 思路：暴力匹配，时间复杂度为O((m-n)n)
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        for i in range(m-n+1):
            if haystack[i: i+n] == needle:
                return i
        return -1


class Solution2(object):
    def strStr(self, t, p):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 思路：KMP算法
        if len(p) == 0:
            return 0
        i, j = 0, 0
        next = [0] * len(p)

        self.GetNext(p, next)

        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == len(p):
            return i - j
        else:
            return -1

    def GetNext(self, p, next):  # 计算改进版next数组
        next[0] = -1
        i, j = 0, -1
        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]

solution = Solution2()
t= "ababababca"
p = "abababca"
solution.strStr(t, p)
