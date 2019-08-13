#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 城市修建.py
@time: 2019/8/8 14:39
"""
"""
题目：
有一个城市需要修建，给你N个民居的坐标X,Y，问把这么多民居全都包进城市的话，城市所需最小面积是多少（注意，城市为平行于坐标轴的正方形）
输入：第一行为N，表示民居数目（2≤N≤1000）
输出：城市所需最小面积
例如：
输入
2
0 0
2 2 

输出
4
"""
# 思路：先求解x的极差，再求y的极差，最后求二者最大的极差
def square(points):
    xs = []
    ys = []
    for p in points:
        xs.append(p[0])
        ys.append(p[1])
    xm = max(xs) - min(xs)
    ym = max(ys) - min(ys)
    res = max(xm, ym)
    return res*res
n = int(input())
points = []
for i in range(n):
    p = [int(e) for e in input().split(" ")]
    points.append(p)
print(square(points))
