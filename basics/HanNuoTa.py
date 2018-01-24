#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘
# 子从A借助B移动到C的方法
def move( n , a , b , c ):
    if n==0 :
        return
    move(n-1,a,c,b)
    print('%s --> %s' % (a , c))
    move(n-1,b,a,c)

move(3,'A','B','C')
#move(6,'A','B',"C")