#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.单词搜索.py
@time: 2019/8/9 11:28
"""
"""
leetcode12: 单词搜索
思路：回溯法
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 思路：回溯法，在二维网格中搜索，从每一个格子开始，找到一条路径，路径即为word单词，
        # 找到即返回True，当找完所有的路径，找不到就返回false
        if len(board) == 0:
            return False
        # 标记矩阵
        marked = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # 对每一个格子从头开始搜索
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(0, i, j, word, marked, board):
                    return True
        return False

    def dfs(self, idx, x, y, word, marked, board):
        # 递归终止条件
        if idx == len(word) - 1:
            return board[x][y] == word[idx]

        if board[x][y] == word[idx]:
            marked[x][y] = True
            # 四个方向(上下左右)
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newx = x + d[0]
                newy = y + d[1]
                if 0 <= newx <= len(board) - 1 and 0 <= newy <= len(board[0]) - 1 and not marked[newx][
                    newy] and self.dfs(idx + 1, newx, newy, word, marked, board):
                    return True
            marked[x][y] = False
        return False
