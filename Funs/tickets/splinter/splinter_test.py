# coding=utf-8
"""
注意安装chromedriver, 在命令行下运行，检测能否启动Chrome
"""
from splinter.browser import Browser

if __name__ == '__main__':
    b = Browser('chrome')
    b.visit("http://www.baidu.com")
