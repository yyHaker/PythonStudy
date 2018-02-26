# -*- coding: utf-8 -*-
"""
This program creates a quit
button. When we press the button,
the application terminates.
"""
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        # 设置按钮默认大小
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建用户界面对象
    ex = Example()
    sys.exit(app.exec_())


