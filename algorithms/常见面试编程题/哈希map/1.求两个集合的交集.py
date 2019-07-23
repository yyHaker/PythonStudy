#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.求两个集合的交集.py
@time: 2019/7/23 21:08
"""
"""
求两个集合的交集，每个集合可能包含数字和字母
思路： 使用哈希表
"""
def interaction(s1, s2):
    res = []
    count = {}
    for ch in s1:
        if ch not in count.keys():
            count[ch] = ch
    for ch in s2:
        if ch in count:
            res.append(ch)
    return res

s1 = ['a', 'b', 'c', 2, 4, 5]
s2 = ['b', 'c', 'd', -1, 2, 7]
res = interaction(s1, s2)
print(res)