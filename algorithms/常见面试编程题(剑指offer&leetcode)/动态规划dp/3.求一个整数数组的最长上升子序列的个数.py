#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.求一个整数数组的最长上升子序列的个数.py
@time: 2019/8/18 19:14
"""
"""
leetcode 300: 求一个整数数组的最长上升子序列的个数
思路：动态规划+二分法
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路1：动态规划，令d[i]表示以nums[i]结尾的最长递增子序列的长度， 则有
        # d[i] = max_{0<=j<i}{d[j] + 1}, if nums[j] < nums[i]
        # 时间复杂度为O(n^2), 空间复杂度为O(n)
        if len(nums) == 0:
            return 0
        max_res = 1
        d = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and d[j] + 1 > d[i]:
                    d[i] = d[j] + 1
            if d[i] > max_res:
                max_res = d[i]
        return max_res

class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路二：二分查找，维护一个序列L，序列L的长度即为遍历到数组第i个元素时的最长递增子序列的长度，
        # 维护的L中每个元素都是当前最小的，新来的元素如果大于nums[len-1], 直接添加；否则直接二分查找插入即可
        # 时间复杂度为O(nlogn), 空间复杂度为O(n)
        # （注意二分查找：在一个数组中查找大于target中的最小数字）
        if len(nums) == 0:
            return 0
        L = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > L[len(L) - 1]:
                L.append(nums[i])
            else:
                # 二分查找加入，替换掉大于等于nums[i]的最小整数
                l, r = 0, len(L) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[i] <= L[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                # l 即为插入替换的位置
                L[l] = nums[i]
        return len(L)


class Solution3(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # (方法一:动态规划)
        # max_len = 0
        # # L[i]表示以nums[i]结尾的最长递增子序列的长度）O(n^2)
        # L = [1] * len(nums)
        # for i in range(len(nums)):
        #     # 表示最大的L[j]
        #     t = 0
        #     for j in range(i):
        #         if nums[i] > nums[j] and L[j] > t:
        #             t = L[j]
        #             L[i] = t + 1
        #     # 更新当前的最大值
        #     if L[i] > max_len:
        #         max_len = L[i]
        # return max_len

        # (方法二)
        # O(nlogn)
        # 维护一个序列L，序列L的长度即为遍历到数组第i个元素时的最长递增子序列的长度，
        # 维护的L中每个元素都是当前最小的，新来的元素如果大于nums[len-1], 直接添加；否则直接二分查找插入即可
        # 时间复杂度为O(nlogn), 空间复杂度为O(n)
        if len(nums) == 0:
            return 0
        L = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > L[len(L) - 1]:
                L.append(nums[i])
            else:
                # 二分查找替换掉L中大于等于nums[i]的最小的数字
                left = 0
                right = len(L) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[i] < L[mid]:
                        right = mid - 1
                    elif nums[i] > L[mid]:
                        left = mid + 1
                    else:
                        left = mid
                        break
                # 替换
                L[left] = nums[i]
        return len(L)


solution = Solution2()
nums = [10,9,2,5,3,7,101,18]
res = solution.lengthOfLIS(nums)
print(res)

# 二分查找
# def binary_search(nums, target):
#     l, r = 0, len(nums)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if target <= nums[mid]:
#             r = mid - 1
#         else:
#             l = mid + 1
#     return l
#
# nums = [1, 2, 3, 5, 6]
# nums2 = [1, 2, 3, 6]
# nums3 = [5]
# target = 4
# res = binary_search(nums3, target)
# print(res)