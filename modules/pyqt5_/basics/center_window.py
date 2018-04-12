# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle("Center Window")
        self.show()

    # 控制窗口显示在屏幕中心的的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕的中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 将窗口显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())    # 怎么理解?

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
