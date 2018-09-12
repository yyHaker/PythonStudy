# -*- coding: utf-8 -*-
"""
ZigZag conversion, 将字符串按照Z型填充到list，然后拼接字符串(难点：怎么填充这个字符串？)
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 将字符串按照Z型填充到list，然后拼接字符串(难点：怎么填充这个字符串？)
        if len(s) <= numRows or numRows == 1:
            return s
        res = ['']*numRows
        index = 0
        step = 1
        for ch in s:
            res[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(res)