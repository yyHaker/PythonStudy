#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 6.求x的平方根.py
@time: 2019/8/18 11:46
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 思路：二分法, x的平方根一定在[1, x/2 + 1]之间
        if x == 0 or x == 1:
            return x
        i = 0
        j = x / 2 + 1
        while True:
            mid = (i + j) / 2
            if mid * mid > x:
                j = mid
            else:
                if (mid + 1) * (mid + 1) > x:
                    return int(mid)
                i = mid

class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 思路: 牛顿迭代法, x的平方根一定在[1, x/2 + 1]之间
        r = x / 2 + 1
        while r * r > x:
            r = (r + x / r) / 2
        return int(r)


solution = Solution()
x = 9
res = solution.mySqrt(x)
print(res)