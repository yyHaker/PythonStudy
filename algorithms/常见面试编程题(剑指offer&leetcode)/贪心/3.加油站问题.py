#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.加油站问题.py
@time: 2019/8/21 10:24
"""
"""
leetcode134: 加油站问题
思路：贪心
参考：https://leetcode-cn.com/problems/gas-station/submissions/
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 思路：贪心，累加在每个位置的left += gas[i] - cost[i], 就是在每个位置剩余的油量,
        # 如果left一直大于0, 就可以一直走下取. 如果left小于0了, 那么就从下一个位置重新开始计数,
        # 并且将之前欠下的多少记录下来, 如果最终遍历完数组剩下的燃料足以弥补之前不够的,
        # 那么就可以到达, 并返回最后一次开始的位置.否则就返回-1。
        # 时间复杂度为O(n)
        start, left, lack = 0, 0, 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if left < 0:
                lack += left
                start = i + 1
                left = 0
        if left + lack >= 0:
            return start
        else:
            return -1
