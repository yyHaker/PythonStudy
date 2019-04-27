#!/usr/bin/python
# coding:utf-8

"""求数组中所有和为0的子序列
@author: yyhaker
@contact: 572176750@qq.com
@file: subarraysum.py
@time: 2019/3/18 21:02
"""
def getSumSeq(seq, K):
    """
    时间复杂度为O(n^2), 空间复杂度为O(1)
    :param seq:
    :return:
    """
    size = len(seq)
    # s = [[None] * size] * size
    for i in range(size):
        c = 0
        for j in range(i, size):
            c = c + seq[j]
            if c == K:
                print(seq[i: j+1])

seq = [3, 4, -2, 2, -2]
getSumSeq(seq, K=0)



