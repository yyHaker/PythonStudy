#!/usr/bin/python
# coding:utf-8

"""随机快排
@author: yyhaker
@contact: 572176750@qq.com
@file: quicksort.py
@time: 2019/4/21 10:23
"""
import copy
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from revised_sort import revised_quickSort
from non_recursive_quicksort import non_rec_quicksort


def quickSort(A, p, r):
    """random quick sort.
    :param A: a list
    :param p: left index
    :param r: right index
    :return:
    """
    if p < r:
        q = _rand_partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

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


# experiments below
def exp1(scale=1000000):
    A = [random.randint(-214783648, 2147483647) for i in range(scale)]
    start = time.time()
    revised_quickSort(A, 0, scale-1)
    # quickSort(A, 0, scale-1)  # cost 5.6s
    # sorted(A)  # 调用内部sort只需0.60s
    end = time.time()
    print("sort 1000000 random 32bit int num costs time: {}ms".format(round((end-start)*1000, 3)))
    return scale, end-start

def exp11():
    """探索输入规模和算法运行时间的关系"""
    X = []
    Y = []
    for s in range(10, 1000000, 4000):
        scale, cost_time = exp1(scale=s)
        X.append(scale)
        Y.append(cost_time)
    X = np.array(X)
    Y = np.array(Y)
    plt.figure(figsize=(8, 4))
    plt.plot(X, Y, color="red", linewidth=2)
    plt.xlabel("input scale")
    plt.ylabel("time(ms)")
    plt.title("input scale and algorithm run time")
    # plt.savefig('run_time.png')
    plt.show()

def exp2():
    A = [1] * 1000000
    start = time.time()
    # # quickSort(A, 0, 1000000 - 1)  # 栈溢出
    # sorted(A)    # 调用内部sort只需0.017s
    revised_quickSort(A, 0, len(A)-1)
    end = time.time()
    print("sort 1000000 1  costs time: {}ms".format(round((end-start)*1000, 3)))

def exp3(scale=10000, one_rate=0.5):
    one_num = int(scale * one_rate)
    A = [1] * one_num + [random.randint(-214783648, 2147483647) for i in range(scale - one_num)]
    start = time.time()
    # quickSort(A, 0, scale-1)
    # sorted(A)
    revised_quickSort(A, 0, scale-1)
    end = time.time()
    cost_time = round((end-start)*1000, 3)
    print("sort {} nums, contain %{} one, cost time: {}ms".format(scale, 100 * one_rate, cost_time))
    return one_rate, cost_time

def exp33(scale=1000):
    """探索不同比例的1与算法运行时间的关系"""
    X = []
    Y = []
    for rate in range(1, 10):
        one_rate, cost_time = exp3(scale, one_rate=rate/10.)
        X.append(one_rate)
        Y.append(cost_time)
    X = np.array(X)
    Y = np.array(Y)
    plt.figure(figsize=(8, 4))
    plt.plot(X, Y, color="red", linewidth=2)
    plt.xlabel("one rate")
    plt.ylabel("time(ms)")
    plt.title("one rate and algorithm run time")
    plt.show()

def analyze_onerate(scale=1000):
    """探索不同比例的1与不同算法运行时间的关系"""
    quick_sort_times = []
    revised_sort_times = []
    in_sort_times = []
    one_rates = []
    for rate in range(1, 10):
        # generate data
        one_rate = rate / 10.
        one_rates.append(one_rate)
        one_num = int(scale * one_rate)
        A = [1] * one_num + [random.randint(-214783648, 2147483647) for i in range(scale - one_num)]
        B = copy.deepcopy(A)
        C = copy.deepcopy(A)

        # for 该随机快排
        start = time.time()
        quickSort(A, 0, scale-1)
        end = time.time()
        q_time = round((end-start)*1000, 3)  # ms
        quick_sort_times.append(q_time)

        # for revised 随机快排
        start = time.time()
        revised_quickSort(B, 0, scale-1)
        end = time.time()
        re_time = round((end-start)*1000, 3)
        revised_sort_times.append(re_time)

        # for builtin sorted
        start = time.time()
        sorted(C)
        end = time.time()
        in_time = round((end-start)*1000, 3)  # ms
        in_sort_times.append(in_time)

    # plot the result
    plt.figure(figsize=(8, 4))
    plt.plot(one_rates, quick_sort_times, color="red", linewidth=2, label="quicksort")
    plt.plot(one_rates, revised_sort_times, color="blue", linewidth=2, label="revised quicksort")
    plt.plot(one_rates, in_sort_times, color="black", linewidth=2, label="python builtin sorted")
    plt.xlabel("one rate")
    plt.ylabel("algorithm run time(ms)")
    plt.title("Algorithm run time for different one rate")
    plt.legend()
    plt.show()


def analyze_scale(scales=[1000, 2000, 3000, 5000, 10000, 20000, 30000]):
    """探索不同的数据规模与不同算法运行时间的关系"""
    quick_sort_times = []
    revised_sort_times = []
    in_sort_times = []
    non_sort_times = []
    for scale in scales:
        # generate data
        A = [random.randint(-214783648, 2147483647) for i in range(scale)]
        B = copy.deepcopy(A)
        C = copy.deepcopy(A)
        D = copy.deepcopy(A)

        # for 该随机快排
        start = time.time()
        quickSort(A, 0, scale-1)
        end = time.time()
        q_time = round((end-start)*1000, 3)  # ms
        quick_sort_times.append(q_time)

        # for revised 随机快排
        start = time.time()
        revised_quickSort(B, 0, scale-1)
        end = time.time()
        re_time = round((end-start)*1000, 3)
        revised_sort_times.append(re_time)

        # for builtin sorted
        start = time.time()
        sorted(C)
        end = time.time()
        in_time = round((end-start)*1000, 3)  # ms
        in_sort_times.append(in_time)

        # for non-recu sort
        start = time.time()
        non_rec_quicksort(D, 0, scale)
        end = time.time()
        non_time = round((end - start) * 1000, 3)  # ms
        non_sort_times.append(non_time)

    # plot the result
    plt.figure(figsize=(8, 4))
    plt.plot(scales, quick_sort_times, color="red", linewidth=2, label="quicksort")
    plt.plot(scales, revised_sort_times, color="blue", linewidth=2, label="revised quicksort")
    plt.plot(scales, in_sort_times, color="black", linewidth=2, label="python builtin sorted")
    plt.plot(scales, non_sort_times, color="yellow", linewidth=2, label="non recur sorted")
    plt.xlabel("the data scale")
    plt.ylabel("algorithm run time(ms)")
    plt.title("Algorithm run time for different scales")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # exp1()
    exp2()
    # exp3(1000, one_rate=0.9)
    # exp33(scale=1000)
    # exp11()
    # analyze_onerate()
    # analyze_scale()

