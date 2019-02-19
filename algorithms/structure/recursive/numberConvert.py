#!/usr/bin/python
# coding:utf-8

"""使用递归解决进制转换问题.
@author: yyhaker
@contact: 572176750@qq.com
@file: numberConvert.py
@time: 2019/2/19 11:14
"""
def divideByBase(num, base):
    convString = "0123456789ABCDEF"
    if num < base:
        return convString[num]
    else:
        return divideByBase(num // base, base) + convString[num % base]


if __name__ == "__main__":
    print(divideByBase(10, 2))
