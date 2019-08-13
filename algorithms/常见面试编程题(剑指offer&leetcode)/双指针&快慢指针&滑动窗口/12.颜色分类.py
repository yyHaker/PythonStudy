#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.颜色分类.py
@time: 2019/8/9 22:09
"""
"""
leetcode75:  颜色分类
思路：双指针
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：双指针，前后设置两个指针，依次从前到后遍历，如果碰到0换到左边，碰到1跳过，碰到2换到右边
        # 时间复杂度为O(n), 空间复杂度为O(1)
        zero = 0
        two = len(nums)-1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1