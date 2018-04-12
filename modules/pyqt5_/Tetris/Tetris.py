# -*- coding: utf-8 -*-
"""
使用PyQt5编写俄罗斯方块游戏
-------
4 object
- Tetris: 存放游戏
- Board: 编写游戏逻辑
- Tetromino:四方格， 包含所有俄罗斯方块
- Shape: 保存方块信息, 包含方块旋转操作

TODO:
[1] fix some bugs
[2] 理解Board面板中绘制图形的原理
"""
import random
import sys
from PyQt5.QtWidgets import (QMainWindow, QFrame,
                             QDesktopWidget, QApplication)
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor


class Tetromino(object):
    """
    四方格， 包含所有的俄罗斯方块
                                                #
                    #            #           #
                    # #     # #           #
                        #    #               #

                                      #      #
        #         # #            #      #
    # # #      # #        # #      # #
    """
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    """
    保存方块信息
    """
    # 使用元祖保存所有可能的俄罗斯方块坐标值
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )

    def __init__(self):
        # 保存方块的坐标值
        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetromino.NoShape

        self.setShape(Tetromino.NoShape)

    def shape(self):
        """得到方块形状"""
        return self.pieceShape

    def setShape(self, shape):
        """设置指定的方块形状"""
        # 查找相应shape的坐标值
        table = Shape.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        self.pieceShape = shape

    def setRandomShape(self):
        """设置随机的方块形状"""
        self.setShape(random.randint(1, 7))

    def x(self, index):
        """获得相应索引的坐标x的值"""
        return self.coords[index][0]

    def y(self, index):
        """获得相应索引y的值"""
        return self.coords[index][1]

    def setX(self, index, x):
        """设置相应索引的坐标的x值"""
        self.coords[index][0] = x

    def setY(self, index, y):
        """设置相应索引的坐标的y值"""
        self.coords[index][1] = y

    def minX(self):
        """得到4个坐标的最小的x的值"""
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
        return m

    def maxX(self):
        """得到4个坐标的最大的x的值"""
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
        return m

    def minY(self):
        """得到4个坐标的最小的y值"""
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
        return m

    def maxY(self):
        """得到4个坐标的最大的Y值"""
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
        return m

    # 旋转方块，如果不能旋转，返回当前对象的应用，
    # 否则创建一个新的块及其坐标设置为的旋转
    def rotateLeft(self):
        if self.pieceShape == Tetromino.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        # 像左旋转 (x, y) -> (-y, x)
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result

    def rotateRight(self):
        if self.pieceShape == Tetromino.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        # 向右旋转(x, y) -> (y, -x)
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
        return result

class Tetris(QMainWindow):
    """程序主窗口"""
    def __init__(self):
        super(Tetris, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建Board面板类并置于中心
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        # 添加状态栏，并连接状态栏显示消息槽
        self.statusBar = self.statusBar()
        self.tboard.msg2StatusBar[str].connect(self.statusBar.showMessage)

        # 启动游戏
        self.tboard.start()

        # 设置主窗口
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        # 使主窗口居中屏幕
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2.,
                  (screen.height() - size.height()) / 2)

class Board(QFrame):
    """Board面板类实例， 包含应用程序的核心组件"""
    # 创建自定义型号用于发送信息到状态栏
    msg2StatusBar = pyqtSignal(str)

    # 定义块(什么块？)的大小和游戏速度
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        # 初始化一些重要的变量
        super(Board, self).__init__(parent)

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0

        # 一个从0到7的数字列表, 记录多种形状的位置和目前剩余的形状
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

        print("self.contentsRect().width(): ", self.contentsRect().width())
        print("self.contentsRect().height()", self.contentsRect().height())

    # 确定在给定形状块的类型(x和y是什么？坐标是怎么定义的？)
    def shapeAt(self, x, y):
        """determines shape at the board position"""
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        # 计算单一方块像素的宽度
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        # 计算单一方块像素的高度
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """开始游戏"""
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        # 发送消息
        self.msg2StatusBar.emit(str(self.numLinesRemoved))
        # 创建新的方块
        self.newPiece()
        # 开启定时器
        self.timer.start(Board.Speed, self)

    def pause(self):
        """暂停游戏"""
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2StatusBar.emit("paused")
        else:
            self.timer.start(Board.speed, self)
            self.msg2StatusBar.emit(str(self.numLinesRemoved))

        self.update()

    # 重写paintEvent方法
    def paintEvent(self, e):
        """
        1. 绘制所有方块
        2. 绘制下降中的方块
        """
        painter = QPainter(self)
        rect = self.contentsRect()
        print(rect.bottom())
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        # 绘制所有方块
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetromino.NoShape:
                    self.drawSquare(painter,
                                    rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        # 绘制下降中的方块
        if self.curPiece.shape() != Tetromino.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())

    def keyPressEvent(self, event):
        if not self.isStarted or self.curPiece.shape() == Tetromino.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):
        """
        clears shapes from the board.
        :return:
        """
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetromino.NoShape)

    def dropDown(self):
        newY = self.curY
        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -= 1
        self.pieceDropped()

    def oneLineDown(self):
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()

    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetromino.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetromino.NoShape)
            self.update()

    def newPiece(self):
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.curPiece.setShape(Tetromino.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetromino.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True

    def drawSquare(self, painter, x, y, shape):
        """draws a square of a shape.
        it contains 4 lines and a fillRect.
        :param painter: QPainter
        :param x:
        :param y:
        :param shape: a 0-7 number represents the type of tetromino.
        :return:
        """
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tetis = Tetris()
    sys.exit(app.exec_())


