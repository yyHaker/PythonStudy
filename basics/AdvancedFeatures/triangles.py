# -*- coding: utf-8 -*-
# 输出杨辉三角
# 下面函数思路在每一行补一个0
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n=0
for t in triangles():
    print(t)
    n = n+1
    if n==10:
        break