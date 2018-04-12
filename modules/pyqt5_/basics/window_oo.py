# -*- coding: utf-8 -*-
"""
This example shows an icon in the titlebar of the window.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        # 绘制界面
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('sun.jpg'))

        self.show()

if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
