# -*- coding: utf-8 -*-
"""
寻找一列数的最大子数组, ex. [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7].
---
思路１：分治法, 将问题分解为求解A[low, mid] 、A[mid, high] 以及跨越前两者之间的最大子数组.
　时间复杂度O(n log n).
"""
def find_max_crossing_subarray(A, low, mid, high):
    sum = 0
    left_sum = -float('inf')
    max_left = mid
    for i in range(mid, low, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    right_sum = -float('inf')
    max_right = mid+1
    for j in range(mid+1, high, 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

def find_max_subarray(A, low, high):
    """分治法求解"""
    if low == high:
        return low, low, A[low]
    mid = (low + high) // 2  # 向下取整
    # 递归求解
    left_i, left_j, left_sum = find_max_subarray(A, low, mid)
    right_i, right_j, right_sum = find_max_subarray(A, mid+1, high)
    mid_i, mid_j, mid_sum = find_max_crossing_subarray(A, low, mid, high)
    # 找最大的
    if left_sum > right_sum and left_sum > mid_sum:
        return left_i, left_j, left_sum
    elif right_sum > left_sum and right_sum > mid_sum:
        return right_i, right_j, right_sum
    else:
        return mid_i, mid_j, mid_sum

if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    B = [1, -4, 3, -4]
    max_i, max_j, max_sum = find_max_subarray(A, 0, 15)
    # max_i, max_j, max_sum = find_max_subarray(B, 0, 3)
    print(max_i, max_j, max_sum)