# -*- coding: utf-8 -*-
"""
PyQt5 tutorial

This example shows
how to use QSplitter widget.

problem: 看不清QFrame之间的界限
"""
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        # 创建spliter分隔QFrame 控件
        spliter1 = QSplitter(Qt.Horizontal)
        spliter1.addWidget(topleft)
        spliter1.addWidget(topright)

        spliter2 = QSplitter(Qt.Vertical)
        spliter2.addWidget(spliter1)
        spliter2.addWidget(bottom)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())