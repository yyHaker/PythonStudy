#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.添加与搜索单词-数据结构设计.py
@time: 2019/8/9 15:55
"""
"""
leetcode211: 添加与搜索单词-数据结构设计
思路：Trie树&前缀树
"""
class Node(object):
    def __init__(self):
        self.child = {}
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        p = self.root
        for c in word:
            if c not in p.child:
                p.child[c] = Node()
            p = p.child[c]
        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        # 回溯法寻找
        if word == "":
            return node.is_word
        if word[0] == ".":
            for k, v in node.child.items():
                if self.dfs(v, word[1:]):
                    return True
        elif word[0] in node.child:
            return self.dfs(node.child[word[0]], word[1:])
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
