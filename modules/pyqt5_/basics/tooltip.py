# -*- coding: utf-8 -*-
"""
This example shows a tooltip on a window and a button.
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
from PyQt5.QtGui import QIcon, QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        # 绘制界面
        self.initUI()

    def initUI(self):
        # 设置工具显示字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个提示
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并设置一个ToolTip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 设置默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("ToolTips")
        self.setWindowIcon(QIcon('sun.jpg'))

        self.show()

if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建用户界面对象
    ex = Example()
    sys.exit(app.exec_())