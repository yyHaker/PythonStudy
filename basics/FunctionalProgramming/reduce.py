# 利用reduce编写prod（）函数接受list求积
from functools import reduce
def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply, L)
print(prod([3, 5, 7, 9]))

# 利用map和reduce实现字符串到浮点数的转换
def str2float(s):
    for x in range(0,len(s)):
        if s[x]=='.':
            break
    s = [y for y in s if y!= '.']
    def fn1(s1):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s1]
    def fn2(x1,x2):
        return x1*10+x2
    return reduce(fn2,list(map(fn1,s)))/(10**(len(s)-x))
print(str2float('12345.6'))