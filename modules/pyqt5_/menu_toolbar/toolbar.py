# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('sun.jpg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.exit)

        # 添加工具栏
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ToolBar')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

