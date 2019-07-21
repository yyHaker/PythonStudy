#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 13.计算右侧小于当前元素的计数数组.py
@time: 2019/7/20 17:30
"""
"""
leetcode315: 计算右侧小于当前元素的计数数组
思路：归并排序+索引数组
时间复杂度O(NlogN)，空间复杂度O(N)
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]

        # 索引数组和临时数组
        temp = [None for _ in range(size)]
        indexes = [i for i in range(size)]
        res = [0 for _ in range(size)]

        self._helper(nums, 0, size - 1, temp, indexes, res)
        return res

    def _helper(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = (left + right) // 2

        # count left
        self._helper(nums, left, mid, temp, indexes, res)
        # count right
        self._helper(nums, mid + 1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self._sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def _sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # [left, mid]前有序数组
        # [mid+1, right]后有序数组

        # 先拷贝，再合并
        for i in range(left, right + 1):
            temp[i] = indexes[i]

        l = left
        r = mid + 1
        for i in range(left, right + 1):
            if l > mid:
                # l 用完，就拼命使用 r
                # [1,2,3,4] [5,6,7,8]
                indexes[i] = temp[r]
                r += 1
            elif r > right:
                # r 用完，就拼命使用 l
                # [6,7,8,9] [1,2,3,4]
                indexes[i] = temp[l]
                l += 1
                # 注意：此时前面剩下的数，比后面所有的数都大
                res[indexes[i]] += (right - mid)
            elif nums[temp[l]] <= nums[temp[r]]:
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[l]
                l += 1
                # 注意：
                res[indexes[i]] += (r - mid - 1)
            else:
                assert nums[temp[l]] > nums[temp[r]]
                # 上面两种情况只在其中一种统计就可以了
                # [3,5,7,9] [4,6,8,10]
                indexes[i] = temp[r]
                r += 1
