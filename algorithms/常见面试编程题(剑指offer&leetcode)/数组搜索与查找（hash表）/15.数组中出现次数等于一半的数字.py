#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 15.数组中出现次数等于一半的数字.py
@time: 2019/8/18 09:38
"""
"""
剑指offer的变种题目
思路：如果按照"数组中出现的次数大于一半的数字"的做法，数组中出现次数等于一半的数字只会出现candidate和nums[n-1]，
所以这里更改一下原先算法，只是遍历前n-1个数，并统计和nums[n-1]相等的数字的个数，判断一下哪个是出现次数等于一半的数字。
时间复杂度为O(n)，空间复杂度为O(1)
"""
class Solution(object):
    def equalHalfNum(self, nums):
        last_count = 1
        last = nums[len(nums)-1]
        count = 0
        candidate = 0
        for i in range(len(nums)-1):
            if nums[i] == last:
                last_count += 1

            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1

        if last_count == len(nums) / 2:
            return last
        else:
            return candidate


class Solution2(object):
    # 不确定是否正确
    def equalHalfNum(self, nums):
        count = 0
        candidate = 0
        for i in range(len(nums)-1):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate


nums = [1, 2, 1, 1, 3, 5]
nums2 = [0, 1, 2, 1]
nums3 = [1, 2, 3, 1, 1, 5]
solution = Solution()
res = solution.equalHalfNum(nums3)
print(res)

