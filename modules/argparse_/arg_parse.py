# arg_parse.py
# coding:utf-8
"""
learn to use python argparse module
"""
import argparse

"""
下面是一个脚本，如果不指定--sum选项，则找出输入参数中的最大值，否则求和。
"""

# 申明一个用于将命令行字符串解析为Python对象的对象
parser = argparse.ArgumentParser(description='Process some integers.')
# Adding argument actions
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                      help='sum the integers (default: find the max)')
# parsing command line argument
args = parser.parse_args()
# Accumulate the result of applying the operator to all elements
print(args.accumulate(args.integers))
