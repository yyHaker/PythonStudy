#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: generate_set.py
@time: 2019/4/25 10:40
"""
import time
from generate_set import generate_set


def greedy_set_cover(number_set, number_subset_family):
    """贪心选择思想的集合覆盖算法.
    :param number_set: 集合
    :param number_subset_family: 集合子集的集族
    :return: 满足条件的集族result
    """
    n = len(number_set)
    result = []
    flag = [0 for i in range(n)]  # 0表示此子集未被选取
    number_set = set(number_set)
    # 当还有未被覆盖的元素
    while len(number_set) > 0:
        temp = 0
        count = n
        #  选择包含未被覆盖元素最多的那个集合
        for i in range(n):
            if flag[i] == 0 and len(number_set.difference(set(number_subset_family[i]))) < count:
                temp = i
                count = len(number_set.difference(set(number_subset_family[i])))
        result.append(number_subset_family[temp])
        number_set = number_set.difference(set(number_subset_family[temp]))
        flag[temp] = 1
    return result

def exp1():
    """小样本测试"""
    x, f, _ = generate_set(100)
    print('生成集合大小: ', len(x))
    print('生成集合： ', x)
    print('生成集合子集族大小: ', len(f))
    print('生成集合子集族: ', f)
    start = time.clock()
    result = greedy_set_cover(x, f)
    end = time.clock()
    print('Run time is: {}s'.format(round((end - start), 3)))
    print('Results are: ')
    for num in result:
        print(num)
    # 检验获取的子集族C是否可行
    temp = []
    for num in result:
        temp += num
    print('解集C检验: ')
    print('解集C大小', len(set(temp)))
    print('解集集合并集:', set(temp))

def exp2():
    """大规模数据实验"""
    # 大规模数据生成测试
    count = [100, 200, 500, 1000, 2000, 3000, 4000, 5000]
    result = []
    for n in count:
        x, f, _ = generate_set(n)
        start = time.clock()
        temp = greedy_set_cover(x, f)
        end = time.clock()
        print('Input size:', n, end=' ')
        print('Run time is: {} s'.format(round((end - start), 3)))
        result.append(end - start)

if __name__ == "__main__":
    exp1()
