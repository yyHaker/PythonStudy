# -*- coding: utf-8 -*-
"""
This program creates a statusbar.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 使用QMainWindow创建状态栏的小窗口
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个主要的应用程序窗口
    ex = Example()
    sys.exit(app.exec_())
