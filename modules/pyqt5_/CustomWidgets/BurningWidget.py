# -*- coding: utf-8 -*-
"""
In this example, we create an custom widget.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen


class Communicate(QObject):
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置控件大小和高度
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):

        self.value = value

    # 重写paintEvent方法
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        # 获得控件尺寸
        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))

        # till参数定义了需要绘制的总尺寸
        till = int(((w / 750.0) * self.value))
        # full参数定义了红色区域的绘制起点
        full = int(((w / 750.0) * 700))

        # 黄色或红黄矩形的绘制
        if self.value >= 700:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)
        else:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            # 画刻度线
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            # 使用字体度量来绘制文本
            fw = metrics.width(str(self.num[j]))
            # 画刻度值
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 水平放置一个QSlider滑块
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)  # 初始值
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)

        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()  # 重绘方法


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
