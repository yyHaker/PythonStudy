#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 10.矩阵置零.py
@time: 2019/7/18 22:35
"""
"""
leetcode73: 矩阵置零
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 思路：遍历整个矩阵，如果 cell[i][j] == 0 就将第 i 行和第 j 列的第一个元素标记。
        # 第一行和第一列的标记是相同的，都是 cell[0][0]，所以需要一个额外的变量告知第一列是否被标记，同时用 cell[0][0] 继续表示第一行的标记。
        # 然后，从第二行第二列的元素开始遍历，如果第 r 行或者第 c 列被标记了，那么就将 cell[r][c] 设为 0。这里第一行和第一列的作用就相当于方法一             # 中的 row_set 和 column_set 。
        # 然后我们检查是否 cell[0][0] == 0 ，如果是则赋值第一行的元素为零。
        # 然后检查第一列是否被标记，如果是则赋值第一列的元素为零。
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 从第二行第二列开始遍历
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 判断第一行是否需要设置为0
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        # 判断第一列是否需要设置为0
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
