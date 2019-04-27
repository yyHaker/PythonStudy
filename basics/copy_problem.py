#!/usr/bin/python
# coding:utf-8

"""python深拷贝和浅拷贝
@author: yyhaker
@contact: 572176750@qq.com
@file: copy_problem.py
@time: 2019/3/12 20:53
参考链接: http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
"""
import copy

a = {1: [1, 2, 3]}
b = a    # 赋值引用
print("b = a: 赋值引用，a 和 b 都指向同一个对象:")
print("a: ", a, "    b:", b)

print("c = a.copy(): 浅拷贝, a 和 c 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）")
c = a.copy()  # 浅拷贝
print("a: ", a, "   c: ", c)

print("执行a[1].append(4)")
a[1].append(4)
print("a: ", a, "   c: ", c)

print("执行a[1] = [2, 3, 4]")
a[1] = [2, 3, 4]
print("a: ", a, "   c: ", c)

print("执行a[1].append(4)")
a[1].append(4)
print("a: ", a, "   c: ", c)

print("d = copy.deepcopy(a),  a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的: ")
d = copy.deepcopy(a)
print("a: ", a, "  d: ", d)

print("执行a[1].append(4)")
a[1].append(4)
print("a: ", a, "   c: ", c)

print("执行a[1] = [2, 3, 4]")
a[1] = [2, 3, 4]
print("a: ", a, "   c: ", c)

print("执行a[1].append(4)")
a[1].append(4)
print("a: ", a, "   c: ", c)


"""
若a是一个值，浅拷贝和深拷贝没有区别。
"""
print("a是一个值的情况")
a = [2, 3, 4]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(3)
print("a: ", a, " b: ", b, " c:", c, "d: ", d)

print("-"*100)
"""
总结： 
直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
"""
print("-"*100)
# 再看一个例子：
print("last example: ")
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)








