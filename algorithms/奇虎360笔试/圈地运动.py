#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 圈地运动.py
@time: 2019/8/8 15:55
"""
"""
题目：链接：https://www.nowcoder.com/questionTerminal/37554f9e45404fa785bd029e5f08280e?f=discussion
来源：牛客网

圈地运动，就是用很多木棍摆在地上组成一个面积大于0的多边形～
小明喜欢圈地运动，于是他需要去小红店里面买一些木棍，期望圈出一块地来。小红想挑战一下小明，所以给小明设置了一些障碍。障碍分别是：
1.如果小明要买第i块木棍的话，他就必须把前i-1块木棍都买下来。
2.买了的木棍都必须用在圈地运动中。
那么请问小明最少买多少根木棍，才能使得木棍围成的图形是个面积大于0多边形呢？

输入: 
3
6 8 10

输出：
3

思路：
假设有n条边，只需要其他n-1条边之和大于最长的那条边就可以构成多边形。
从头到尾统计前n条边之和，与最长边比较即可。没有答案输出-1
"""
def get_count(nums):
    # 得到圈地运动的最小木棍数量
    if len(nums) <= 2:
        return -1
    total = 0
    max_side = 0
    for i, m in enumerate(nums):
        total += m
        if m > max_side:
            max_side = m
        # 判断
        if i >= 2:
            if total - max_side > max_side:
                return i + 1
    return -1

n = int(input())
nums = [int(e) for e in input().split(" ")]
res = get_count(nums)
print(res)