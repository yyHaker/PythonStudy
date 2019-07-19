#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.顺时针打印矩阵.py
@time: 2019/7/16 22:16
"""
"""
剑指offer：顺时针打印矩阵
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 解题思路：顺时针打印就是按圈数循环打印，一圈包含两行或者两列，
        # 在打印的时候会出现某一圈中只包含一行，要判断从左向右打印和从右
        # 向左打印的时候是否会出现重复打印，同样只包含一列时，要判断从上
        # 向下打印和从下向上打印的时候是否会出现重复打印的情况
        lx = 0
        ly = 0
        rx = len(matrix)-1
        ry = len(matrix[0])-1
        res = []
        while lx <= rx and ly <= ry:
            # right
            j=ly
            while j<= ry:
                res.append(matrix[lx][j])
                j += 1
            # down
            i=lx
            while i+1 <= rx:
                i += 1
                res.append(matrix[i][ry])
            # left
            j=ry
            if lx < rx:
                while j-1 >= ly:
                    j = j-1
                    res.append(matrix[rx][j])
            # up
            i=rx
            if ly < ry:
                while i-1 > lx:
                    i = i-1
                    res.append(matrix[i][ly])
            # 更新左上角和右下角
            lx += 1
            ly += 1
            rx -= 1
            ry -= 1
        return res
