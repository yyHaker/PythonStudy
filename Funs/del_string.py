# -*- coding: utf-8 -*-
"""
删除一个list中的空字符串
"""
alist = ["asd", "中文", "", "ans", ""]

# method 1
while "" in alist:
    alist.remove("")

print(alist)

# method 2
alist = ["asd", "中文", "", "ans", ""]
for s in alist:
    if s.strip() == "":
        alist.remove(s)
print(alist)