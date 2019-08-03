#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 数字圆环.py
@time: 2019/8/3 16:46
"""
def get_res(count, nums):
    out = []
    sum_min = 99999
    index_left = 0
    flag = 1
    for i in range(int(count)):
        if i == 0:
            out.append(int(nums[0]))
            sum_min = nums[0]
            index_left = 0
        elif i == 1:
            out.append(int(nums[1]))
            sum_min = nums[0] + nums[1]
            index_left = 0
        else:
            if nums[i] < sum_min:
                out.insert(index_left, nums[i])
            else:
                flag = 0
    if flag == 1:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for idx in range(T):
    n = int(input())
    nums = [int(e) for e in input().split(" ")]
    res = get_res(n, nums)
    print(res)
