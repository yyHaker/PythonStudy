#!/usr/bin/python
# coding:utf-8

"""使用两种方法求解sqrt(n) , 精确度在10^(-5)
@author: yyhaker
@contact: 572176750@qq.com
@file: sqrtn.py
@time: 2019/3/20 09:16
"""
def division(n, prec=0.00001):
    """
    使用二分法求得n的平方根.
    --------
    n的平方根一定在区间[1, n/2 + 1], 二分搜索查找即可.
    :param n:
    :param prec:
    :return:
    """
    left = 1
    right = n/2 + 1
    while left < right:
        mid = (left + right) / 2
        # print(mid)
        if abs(mid * mid - n) < prec:
            return mid
        else:
            if mid * mid < n:
                left = mid
            else:
                right = mid

print("division method: ")
sqrtn = division(5)
print("sqrt(n): ", sqrtn, " , (sqrtn^2): ", sqrtn * sqrtn)

def newton(n, prec=0.00001):
    """
    使用牛顿法求解n的平方根.
    :param n:
    :param prec:
    :return:
    """
    m = 1.0
    while abs(m * m - n) > prec:
        m = (m + n/m)/2
    return m

print("newton method: ")
sqrtn = newton(5)
print("sqrt(n): ", sqrtn, " , (sqrtn^2): ", sqrtn * sqrtn)


