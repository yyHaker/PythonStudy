# -*- coding: utf-8 -*-
"""
In this example, we determine the event sender
object.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, QObject

# 自定义信号
class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # 将信号连接到QMainWindow的close槽
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    # 重写鼠标点击方法
    def mousePressEvent(self, e):
        self.c.closeApp.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
