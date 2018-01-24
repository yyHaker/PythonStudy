from collections import Iterable
# 迭代key
d={'a':1, 'b' :2, 'c':3}
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 迭代key和value
for k,v in d.items():
    print(k,v)

# 字符串也可迭代对象
for ch in 'ABC':
    print(ch)

# 判断是否可迭代
print(isinstance('abc', Iterable))
print(isinstance([123], Iterable))
print(isinstance(123, Iterable))

# 同时迭代索引和本身   enumerate函数将list变成元素索引对
for i,value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x,y in [(1,2),(3,4),(5,6)]:
    print(x, y)


# 小结:任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。