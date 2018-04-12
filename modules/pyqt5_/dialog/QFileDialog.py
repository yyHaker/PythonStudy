# -*- coding: utf-8 -*-
"""
The QFileDialog example.
"""
import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)

from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.textedit = QTextEdit()
        self.setCentralWidget(self.textedit)
        self.statusBar()

        openfile = QAction(QIcon('sun.jpg'), 'open', self)
        openfile.setShortcut('Ctrl+0')
        openfile.setStatusTip('Open new file')
        openfile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openfile)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textedit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
