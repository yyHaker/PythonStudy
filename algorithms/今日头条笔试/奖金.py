#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 奖金.py
@time: 2019/8/11 19:38

# 测试用例
2 2 3 3 2 1 4 3 1 2
"""
def min_reward(nums):
    last_reward = 0
    sum_reward = 0
    for i in range(len(nums)):
        # 每次判断这个人的年限是否高于上一个人，高则给他多给100;
        # 低则给他少给100，若上一个人为100，那么上一个人以及他之前部分人(满足某个要求)都要多给100。
        if i == 0 or nums[i] > nums[i-1]:
            current_reward = last_reward + 100
        elif nums[i] == nums[i-1]:
            current_reward = last_reward
        else:
            if last_reward > 100:
                current_reward = last_reward - 100
            else:
                current_reward = 100
                k = i - 1
                while k >= 0:
                    if nums[k] >= nums[k+1]:
                        sum_reward += 100
                        k = k - 1
                    else:
                        break
        last_reward = current_reward
        sum_reward += current_reward
    return sum_reward

N = int(input())
nums = [int(e) for e in input().split(" ")]
res = min_reward(nums)
print(res)