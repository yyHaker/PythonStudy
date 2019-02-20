#!/usr/bin/python
# coding:utf-8

"""实现map
@author: yyhaker
@contact: 572176750@qq.com
@file: map.py
@time: 2019/2/20 16:17
"""
class HashTable(object):
    """
    实现map.
    hash函数：简单的余数方法
    冲突解决技术： 加1 rehash函数的线性探测
    """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):  # 提供索引操作
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def put(self, key, val):
        """增加一个新的键值对，如果键已经存在map中，那么使用新值替换旧值.
        :param key:
        :param val:
        :return:
        """
        # calc hash value
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = val  # replace
            else:
                # hash conflict
                hashvalue = self.rehash(hashvalue, self.size)
                while self.slots[hashvalue] != None and self.slots[hashvalue] != key:
                    hashvalue = self.rehash(hashvalue, self.size)

                if self.slots[hashvalue] == None:
                    self.slots[hashvalue] = key
                    self.data[hashvalue] = val
                else:
                    self.data[hashvalue] = val  # replace

    def get(self, key):
        """给定一个键，返回存储在map中的值或者None.
        :param key:
        :return:
        """
        startslot = self.hashfunction(key, self.size)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True
        return data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (1 + oldhash) % size


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print("slots: ", H.slots)
    print("data: ", H.data)

    # change value
    H[20] = "duck"
    print("after change: ")
    print("slots: ", H.slots)
    print("data: ", H.data)

    print(H[99])


