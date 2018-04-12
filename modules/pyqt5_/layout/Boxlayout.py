# -*- coding: utf-8 -*-
"""
In this example, we position two push buttons
in the bottom-right corner of the window.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("ok")
        cancelButton = QPushButton("Cancel")

        # 创建一个水平布局和添加一个伸展因子和两个按钮
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建一个垂直布局，并添加伸展因子，让水平布局显示在窗口底部
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置窗口的布局界面
        self.setLayout(vbox)

        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('BoxLayout')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



