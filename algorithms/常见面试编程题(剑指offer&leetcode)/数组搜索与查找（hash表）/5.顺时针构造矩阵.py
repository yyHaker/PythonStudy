#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.顺时针构造矩阵.py
@time: 2019/7/16 17:02
"""
"""
顺时针构造矩阵，例如给一个5，你需要输出:
[[1, 2, 3, 4, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9]]
思路： 根据顺时针的方向打印数组，记录个数和左右边界left和right，每一圈之后，
左右边界均缩小，依次打印输出即可
"""
def get_matrix(n):
    # 创建一个二维数组
    res = [[0]*n for _ in range(n)]
    i, j = 0, -1
    count = 0
    left = 0
    right = n-1
    while count <= n*n and left <= right:
        # 右
        while j+1 <= right:
            j += 1
            count += 1
            res[i][j] = count
        # 下
        while i+1 <= right:
            i += 1
            count += 1
            res[i][j] = count
        # 左
        while j-1 >= left:
            j -= 1
            count += 1
            res[i][j] = count
        # 上
        while i-1 > left:
            i -= 1
            count += 1
            res[i][j] = count
        # 调整边界
        left += 1
        right -= 1
    return res

res = get_matrix(5)
print(res)


