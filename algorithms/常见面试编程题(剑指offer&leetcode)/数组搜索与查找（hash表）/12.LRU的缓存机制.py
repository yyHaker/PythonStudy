#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 12.LRU的缓存机制.py
@time: 2019/7/19 14:44
"""
"""
leetcode146: 实现LRU的缓存机制，使得能够以O(1)的时间复杂度执行get(key)和put(key,value)操作
思路：使用双向链表+哈希表来实现LRU缓存机制

"""
class LinkedNode(object):
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = 0
        self.next = 0


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = LinkedNode(), LinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """
        Add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        remove an existing node from the linked list.
        """
        prev = node.prev
        back = node.next

        prev.next = back
        back.prev = prev

    def _move_to_head(self, node):
        """
        move certain node to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        pop the current tail.
        """
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key, None)

        if not node:
            newNode = LinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            # update the value
            node.value = value
            self._move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
