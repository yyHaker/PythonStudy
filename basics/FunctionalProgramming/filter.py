# -*- coding: utf-8 -*-
# 利用filter()滤掉非回数
def is_palindrome(n):
    a=str(n)
    s=a[::-1]
    return int(a)==int(s)
output = filter(is_palindrome,range(1,1000))
print(list(output))

# 小结 : filter()的作用是从一个序列中筛出符合i
# 条件的元素。由于filter()使用了惰性计算，所以只
# 有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素