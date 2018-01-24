# -*- coding: utf-8 -*-
#caculate the quadratic
import math

def quadratic(a,b,c):
    #if not isinstance(a,(int,float)):
    #   raise TypeError('bad operand type')
    num = b*b-4*a*c
    if num < 0:
        print('no result')
        return
    else:
        return (-b+math.sqrt(num))/(2*a), (-b-math.sqrt(num))/(2*a)
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
