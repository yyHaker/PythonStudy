#!/usr/bin/python
# coding:utf-8

"""python装饰器decorator
@author: yyhaker
@contact: 572176750@qq.com
@file: decorator.py
@time: 2019/3/13 13:51
参考链接：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
"""
import functools
import time
from inspect import isfunction

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print("%s executed in %s ms" % (func.__name__, end - start))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 带参数的decorator(兼容log、log('')、log('str'))
def log(arg=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s' % arg)
            return func(*args, **kwargs)
        return wrapper
    if type(arg) is str:
        return decorator
    elif isfunction(arg):
        return arg

@log('excute')
def f1(x, y):
    print(max(x, y))

@log()
def f2(x, y):
    print(max(x, y))

@log
def f3(x, y):
    print(max(x, y))

f1(4, 5)
# f2(6, 7)
# f3(8, 9)


ss = [['a', 'b'], ['c'], ['d'], [3], [6.6], ["我的", "你的"]]
print(sum(ss, ['nini']))






