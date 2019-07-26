#!/usr/bin/python
# coding:utf-8
"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.验证回文串.py
@time: 2019/7/21 09:40
"""
"""
 leetcode125: 验证回文串
思路：使用双指针，依此分别从前后往中间遍历判断
    时间复杂度为O(N)，空间复杂度为O(1)
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            while left < right and not self.is_letters_digits(s[left]):
                left += 1
            while right > left and not self.is_letters_digits(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def is_letters_digits(self, c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9'