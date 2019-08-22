#!/usr/bin/python
# coding:utf-8

class Solution(object):
    def __init__(self):
        self.score = 0

    def search(self, m):
        directions = [(1, -1), (1, 0), (1, 1)]
        start = [(0, 0), (0, 1), (0, 2)]

        def dfs(x, y, directions, m, cur):
            if x == len(m) - 1:
                if cur > self.score:
                    self.score = cur
            else:
                for d in directions:
                    nx = x + d[0]
                    ny = y + d[1]
                    if 0 <= nx < len(m) and 0 <= ny < 3:
                        cur += m[nx][ny]
                        if m[nx][ny] == 0:
                            cur = -1 * cur
                        dfs(nx, ny, directions, m, cur)
                        cur -= m[nx][ny]
                        if m[nx][ny] == 0:
                            cur = -1 * cur

        for x, y in start:
            cur = m[x][y]
            dfs(x, y, directions, m, cur)

        return self.score

n = int(input())
m = [[0] * 3 for _ in range(n)]
for i in range(n):
    m[i] = [int(e) for e in input().split(" ")]
# n = 6
# m = [
#     [1, 2, 3],
#     [8, 9, 10],
#     [5, 0, 5],
#     [-9, -8, -10],
#     [0, 1, 2],
#     [5, 4, 6]
# ]
solution = Solution()
res = solution.search(m)
print(res)


