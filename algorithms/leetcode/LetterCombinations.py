# -*- coding: utf-8 -*-
"""
2018年9月10日
题解：电话号码对应的字符串组合，解题思路是：递归思想求解子问题，
取电话号码第一个，后面递归求解，
依次将第一个电话号码添加到后面电话号码对应的所有字符串组合.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number2letter = {0: [], 1: [],  2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return number2letter[int(digits)]
        elif len(digits) > 1:
            head = number2letter[int(digits[0])]
            trail = self.letterCombinations(digits[1:])
            result = []
            for h in head:
                tr = [h+t for t in trail]
                result.extend(tr)
            return result


