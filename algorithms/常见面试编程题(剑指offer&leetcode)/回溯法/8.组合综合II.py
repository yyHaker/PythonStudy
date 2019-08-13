#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 8.组合综合II.py
@time: 2019/8/6 11:12
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 思路：回溯法，依次从候选列表中寻找数据；
        # 注意为了防止重复，按照指定顺序找
        res = []
        cur = []
        candidates = sorted(candidates)
        self.dfs(candidates, cur, target, 0, res)
        return res

    def dfs(self, candidates, cur, target, last, res):
        if sum(cur) == target:
            res.append(cur[:])
            return
        else:
            for m in candidates:
                if m >= last and sum(cur) + m <= target:
                    self.dfs(candidates, cur + [m], target, m, res)