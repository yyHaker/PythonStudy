#!/usr/bin/python
# coding:utf-8

"""顺序查找
@author: yyhaker
@contact: 572176750@qq.com
@file: sequentialSearch.py
@time: 2019/2/20 10:29
"""
def sequentialSearch(alist, item):
    """find if item in alist.
    :param alist:
    :param item:
    :return:
    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
            break
        else:
            pos = pos + 1
    return found

def orderedSequentialSearch(alist, item):
    """
    :param alist:
    :param item:
    :return:
    """
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found
