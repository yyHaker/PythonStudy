# -*- coding: utf-8 -*-
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[ch.lower() for ch in L1 if isinstance(ch,str)]
print(L2)