#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 序列交换.py
@time: 2019/8/3 16:06
"""
"""
网易有道笔试题目：
给定n个数字a_1, a_2, ..., a_n， 你可以对这个数组执行任意次以下交换操作：
    对于数组中的两个下标i,j(1<=i,j<=n)，如果a_i+a_j为奇数，那么交换这两个数
现在允许我们的交换次数不限，求出能够通过若干次数操作后得到的数组中字典序最小的一个
例如：
样例1：
输入： 7 3 5 1
输出： 7 3 5 1

样例2：
输入：53941 38641 31525 75864 29026 12199 83522 58200 64784 80987
输出：12199 29026 31525 38641 53941 58200 64784 75864 80987 83522  

思路：如果数组中只有偶数或者奇数，没法交换；
          如果数组中既有偶数也有奇数，可以无限次数交换，交换后的顺序即为数组最后排序的结果！
例如：输入的是 5, 6, 4, 1, 3
最后一定会换成 1, 3, 4, 5, 6
(吐槽：这是考脑筋急转弯吗？)
"""

def seq_change(nums):
    even = 0
    odd = 0
    for m in nums:
        if m % 2 == 1:
            odd += 1
        else:
            even += 1
    if even > 0 and odd > 0:
        return sorted(nums)
    else:
        return nums


n = int(input())
nums = [int(e) for e in input().split(" ")]
res = seq_change(nums)
print(" ".join(map(str, res)))
