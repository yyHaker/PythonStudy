#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: non_recursive_quicksort.py
@time: 2019/4/25 20:34
"""
import random


def non_rec_quicksort(A, p, r):
    """使用栈实现非递归的快速排序
    :param A:
    :param p: left index
    :param r: right index
    :return:
    """
    if len(A) < 2:
        return A
    stack = []
    stack.append(len(A)-1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = _rand_partition(A, l, r)
        if l < index - 1:
            stack.append(index-1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index+1)


def _rand_partition(A, p, r):
    """
    :param A:
    :param p:
    :param r:
    :return:
    """
    # random choose a partition x
    i = random.randint(p, r)
    _exchange(A, r, i)
    x = A[r]
    # keep A[p...i] <= x
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            _exchange(A, j, i)
    # exchange partition to i+1
    _exchange(A, r, i+1)
    return i+1

def _exchange(A, i, j):
    """exchange A[i] and A[j]"""
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

if __name__ == "__main__":
    A = [2, 1, 3, 4, 2, 10, 40, 28]
    non_rec_quicksort(A, 0, len(A) - 1)
    print(A)