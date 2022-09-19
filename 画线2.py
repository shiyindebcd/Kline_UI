



from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *





class PaintBoard(QWidget):

    def __init__(self, parent=None):

        super(PaintBoard, self).__init__(parent)

        self.initData()

        self.initView()



    def initData(self):

        self.size = QSize(600, 900)

        self.board = QPixmap(self.size)

        self.board.fill(Qt.white)  # 画板填充为白色

        self.IsEmpty = True  # 初始默认为空画板

        self.lastPoint = QPoint(0, 0)

        self.endPoint = QPoint(0, 0)

        # 辅助画布

        self.tempBoard = QPixmap()

        self.isDrawing = False  # 标志是否正在绘图



    def initView(self):

        pass



    def paintEvent(self, event):

        painter = QPainter(self)

        x = self.lastPoint.x()

        y = self.lastPoint.y()

        w = self.endPoint.x() - x

        h = self.endPoint.y() - y

        if self.isDrawing:

            self.tempBoard = self.board

            pen = QPainter(self.tempBoard)

            pen.drawRect(x, y, w, h)

            painter.drawPixmap(0, 0, self.tempBoard)

        else:

            pen = QPainter(self.board)

            pen.drawRect(x, y, w, h)

            painter.drawPixmap(0, 0, self.board)



    def mousePressEvent(self, event):

        # 按下鼠标左键

        if event.button() == Qt.LeftButton:

            self.lastPoint = event.pos()

            self.endPoint = self.lastPoint

            self.isDrawing = True



    def mouseReleaseEvent(self, event):

        # 释放鼠标左键

        if event.button() == Qt.LeftButton:

            self.endPoint = event.pos()

            # 重新绘制

            self.update()

            self.isDrawing = False



    def mouseMoveEvent(self, event):

        if event.buttons() and Qt.LeftButton:

            self.endPoint = event.pos()

            self.update()