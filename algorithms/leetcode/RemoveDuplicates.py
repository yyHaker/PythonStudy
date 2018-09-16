# -*- coding: utf-8 -*-
"""
remove duplicates.
思路： 从左到右遍历，找出第p大的数放在第p个位置
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 从左到右遍历，找出第p大的数放在第p个位置
        if len(nums) == 0:
            return 0
        p = 1
        for n in nums[1: ]:
            if nums[p-1] < n:
                nums[p] = n
                p = p + 1
        return p

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    len = solution.removeDuplicates(nums)
    print(len)
