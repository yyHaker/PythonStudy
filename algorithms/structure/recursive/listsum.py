#!/usr/bin/python
# coding:utf-8

"""使用递归算法求整数列表的和.
列表nums的和是列表的第一个元素和列表其余部分的元素之和的总和.
@author: yyhaker
@contact: 572176750@qq.com
@file: listsum.py
@time: 2019/2/19 10:59
"""
def listSum(nums):
    """
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + listSum(nums[1:])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(listSum(nums))

