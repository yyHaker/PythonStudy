#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: string_permutation.py
@time: 2019/7/1 21:06
"""

class Solution:
    def Permutation(self, ss):
        # write code here
        out = []
        if len(ss) == 0:
            return out
        charlist = list(ss)
        self.permut(charlist, 0, out)
        out = [''.join(out[i]) for i in range(len(out))]
        sorted(out)
        return out

    def permut(self, alist, begin, out):
        # 一轮递归结束条件
        if begin == len(alist) - 1:
            out.append(alist[:])
        else:
            for i in range(begin, len(alist)):
                # 如果是重复字符就跳过
                if alist[i] == alist[begin] and i != begin:
                    continue
                else:
                    # 依次与后面值进行交换
                    alist[begin], alist[i] = alist[i], alist[begin]
                    self.permut(alist, begin + 1, out)
                    # 回到上一个状态
                    alist[begin], alist[i] = alist[i], alist[begin]
