#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 序列交换.py
@time: 2019/8/3 16:06
"""
# n = int(input())
# nums = [int(e) for e in input().split(" ")]
# def get_array(n, nums):
#     for i in range(1, n):  # i表示迭代次数
#         for j in range(n - i):  # j表示下标
#             if (nums[j] + nums[j+1]) % 2 == 1:
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
# get_array(n, nums)
# print(" ".join(map(str, nums)))


# def quick_sort(nums, low, high):
#     if low < high:
#         p = partition(nums, low, high)
#         quick_sort(nums, 0, p-1)
#         quick_sort(nums, p+1, high)
#
# def partition(nums, low, high):
#     pivot = nums[high]
#     start = low
#     for i in range(low, high):
#         if nums[i] < pivot:
#             nums[start], nums[i] = nums[i], nums[start]
#             start += 1
#     nums[start], nums[high] = nums[high], nums[start]
#     return start
#
# quick_sort(nums, 0, n-1)
# print(" ".join(map(str, nums)))

n = 4
nums = [7, 3, 5, 1]
def get_array(n, nums):
    for i in range(1, n):  # i表示迭代次数
        for j in range(n - i):  # j表示下标
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
get_array(4, nums)
print(nums)