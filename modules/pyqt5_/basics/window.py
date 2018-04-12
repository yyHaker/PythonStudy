# -*- coding: utf-8 -*-
"""
In this example, we create a simple window in PyQt5.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 用户界面对象的基类
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('A simple window')
    w.show()

    # 消息循环结束之后返回0，接着调用sys.exit(0)退出程序
    sys.exit(app.exec_())
