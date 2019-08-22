#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 4.N皇后II.py
@time: 2019/8/5 14:37
"""
"""
leetcode52: N皇后II
思路：回溯法
"""
class Solution:
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n: int) -> int:
        # 思路：回溯法
        # 表示第i行第board[j]的位置一个皇后
        board = [-1 for i in range(n)]
        self.dfs(0, n, board)
        return self.count

    def dfs(self, i, n, board):
        if i == n:
            self.count += 1
            return
        else:
            for j in range(n):
                if self.is_valid(i, j, board):
                    board[i] = j
                    self.dfs(i + 1, n, board)

    def is_valid(self, row, col, board):
        # 保证新添加的(row, col)与之前的皇后不同行不同列
        for i in range(row):
            if col == board[i] or abs(col - board[i]) == abs(row - i):
                return False
        return True
