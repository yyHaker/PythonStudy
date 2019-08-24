#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 2.二进制中1的个数.py
@time: 2019/7/18 10:23
"""
"""
剑指offer：求一个整数的二进制表示中位1的个数(考虑负数)
leetcode191：求一个无符号整数中位1的个数
思路：
如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，原来在1
后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，它后面的两位0变成了1，
而前面的1保持不变，因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。这个时候如果我们
再把原来的整数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000.也就是
说，把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少
次这样的操作。
但是负数使用补码表示的，对于负数，最高位为1，而负数在计算机是以补码存在的，往右移，符号位不变，符号位1往右移，
最终可能会出现全1的情况，导致死循环。与0xffffffff相与，就可以消除负数的影响

参考：
【1】https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/ComputerCode.html（源码、反码、补码）
"""
class Solution:
    def hammingWeight(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n-1)
            count += 1
        return count


class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 若n为无符号整数
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

n = -3
solution = Solution()
res = solution.hammingWeight(n)
print(res)
