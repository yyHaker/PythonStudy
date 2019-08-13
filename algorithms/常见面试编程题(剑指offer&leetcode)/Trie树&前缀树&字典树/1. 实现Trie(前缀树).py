#!/usr/bin/python
# coding:utf-8
"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 1. 实现Trie(前缀树).py
@time: 2019/8/9 15:09
"""
"""
leetcode208: 实现Trie树
参考：
【1】https://blog.csdn.net/fuxuemingzhu/article/details/79388432
【2】https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode/
"""
class Node(object):
    def __init__(self):
        self.child = {}
        self.is_word = False  # 表示该结点是否是一个单词


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if c not in p.child:
                p.child[c] = Node()
            p = p.child[c]
        p.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for c in word:
            if c not in p.child:
                return False
            p = p.child[c]
        return p.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for c in prefix:
            if c not in p.child:
                return False
            p = p.child[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
