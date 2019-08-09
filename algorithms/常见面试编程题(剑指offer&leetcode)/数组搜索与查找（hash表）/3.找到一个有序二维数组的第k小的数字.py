#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.找到一个有序二维数组的第k小的数字.py
@time: 2019/7/14 20:58
"""
"""
leetcode378: 找到一个有序二维数组的第k小的数字
思路：使用最小堆，每次把最小的值（可能是右方，也可能是上方）放进堆，进行k次即可;时间复杂度为O(klogk)
        每次弹出当前最小堆中元素后，将该元素的右边元素添加到堆， 如果是第一列，把下边的元素也添加到堆
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        m, n = len(matrix), len(matrix[0])
        min_heap = [(matrix[0][0], 0, 0)]
        for _ in range(k):
            res, i, j = heapq.heappop(min_heap)
            if j == 0 and i + 1 < m:
                heapq.heappush(min_heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(min_heap, (matrix[i][j + 1], i, j + 1))
        return res

