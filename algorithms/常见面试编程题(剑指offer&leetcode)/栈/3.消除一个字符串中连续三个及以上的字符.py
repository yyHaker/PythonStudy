#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 消消乐.py
@time: 2019/8/22 09:20
"""
"""
红红黄黄绿绿绿绿黄蓝 ->消一次变成 红红蓝 （三个以上的干掉）这个比较简单，给了O(n)算法
"""
def kill(strs):
    # 思路：双指针, 时间复杂度为O(n^2), 空间复杂度为O(1)
    if len(strs) <= 2:
        return strs
    l, r = 0, 0
    while l < len(strs):
        r = l
        while r + 1 < len(strs) and strs[r+1] == strs[r]:
            r = r + 1
        # del str
        if r-l+1 >= 3:
            strs = strs[0: l] + strs[r+1:]
            l = 0
        else:
            l = r + 1
    return strs

def delrepeat(strs):
    # 思路：栈+指针， 遍历字符串的过程中，维护当前字符cur和count(次数)，
    # 若能消除则直接消除，若不能消除则将cur和次数count压栈
    # 时间复杂度为O(n), 空间复杂度为O(n)
    if len(strs) <= 2:
        return strs
    stack = []
    r = 0
    while r < len(strs):
        cur = strs[r]
        count = 1
        while r+1 < len(strs) and strs[r+1] == strs[r]:
            r = r + 1
            count += 1
        # 判断是否需要消除
        if stack and stack[-1][0] == cur:
            t = stack.pop()
            t = t[0], count + t[1]
            if t[1] >= 3:
                r = r + 1
            else:
                stack.append(t)
                r = r + 1
        else:
            if count >= 3:
                r = r + 1
            else:
                stack.append((cur, count))
                r = r + 1

    return "".join(map(lambda x: x[0]*x[1], stack))

strs1 = "红红黄黄绿绿绿绿黄蓝"
strs2 = "红红蓝蓝黄黄绿绿绿绿黄蓝红"
strs3 = "红红蓝蓝黄黄绿绿绿绿黄蓝"
res = delrepeat(strs1)
print(res)


