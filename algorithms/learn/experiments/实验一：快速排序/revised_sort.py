#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: revised_sort.py
@time: 2019/4/25 19:18
"""
import random


def revised_quickSort(A, p, r):
    """random quick sort.
    :param A: a list
    :param p: left index
    :param r: right index
    :return:
    """
    if p < r:
        q_left, q_right = _rand_partition(A, p, r)
        revised_quickSort(A, p, q_left-1)
        revised_quickSort(A, q_right+1, r)


def _rand_partition(num, left, right):
    """
    :param num: array
    :param left: min index of num
    :param right: max index of num
    :return: flag
    """
    flag = random.randint(left, right)
    label = num[flag]
    # 下面变量依次为左边等于label的数应该交换的位置、左指针；右边等于label应该交换的位置，右指针
    flag_left, index_left, flag_right, index_right = left, left, right, right

    # 将与label相等的值分别移动到左右两边
    while True:
        while index_left <= index_right and num[index_left] <= label:
            if num[index_left] == label:
                num[flag_left], num[index_left] = num[index_left], num[flag_left]
                flag_left += 1
            index_left += 1
        while index_right >= index_left and num[index_right] >= label:
            if num[index_right] == label:
                num[flag_right], num[index_right] = num[index_right], num[flag_right]
                flag_right -= 1
            index_right -= 1
        if index_left > index_right:
            break
        num[index_right], num[index_left] = num[index_left], num[index_right]
        index_left += 1; index_right -= 1

    # 将两边相等的值移动到flag附近，完成三分类
    i, j = index_right, left
    while j < flag_left and num[i] != label:
        num[i], num[j] = num[j], num[i]
        i -= 1; j += 1
    i, j = index_left, right
    while j > flag_right and num[i] != label:
        num[i], num[j] = num[j], num[i]
        i += 1; j -= 1
    # 返回值分别表示对应下标的左边全部小于label， 对应下标的右边全部大于label
    return index_left - (flag_left - left), index_right + (right - flag_right)


def _exchange(A, i, j):
    """exchange A[i] and A[j]"""
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
