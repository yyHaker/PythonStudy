#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 序列重组.py
@time: 2019/8/15 20:16
"""

def get_res(n, m, nums1, nums2):
    # 思路：依次产生最大的数字，添加到res中
    res = []
    used1 = [0] * len(nums1)
    used2 = [0] * len(nums2)
    while len(res) < n:
        cur_max = -1
        max_i = -1
        max_j = -1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if not used1[i] and not used2[j] and (nums1[i] + nums2[j]) % m > cur_max:
                    cur_max = (nums1[i] + nums2[j]) % m
                    max_i = i
                    max_j = j
        #
        res.append(cur_max)
        used1[max_i] = 1
        used2[max_j] = 1
    return res

# 输入输出
p = [int(e) for e in input().strip().split(" ")]
n, m = p[0], p[1]
nums1 = [int(e) for e in input().strip().split(" ")]
nums2 = [int(e) for e in input().strip().split(" ")]
# n = 5
# m = 5
# nums1 = [4, 4, 1, 1, 1]
# nums2 = [4, 3, 0, 1, 2]
res = get_res(n, m, nums1, nums2)
print(" ".join(map(str, res)))
