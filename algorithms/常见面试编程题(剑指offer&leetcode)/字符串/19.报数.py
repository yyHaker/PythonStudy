#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 19.报数.py
@time: 2019/8/4 16:02
"""
"""
leetcode38：报数(Count and Say)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        # 思路：统计字符串个数，然后拼接到一起
        res = "1"
        for i in range(n-1):
            prev = res[0]
            count = 1
            ans = ""
            for j in range(1, len(res)):
                cur = res[j]
                if prev != cur:
                    ans = ans + str(count) + str(prev)
                    prev = cur
                    count = 0
                count += 1
            res = ans + str(count) + str(prev)
        return res
