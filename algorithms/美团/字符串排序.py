#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 字符串排序.py
@time: 2019/8/22 16:18
"""
"""
美团笔试题目：不能使用sort函数，逆序排序字符串数组, 比如"wbd"在"bbd"前面，
"abc"在"abcdef"前面
思路：快排思想
时间复杂度为O(nlogn)
"""
def notLarge(str1, str2):
    minlen = min(len(str1), len(str2))
    for i in range(minlen):
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False
    return len(str1) <= len(str2)


def quicksort(list, p, r):
    if p < r:
        q = partion(list, p, r)
        quicksort(list, p, q)
        quicksort(list, q+1, r)

def partion(list, p, r):
        i = p-1
        for j in range(p, r):
            if notLarge(list[j], list[r]):  # list[j]<=list[r]:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[r] = list[r], list[i+1]
        return i


strlist = input().strip().split(',')
quicksort(strlist, 0, len(strlist)-1)
print(','.join(strlist))