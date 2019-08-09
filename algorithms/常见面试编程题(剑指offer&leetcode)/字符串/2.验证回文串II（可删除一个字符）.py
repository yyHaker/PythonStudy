#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.验证回文串II（可删除一个字符）.py
@time: 2019/7/21 09:40
"""
"""
leetcode680: .验证回文串II（可删除一个字符）
思路：双指针，从左右两端开始验证回文串，若左右两边的字符不想等的时候，选择跳过左边或者右边的一个字符，再去验证一遍。
        时间复杂度为O(N),空间复杂度为O(1)
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
        return True

    def isPalindrome(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
