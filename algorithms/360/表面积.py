#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 表面积.py
@time: 2019/8/15 20:40
"""

def get_res(nums):
    N = len(nums)
    M = len(nums[0])
    res = 0
    for i in range(N):
        for j in range(M):
            if nums[i][j]:
                res += 2
                for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= ni < N and 0 <= nj < M:
                        value = nums[ni][nj]
                    else:
                        value = 0
                    res += max(nums[i][j] - value, 0)
    return res

n, m = [int(num) for num in input().strip().split(' ')]
nums = [[] for j in range(n)]

for i in range(n):
    nums[i] = [int(num) for num in input().strip().split(' ')]
res = get_res(nums)
print(res)
