# -*- coding: utf-8 -*-
"""
This program creates a menubar. The menubar has
one menu with an exit action.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建退出事件
        exitAcition = QAction(QIcon('sun.jpg'), '&Exit', self)
        exitAcition.setShortcut('Ctrl+Q')
        exitAcition.setStatusTip('Exit application')
        exitAcition.triggered.connect(qApp.quit)

        # 添加一个状态栏
        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加一个菜单
        filemenu = menubar.addMenu('&File')
        # 给菜单添加事件
        filemenu.addAction(exitAcition)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
