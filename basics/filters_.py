# -*- coding: utf-8 -*-
"""
The usage of filters.
"""
# filter the numbers of a list which is odd
def is_odd(x):
    return x % 2 == 1

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for a in newlist:
    print(a)

# 1 3 5 7 9
