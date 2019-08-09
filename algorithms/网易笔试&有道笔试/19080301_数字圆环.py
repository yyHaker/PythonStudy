#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 数字圆环.py
@time: 2019/8/3 16:46
"""
"""
网易有道笔试题目：
            数字圆环：给定n个数字，a_1, a_2, a_3...a_n. 其中每个数字都是大于等于1的正整数, 请判断这n个数字是否可以构成一个数字圆环？
 要求：该数比相邻两数相加之和小，从而形成一个数字圆环，an的相邻两数为an-1与a1，数字顺序可以调换。
 如输入为1 7 3 5 最后可以得出一种排列为1 3 7 5 满足数字圆环。
 注意：nums数字的个数至少为3
 思路：先排序，最后只需要判断倒数第二个数字、倒数第一个数字、以及第一个数字
"""

def is_circle(nums):
    # 判断nums数组中的数字能否构成数字圆环
    nums = sorted(nums)
    if nums[0] + nums[-2] > nums[-1]:
        return True
    else:
        nums[-2], nums[-1] = nums[-1], nums[-2]
        # 判断nums[-2]
        if nums[-2] < nums[-3] + nums[-1]:
            return True
        else:
            return False

T = int(input())
for idx in range(T):
    n = int(input())
    nums = [int(e) for e in input().split(" ")]
    res = is_circle(nums)
    if res:
        print("true")
    else:
        print("false")
