#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 5.单词拆分.py
@time: 2019/7/23 09:11
"""
"""
leetcode139: 单词拆分
方法：
1.暴力回溯（超时）
2.暴力回溯+记忆搜索
3.BFS+队列（超时）
4.DFS+栈（超时）
5.DP
"""
class Solution1(object):
    # 思路：暴力回溯，时间复杂度O(N^N), 空间复杂度为O(N)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.back(s, wordDict, 0)

    def back(self, s, wordDict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.back(s, wordDict, end):
                return True
        return False


class Solution2(object):
    # 思路：暴力回溯+记忆化搜索，使用记忆数组保存已经求得得结果
    # 时间复杂度为O(N^2), 空间复杂度为O(N)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 维护一个记忆数组，memory[i]表示从第i个字符大最后一字符的字符串是否在字典中
        memory = [None] * len(s)
        return self.back(s, wordDict, 0, memory)

    def back(self, s, wordDict, start, memory):
        if start == len(s):
            return True
        if memory[start] != None:
            return memory[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.back(s, wordDict, end, memory):
                memory[start] = True
                return True
        memory[start] = False
        return False

class Solution3(object):
    # 思路：BFS， 使用队列
    # 时间复杂度为O(N^2), 空间复杂度为O(N)
    # visited数组是为了防止重复扩展
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue = []
        visited = [False] * len(s)
        queue.append(0)
        while queue:
            start = queue.pop(0)
            if not visited[start]:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited[start] = False
        return False


class Solution4(object):
    # DFS， 使用栈
    # 时间复杂度为O(N^2), 空间复杂度为O(N)
    # visited数组是为了防止重复扩展
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        stack = []
        visited = [False] * len(s)
        stack.append(0)
        while stack:
            start = stack.pop(0)
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        stack.append(end)
                        if end == len(s):
                            return True
                visited[start] = False
        return False


class Solution5(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 思路：使用DP，设置一个数组d，d[i]表示到第i个字符（不包括字符i）的字符串是否为字典的一部分，
        # d数组大小为len(s)+1,d[0]=0表示空字符串。将该字符串划分为两部分s(0,i-1) -> s(0,j-1)和s(j, i-1)，
        # 分别判断s(0,j-1)和s(j,i-1)是否为字典的一部分，来决定d[i]的值
        # 时间复杂度为O(N^2),空间复杂度为O(N)
        d = [False] * (len(s) + 1)
        d[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if d[j] and s[j:i] in wordDict:
                    d[i] = True
                    break
        return d[len(s)]



