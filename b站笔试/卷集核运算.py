#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 卷集核运算.py
@time: 2019/8/20 19:47
"""

# def calc_conv(h, w, P, m, filters):
#     high = h - m + 1
#     width = w - m + 1

h, w = tuple(map(int, input().strip().split()))
p = []
for i in range(h):
    t = list(map(int, input().strip().split()))
    p.append(t)
m = int(input().strip())
k = []
for i in range(m):
    t = list(map(float, input().strip().split()))
    k.append(t)

for i in range(h - m + 1):
    for j in range(w - m + 1):
        t = 0
        for x in range(m):
            for y in range(m):
                t += p[i + x][j + y] * k[x][y]
        print(min(int(t), 255), end=' ')
    print()



"""
3 3
40 24 135
200 239 238
90 34 94
2
0.0 0.6
0.1 0.3
"""
