#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 日期工具函数.py
@time: 2019/7/24 19:45
"""
import datetime
import time
import sys
import calendar


def get_day(line):
    year, month, week, day = [int(k) for k in line.split(' ')]
    try:
        cal = calendar.monthcalendar(year, month)
        date = cal[week - 1][day - 1]
        res = "%d-%d-%d" % (year, month, date)
        time.strptime(res, "%Y-%m-%d")
        return res
    except:
        return 0


line = sys.stdin.readline().strip()
date = get_day(line)
print(date)
