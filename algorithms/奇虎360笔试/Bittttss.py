#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: Bittttss.py
@time: 2019/8/8 15:14

题目：链接：https://www.nowcoder.com/questionTerminal/a19f8670d25d444ab9e2f5601e1143ce
来源：牛客网

现在有q个询问，每次询问想问你在[l,r]区间内，k进制表示中，k-1的数量最多的数是哪个数。
比如当k=2时，9的二进制就是1001，那么他就有2个1.
输入：
第一行一个q，表示有q组询问。
接下来q行，每行三个整数k,l,r,分别表示进制数,查询的数字,以及查询的范围。
满足1<=q<=100000,2<=k<=16,1<=l<=r<=10^16
输出：
对于每组询问，输出答案。如果有多个答案，请输出最小的。

思路：
首先将start（我用start和end分别表示左右的边界）转换成k进制。将转换后的每一位都存在列表
中。然后从低位往高位依次将每一位变成（k-1）。在变换之前，
首先看看能不能变，能变则变，不能变表示超过了end，这个时候直接跳出即可。
"""
# 思路：求数字的相应K进制的表示，统计k-1的个数，保存最多的结果
"""
疑惑：算法的时间复杂度为O(n), 只是过了86.67%
"""
def get_hex(num, k):
    # 得到一个数字的k进制表示
    res = []
    while num != 0:
        t = num % k
        res.append(t)
        num = num // k
    return res

def get_num(k, l, r):
    rhex = get_hex(r, k)
    res = get_hex(l, k)
    res = res + [0] * (len(rhex)-len(res))
    cur = l
    for i in range(len(res)):
        margin = (k - 1 - int(res[i])) * pow(k, i)
        if cur + margin <= r:
            cur = cur + margin
            res[i] = k - 1
        else:
            break
    return cur

q = int(input())
for _ in range(q):
    params = [int(e) for e in input().split(" ")]
    k, l, r = params[0], params[1], params[2]
    out = get_num(k, l, r)
    print(out)

