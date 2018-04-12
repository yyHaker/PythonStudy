# -*- coding: utf-8 -*-
"""
PyQt5 tutorial

This example shows a QCalendarWidget widget.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication)
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 添加日历控件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        # 部件选择一个日期,点击[QDate]发出信号。我们将这个信号连接到用户定义的showDate()方法
        cal.clicked[QDate].connect(self.showDate)

        # 添加标签
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())