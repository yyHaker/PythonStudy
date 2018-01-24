#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted的函数的用法
from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))

print(sorted(students,key=lambda x:x[0]))  # 根据名字排列
print(sorted(students,key=lambda x:x[1],reverse=True))  # 根据成绩排列
print(sorted(students,key=lambda x:x[1],reverse=False))  # 根据成绩排列
