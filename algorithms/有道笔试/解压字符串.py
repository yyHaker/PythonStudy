#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 解压字符串.py
@time: 2019/8/3 19:24
"""

"""
5
A11B
(AA)2A
((A2B)2)2G
(YUANFUDAO)2JIAYOU
A2BC4D2
"""

def get_str(chs):
    # 保存前一个字符
    pre_ch = ""
    pre_num = 0
    res = ""
    for i, c in enumerate(chs):
        if c == "(":
            pass
        if c.isdigit():
            pre_num = pre_num*10 + int(c)
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i == len(chs) - 1:
            res += pre_ch * pre_num
            pre_ch = c
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and i == len(chs)-1:
                res += pre_ch
            # 更新
            pre_num = 0
    return res

T = int(input())
for i in range(T):
    chs = input()
    res = get_str(chs)
    print(res)
