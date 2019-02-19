#!/usr/bin/python
# coding:utf-8

"""使用递归解决汉诺塔问题
@author: yyhaker
@contact: 572176750@qq.com
@file: towers.py
@time: 2019/2/19 13:40
"""
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, withPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


if __name__ == "__main__":
    moveTower(6, 0, 1, 2)
