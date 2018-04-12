# -*- coding: utf-8 -*-
"""
PyQt5 tutorial

This example shows a QSlider widget.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 添加一个滑块
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        # 创建了一个QLabel控件并为它设置了一个初始音量图像
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('audio-mute.ico'))  # 只支持ico格式
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('audio-mute.ico'))
        elif value <= 30:
            self.label.setPixmap(QPixmap('audio-low.ico'))
        elif value < 80:
            self.label.setPixmap(QPixmap('audio-mid.ico'))
        else:
            self.label.setPixmap(QPixmap('audio-high.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())