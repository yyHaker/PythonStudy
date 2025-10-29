#!/usr/bin/python
# coding:utf-8

"""题目：写一个快速排序算法，时间复杂度要求O(nLogN)，最坏的情况是O(N^2)
@author: yyhaker
@contact: 572176750@qq.com
@file: quick_sort.py
@time: 2025/10/29
"""
from random import randint

def quick_sort(nums, start, end):
    # 使用partition函数划分数组
    if start < end:
        pivot = partition(nums, start, end)

        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)

# def partition(nums, start, end):
#     pivot_value = nums[start]
#     l = start+1
#     r = end

#     while l <= r:
#         # |start|.l..pivot..r..|end|
#         while l <= r and nums[l] <= pivot_value:
#             l = l + 1
#         while r >= l and nums[r] >= pivot_value:
#             r = r - 1
        
#         # swap
#         nums[l], nums[r] = nums[r], nums[l]
    
#     # sawp first and right
#     nums[start], nums[r] = nums[r], nums[start]
#     return r


def partition(nums, left, right):
    """
    分治法划分数组
    """
    i = randint(left, right)
    pivot = nums[i]
    # 划分点放在最左边
    nums[i], nums[left] = nums[left], nums[i]

    i,j = left+1, right
    while True:
        while i<=j and nums[i] < pivot:
            i += 1
        while i<=j and nums[j] > pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # 将划分点放在j位置
    nums[left], nums[j] = nums[j], nums[left]
    # 返回pivot下标
    return j
        


if __name__ == "__main__":
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)