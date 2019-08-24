#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1.数组中出现次数超过一半的数字.py
@time: 2019/7/14 09:56
"""
"""
剑指offer： 数组中出现次数超过一半的数字
leetcode169: 求众数
思路：利用数组的特点，在遍历数组的时候，保存两个值：数字和次数；如果下一个
        数字和保存的数字相等，次数加1；不等，次数减1。如果次数为0，需要保存下一个数字，
        并把次数设置为1。由于我们要找的数字出现的次数比其它所有数字出现的次数之和还要多，
        那么要找的数字肯定是最后一次把数字设为1时对应的数字。最后统计次数判断一下即可。
 时间复杂度O(n)，空间复杂度O(1)
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 1
        num = numbers[0]
        for i in numbers[1:]:
            if i == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = i
                    count = 1
        # count num
        count = 0
        for j in numbers:
            if j == num:
                count += 1
        if count > len(numbers)/2:
            return num
        else:
            return 0

# 二刷
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路：利用数组特性，统计与当前字符个数相同的数字, 最后一次将count置1的数一定是出现次数大于一般的数字（众数）
        # Time: O(n), Space: O(1)
        cur = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == cur:
                count +=1
            else:
                count -= 1
            # if change num
            if count == 0:
                cur = nums[i]
                count = 1
        return cur
