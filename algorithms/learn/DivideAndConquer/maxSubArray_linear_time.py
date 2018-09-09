# -*- coding: utf-8 -*-
"""
线性时间求解最大子数组问题.
思路：若已知A[1..j]的最大子数组，可以迭代求出A[1...j+1]的最大子数组.
                              | - A[1...j]的最大子数组 (前最大子数组)
A[1...j] -> A[1...j+1]  |                                                                           | - (只包含A[j+1])
                             |-  是某个数组A[i...j+1] (1=<i<=j+1) (边界最大子数组) |
                                                                                                        | - (不只包含A[j+1]) (前一个元素的边界最大子数组+A[j+1])
从左向右循环，依次保存前最大子数组和边界最大子数组， 然后求出每一轮A[1...j+1]的最大子数组.
时间复杂度O(n).
"""
def find_max_sub_array(A, low, high):
    maxarray, boundary = A[low], A[low]
    for j in range(low+1, high):
        if boundary + A[j] > A[j]:
            boundary += A[j]
        else:
            boundary = A[j]
        if boundary > maxarray:
            maxarray = boundary
    return maxarray

if __name__ == "__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    maxarray = find_max_sub_array(A, 0, 15)
    print(maxarray)
