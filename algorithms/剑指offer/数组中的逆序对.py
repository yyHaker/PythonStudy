#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 数组中的逆序对.py
@time: 2019/7/4 21:09
"""

"""
思想：归并排序的思想（本质上是分治思想）
"""
class Solution:
    def InversePairs(self, data):
        # write code here
        res = self.mergeCount(data) % 1000000007
        return res

    def mergeCount(self, array):
        # 使用归并思想求逆序对的个数
        if len(array) <= 1:
            return 0
        if len(array) == 2:
            if array[0] < array[1]:
                return 0
            else:
                array[0], array[1] = array[1], array[0]
                return 1
        # 分
        mid = (0 + len(array) - 1) // 2
        left = array[0:mid + 1]
        right = array[mid + 1:]
        count = self.mergeCount(left) + self.mergeCount(right)

        # 合
        i = 0
        j = 0
        k = 0  # 归并后的index
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
                count += mid - i + 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return count

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    solution = Solution()
    res = solution.InversePairs(data)
    print(res)