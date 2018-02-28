# -*- coding: utf-8 -*-
"""
A simple drag and drop example.
"""
import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)

# 使button接受拖放操作
class Button(QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

        # 支持drop事件
        self.setAcceptDrops(True)

    # 重新实现dragEnterEvent方法， 并设置可接受的数据类型
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # 重新实现dropEvent方法， drop事件发生时改变按钮的文字
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        # 设置控件支持drag(拖)操作
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("button", self)
        button.move(190, 65)

        self.setWindowTitle("Simple drag & drop")
        self.setGeometry(300, 300, 300, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
