# -*- coding: utf-8 -*-
"""
In this example, we create a bit more complicated window
layout, using the the QGridLayout manager.
"""
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QTextEdit, QGridLayout,
                             QApplication)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 创建一个网格布局
        grid = QGridLayout()
        # 设置组件之间的差距
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        # 设置布局
        self.setLayout(grid)

        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


