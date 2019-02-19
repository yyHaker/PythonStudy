#!/usr/bin/python
# coding:utf-8

"""使用动态规划解决硬币找零的问题
@author: yyhaker
@contact: 572176750@qq.com
@file: resCoins.py
@time: 2019/2/19 14:41
"""
def resCoin(coinValueList, change):
    """递归方法解决. (效率太低，重复计算)
    :param coinValueList:
    :param change:
    :return:
    """
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + resCoin(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


# 递归方法，去掉重复计算，保存已经计算的结果
def resCoin_(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + resCoin_(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

# 优雅的动态规划算法求解
def dpMakeChange(coinValueList, change, minCoins):
    """维护一个包含每个值最小硬币数量的列表
    :param coinValueList: 一个有效硬币值的列表
    :param change: 找零额
    :param minCoins: 包含每个值的最小硬币数量的列表
    :return:
    """
    for value in range(change+1):
        coinCounts = value
        # coinCounts保存当前值最小硬币数量
        for i in [c for c in coinValueList if c <= value]:
            if 1 + minCoins[value-i] < coinCounts:
                coinCounts = 1 + minCoins[value-i]
        minCoins[value] = coinCounts
    return minCoins[change]


# (带跟踪的动态规划算法)
def dpMakeChange_path(coinValueList, change, minCoins, coinsUsed):
    """维护一个包含每个值最小硬币数量的列表
    :param coinValueList: 一个有效硬币值的列表
    :param change: 找零额
    :param minCoins: 包含每个值的最小硬币数量的列表
    :return:
    """
    for value in range(change+1):
        coinCounts = value
        newCoin = 1  # 保存最后一个硬币值
        # coinCounts保存当前值最小硬币数量
        for i in [c for c in coinValueList if c <= value]:
            if 1 + minCoins[value-i] < coinCounts:
                coinCounts = 1 + minCoins[value-i]
                newCoin = i
        minCoins[value] = coinCounts
        coinsUsed[value] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


if __name__ == "__main__":
    print(resCoin_([1, 5, 10, 25], 63, [0]*64))
    print(dpMakeChange([1, 5, 10, 25], 63, [0]*64))

    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)

    print("Making change for", amnt, "requires")
    print(dpMakeChange_path(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are:")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)
