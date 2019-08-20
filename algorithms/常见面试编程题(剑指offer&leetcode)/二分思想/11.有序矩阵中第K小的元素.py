#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 11.有序矩阵中第K小的元素.py
@time: 2019/8/18 22:37
"""
"""
leetcode378: 寻找有序数组中第K小的元素
思路：
【1】建立最小堆
【2】二分查找
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 思路：维护一个最小堆，首先将矩阵的左上角元素加入到堆，然后执行k次循环，弹出堆顶元素，记录其下标为i，j
        # 添加改元素的右边和下边元素入堆，注意仅当j=0的时候才添加下边的元素
        # 时间复杂度为O(klogk)
        import heapq
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

class Solution2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 思路：二分查找，将查找上下限设为矩阵的右下角与左上角元素， 查找过程中对中值在矩阵每一行可插入的位置进行累加，记该值为loc，
        # 根据loc与k的大小关系调整上下限
        # 时间复杂度为o(nlogn), 注意最外层复杂度为O(max_val - min_val) = O(1)
        import bisect
        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            mid = (l + r) >> 1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if k <= loc:
                r = mid -1
            else:
                l = mid + 1
        return l



