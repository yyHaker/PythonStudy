# -*- coding: utf-8 -*-
"""
In this example, we create a skeleton
of a calculator using a QGridLayout.
"""
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, \
    QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口为网格布局
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['cls', 'bck', '', 'close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        # 设置窗口位置
        self.move(300, 150)
        self.setWindowTitle('calculator')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

