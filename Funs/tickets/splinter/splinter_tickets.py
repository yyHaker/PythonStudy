# -*- coding: utf-8 -*-
"""
在命令行下运行 python splinter_tickets.py即可打开浏览器运行
"""
from splinter.browser import Browser
import time

b = Browser(driver_name="chrome")

url = "https://kyfw.12306.cn/otn/leftTicket/init"
b.visit(url)
input("请直接在页面输入目的地信息和出发时间，点击查询后，按任意键继续: ")
# 添加相应的cookies，在浏览自重查找得到
b.cookies.add({"_jc_save_fromDate": "2018-02-09"})
b.cookies.add({"_jc_save_fromStation": "%u6DF1%u5733%2CSZQ	"})
b.cookies.add({"_jc_save_toStation": "%u6B66%u6C49%2CWHN	"})
b.reload()
while b.is_element_not_present_by_text(u"预订"):
    b.find_by_text(u"查询").click()
    time.sleep(3)
b.find_by_text(u"预订")[0].click()

