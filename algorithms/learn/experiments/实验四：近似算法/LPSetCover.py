#!/usr/bin/python
# coding:utf-8
"""
@author: yyhaker
@contact: 572176750@qq.com
@file: maze.py
@time: 2019/4/22 09:47
"""
import pulp
from generate_set import generate_set
import random
import time

def lp_solve(x, weight, f):
    """
    利用pulp包求解lp松弛问题的精确解，以及集合元素的频率集合freq
    :param x: 数据集合
    :param weight: 集族中每个集合的权重, [0, 1]
    :param f: 集合子集族
    :return:
    """
    # 集合大小
    n = len(x)
    # 设置对象
    prob = pulp.LpProblem('mypro', pulp.LpMinimize)

    # 设置决策变量
    flag = [0 for i in range(n)]
    for i in range(n):
        flag[i] = pulp.LpVariable("flag" + str(i), lowBound=0, cat=pulp.LpContinuous)

    # 目标函数
    z = 0
    for i in range(n):
        z += flag[i] * weight[i]
    prob += z

    # 载入约束变量
    freq = [0 for i in range(n)]  # 元素在集族F中的频度
    for i in range(n):
        sum = 0   #
        for j in range(n):
            if x[i] in f[j]:
                sum += flag[j]  # 集族F中至少有一个集合S包含元素X[i]
                freq[i] += 1
        prob += sum >= 1

    # 求解lp问题的精确解
    prob.solve()
    # print(prob)
    result = [0.0 for i in range(n)]
    for v in prob.variables():
        # print(v.name, "=", v.varValue)
        result[int(v.name[4:])] = v.varValue
    # print(result)
    return result, freq

def LP_set_cover(number_subset_family, result, freq):
    """舍入法求解集合覆盖问题.
    :param number_subset_family: 集合子集族
    :param result: 利用pulp包求解lp松弛问题的精确解Xs
    :param freq: 集合中元素的频率集合freq
    :return: 满足条件的集族sub_set_family
    """
    n = len(number_subset_family)
    sub_set_family = []
    # 元素在集族F中的最大频率
    max_f = max(freq)
    for i in range(n):
        if result[i] >= 1 / max_f:
            sub_set_family.append(number_subset_family[i])
    return sub_set_family


def exp1():
    """小样本测试"""
    X, F, W = generate_set(50)
    print('生成集合大小: ', len(X))
    print('生成集合： ', X)
    print('生成集合子集族大小: ', len(F))
    print('生成集合子集族: ', F)
    start = time.clock()
    result, temp = lp_solve(X, W, F)
    C = LP_set_cover(F, result, temp)
    end = time.clock()
    print('Run time is: {} s'.format(round((end - start), 3)))
    print('Results are: ')
    for num in C:
        print(num)
    # 检验获取的子集族C是否可行
    temp = []
    for num in C:
        temp += num
    print('解集C检验: ')
    print('解集C大小', len(set(temp)))
    print('解集集合并集:', set(temp))

def exp2():
    """大规模数据实验"""
    # 大规模数据生成测试
    count = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 10000]
    costs = []
    for n in count:
        X, F, W = generate_set(n)
        start = time.clock()
        result, temp = lp_solve(X, W, F)
        C = LP_set_cover(F, result, temp)
        end = time.clock()
        print('Input size:', n, end=' ')
        print('Run time is: {} s'.format(round((end - start), 3)))

if __name__ == "__main__":
    exp2()

