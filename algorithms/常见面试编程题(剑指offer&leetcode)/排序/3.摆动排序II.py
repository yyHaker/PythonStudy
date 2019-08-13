#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.摆动排序II.py
@time: 2019/8/11 11:04
"""
"""
leetcode324: 摆动排序
思路：
    1. 将nums升序排列，分为两边，然后倒序交叉排列即可。 时间复杂度为O(nlogn), 空间复杂度为O(n)
    2. 先找出中位数mid, 再用中位数mid对数组进行三路划分。时间复杂度为O(n), 空间复杂度为O(1)

吐槽：同样的思路c++实现效率很高，而python实现效率很低超时
"""
class Solution1(object):
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：将nums升序排列，分为两边，然后倒序交叉排列即可
        nums.sort()
        mid = (0 + len(nums)+1) // 2
        left = nums[: mid]
        right = nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mid = self.findKthLargest(nums, (len(nums)+1) // 2)

        # remap the index
        m = lambda x: (2 * x + 1) % (len(nums) | 1)

        # 三路划分
        beg, end, cur = 0, len(nums)-1, 0
        while cur <= end:
            if nums[m(cur)] > mid:  # 放在1， 3， 5
                nums[m(cur)], nums[m(beg)] = nums[m(beg)], nums[m(cur)]
                cur += 1
                beg += 1
            elif nums[m(cur)] < mid:  # 放在0， 2， 4
                nums[m(cur)], nums[m(end)] = nums[m(end)], nums[m(cur)]
                end -= 1
            else:
                cur += 1
        print(nums)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        n = len(nums)
        while low <= high:
            p = self.partition(nums, low, high)
            if p == n - k:
                return nums[p]
            elif p > n - k:
                high = p - 1
            else:
                low = p + 1

    def partition(self, nums, low, high):
        # 二路划分
        pivot = nums[high]
        start = low
        for i in range(low, high):
            if nums[i] < pivot:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
        nums[start], nums[high] = nums[high], nums[start]
        return start

nums = [1, 3, 2, 2, 3, 1]
nums2 = [1, 5, 1, 1, 6, 4]
nums3 = [2, 1, 3, 6, 5, 7, 3]
nums4 = [1, 2, 3, 4, 5, 6]
solution = Solution()
solution.wiggleSort(nums4)


