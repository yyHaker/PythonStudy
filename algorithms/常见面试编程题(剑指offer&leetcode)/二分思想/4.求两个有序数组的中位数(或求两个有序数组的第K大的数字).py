#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.求两个有序数组的中位数(或求两个有序数组的第K大的数字).py
@time: 2019/7/18 10:32
"""
"""
leetcode4: 求两个有序数组的中位数？（求两个有序数组的第K大的数）
思路：二分，时间复杂度为O(log(m+n))
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 基本思路还是二分法
        # find the k-th number of nums1 and nums2, O(log(n+m))
        def findkth(A, B, k):
            lena = len(A)
            lenb = len(B)
            if lena > lenb:
                return findkth(B, A, k)
            # special case
            if lena == 0:
                return B[k - 1]
            if k == 1:
                return min(A[0], B[0])
            pa = min(k // 2, lena)
            pb = k - pa
            if A[pa - 1] == B[pb - 1]:
                return A[pa - 1]
            elif A[pa - 1] < B[pb - 1]:
                return findkth(A[pa:], B, k - pa)
            else:
                return findkth(A, B[pb:], k - pb)

        # find mid
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (findkth(nums1, nums2, length // 2) + findkth(nums1, nums2, length // 2 + 1)) / 2.0
        else:
            return findkth(nums1, nums2, length // 2 + 1) * 1.0


# （二刷）
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 思路：二分法，先求两个有序数组的第K大的数
        length = len(nums1) + len(nums2)
        k = length // 2
        if length % 2 == 1:
            return self.findkth(nums1, nums2, k + 1)
        else:
            return (self.findkth(nums1, nums2, k) + self.findkth(nums1, nums2, k + 1)) / 2.0

    def findkth(self, A, B, k):
        # find kth max value of A and B
        lena = len(A)
        lenb = len(B)
        if lena > lenb:
            return self.findkth(B, A, k)
        if lena == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k // 2, lena)
        pb = k - pa
        if A[pa - 1] == B[pb - 1]:
            return A[pa - 1]
        elif A[pa - 1] > B[pb - 1]:
            return self.findkth(A, B[pb:], k - pb)
        else:
            return self.findkth(A[pa:], B, k - pa)


