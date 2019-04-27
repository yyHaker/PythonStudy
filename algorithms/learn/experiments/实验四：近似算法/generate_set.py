#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: generate_set.py
@time: 2019/4/25 10:40
"""
import random

def generate_set(N=1000, M=1000):
    """
    随机产生指定大小的集合.
    :param N: 元素集合X的个数, (N>20).
    :param M:
    :return: 集合X: number_set，
                 子集族F: number_subset
    """
    M = N  # 令|X| == |F|
    number_set = [i for i in range(N)]    # 元素集合X
    number_subset_family = []   # 子集族F
    subset0 = random.sample(number_set, 20)  # 第一次生成的子集集合
    number_subset_family.append(set(subset0))  # add set
    choosed = set(subset0)  # 已取元素集合
    unchoosed = list(set(number_set).difference(set(choosed)))  # 剩余未取元素集合
    # 继续产生子集
    while len(unchoosed) > 20:
        subset = []
        n = random.randint(1, 20)  # the size of subset
        x = random.randint(1, n)
        subset += random.sample(unchoosed, x)
        subset += random.sample(choosed, n-x)
        number_subset_family.append(set(subset))
        # update choosed and unchoosed
        choosed = set.union(choosed, subset)
        unchoosed = list(set(unchoosed).difference(set(subset)))
    # 如果还有unchoosed，直接添加到集族
    if len(unchoosed) > 0:
        number_subset_family.append(set(unchoosed))
    # 继续生成子集
    while len(number_subset_family) < M:
        num = random.sample(number_set, random.randint(1, 20))
        if set(num) not in number_subset_family:
            number_subset_family.append(set(num))
    # weight if use
    # weight = [len(number_subset_family[i]) for i in range(M)]
    weight = [1 for i in range(M)]
    return number_set, number_subset_family, weight

if __name__ == "__main__":
    number_set, number_subset_family, _ = generate_set(100)
    print("子集大小: ", len(number_set))
    print("子集族大小:", len(number_subset_family))

