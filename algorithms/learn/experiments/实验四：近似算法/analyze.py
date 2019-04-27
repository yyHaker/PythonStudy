#!/usr/bin/python
# coding:utf-8

"""集合覆盖问题的算法比较
@author: yyhaker
@contact: 572176750@qq.com
@file: analyze.py
@time: 2019/4/25 16:03
"""
import time
import matplotlib.pyplot as plt
from generate_set import generate_set
from GreedySetCover import greedy_set_cover
from LPSetCover import lp_solve, LP_set_cover

def main():
    # 大规模数据生成测试()
    count = [100, 200, 500, 1000, 2000, 3000, 4000, 5000]
    greedy_costs = []
    lp_costs = []
    for n in count:
        # generate data
        X, F, W = generate_set(n)
        # for lp algorithm
        start = time.clock()
        result, temp = lp_solve(X, W, F)
        C = LP_set_cover(F, result, temp)
        end = time.clock()
        lp_time = round((end - start), 3)
        lp_costs.append(lp_time)
        # for greedy
        start = time.clock()
        res = greedy_set_cover(X, F)
        end = time.clock()
        greedy_time = round((end - start), 3)
        greedy_costs.append(greedy_time)
        print('Input size:', n, end=' ')
        print('Run time for LP set cover: {} s, for greedy set cover: {} s'.format(lp_time, greedy_time))

    # plot the graph
    plt.figure(figsize=(8, 4))
    plt.plot(count, lp_costs, color="red", linewidth=2, label="LP")
    plt.plot(count, greedy_costs, color="blue", linewidth=2, label="greedy")
    plt.xlabel("the size of number set(n)")
    plt.ylabel("time(s)")
    plt.title("Algorithm run time LP and Greedy")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
