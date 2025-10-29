#!/usr/bin/python
# coding:utf-8

"""题目：求一个数组中第K大数字，要求时间复杂读O(N)
@author: yyhaker
@contact: 572176750@qq.com
@file: quick_sort.py
@time: 2025/10/29

target = n-K 表示第K大的数的索引，划分点i，依次去二分查找第K大的数，
如果i==target_idx，返回该值；如果i > target_idx，说明第K大的值在左边；如果i < target_idx，说明第K大的值在右边


"""
from random import randint

def findKthLargest(nums, K):
    n = len(nums)
    target_idx = n - K
    left, right = 0, n-1
    while True:
        i = partition(nums, left, right)
        if i == target_idx:
            return nums[i]
        elif i > target_idx:
            right = i - 1
        else:
            left = i + 1


def partition(nums, left, right):
    idx = randint(left, right)
    pivot = nums[idx]
    # 将划分点放在左边
    nums[left], nums[pivot] = nums[pivot], nums[left]

    i, j = left + 1, right
    while True:
        while i <= j and nums[i] < pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        
        if i > j:
            break

        # |pivot|...i....j....|
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    # 将划分点放在j的位置
    nums[left], nums[j] = nums[j], nums[left]
    return j
