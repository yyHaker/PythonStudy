#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.盛最多水的容器.py
@time: 2019/8/9 21:26
"""
"""
leetcode11: 盛最多水的容器
思路：双指针
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 思路：双指针, 每次移动短板所在的指针（可用反证法证明）,在这个过程中更新最大值
        l, r = 0, len(height) - 1
        cur = 0
        while l < r:
            if min(height[l], height[r]) * (r - l) > cur:
                cur = min(height[l], height[r]) * (r - l)
            # 判断是左指针动还是右指针动
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1
        return cur
