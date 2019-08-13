#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 3.N.py
@time: 2019/8/5 14:22
"""
"""
leetcode51：N皇后问题
思路：回溯法
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 思路：回溯法， 一行一行的放
        res = []
        # 表示在第i行第board[i]列放置一个皇后
        board = [-1 for i in range(n)]
        matrix = []
        self.dfs(0, n, board, matrix, res)
        return res

    def dfs(self, i, n, board, matrix, res):
        if i == n:
            res.append(matrix)
            return
        else:
            for j in range(n):
                if self.is_valid(i, j, board):
                    board[i] = j
                    s = "." * n
                    self.dfs(i + 1, n, board, matrix + [s[:j] + "Q" + s[j + 1:]], res)

    def is_valid(self, row, col, board):
        # 保证新放置的位置(row, col)满足要求
        # 不同行、不同列、不同斜线
        for i in range(0, row):
            if col == board[i] or abs(col - board[i]) == abs(row - i):
                return False
        return True

