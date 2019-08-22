#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 最长公共前缀.py
@time: 2019/8/22 15:58
"""

def lcs(strs1, strs2):
    if len(strs1) == 0 or len(strs2) == 0 or strs1[0] != strs2[0]:
        return 0
    j = 0
    while j < len(strs2):
        if j < len(strs1) and strs1[j] == strs2[j]:
            j += 1
        else:
            break
    return j

n = int(input())
strs = []
for _ in range(n):
    s = input().strip()
    strs.append(s)

while True:
    nums = [int(e) for e in input().strip().split(" ")]
    a, b = nums[0], nums[1]
    if 1 <= a <= n and 1 <= b <= n:
        res = lcs(strs[a-1], strs[b-1])
        print(res)
    else:
        pass
