#!/usr/bin/env python3       #让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-         #.py文件本身使用标准UTF-8编码

' a test module'                   # 一个字符串，表示模块的文档注释

__author__ = 'Michael Liao'    # 使用__author__变量把作者写进去

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()