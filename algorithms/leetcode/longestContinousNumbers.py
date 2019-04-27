#!/usr/bin/python
# coding:utf-8

"""找出数组中最长连续数字序列.
---
一个数组，找出其中出现过的最长的连续数，如数组为：[100, 1, 200, 3, 2, 4, 8, 9]，
则最长的连续数为4.
解法：
    (1) 直接排序，然后找最长连续数字，时间复杂度O(nlogn)
    (2) 使用hashmap，键保存该数字， 值保存所在连续数字的长度,  遍历的过程中维护最长的连续数字首尾位保存长度值。时间复杂度O(n)
@author: yyhaker
@contact: 572176750@qq.com
@file: longestContinousNumbers.py
@time: 2019/2/23 21:34
"""
def longestConsecutive(nums):
    """
    :param nums: num list.
    :return:
    """
    hashmap = {}
    longest = 0
    for n in nums:
        if n in hashmap.keys():
            continue
        else:
            hashmap[n] = 1
            if (n-1) in hashmap.keys():
                hashmap[n] = hashmap[n-1] + hashmap[n]
                hashmap[n-1-hashmap[n-1]+1] = hashmap[n]
                longest = max(longest, hashmap[n])
            if (n+1) in hashmap.keys():
                hashmap[n] = hashmap[n+1] + hashmap[n]
                hashmap[n+1+hashmap[n+1]-1] = hashmap[n]
                longest = max(longest, hashmap[n])
    # print(hashmap)
    return longest

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2, 7, 5]
    print(longestConsecutive(nums))

