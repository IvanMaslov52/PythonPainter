import random

from PyQt5 import QtCore
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys





class Window(QMainWindow):
    def __init__(self,x_1,y_1):#конструктор где мы задаем название окна (рандомную величину), размеры и вызывается функция с инициализацией самого окна
        super().__init__()
        self.title = "Drawing"
        self.top = 150
        self.left = 150
        self.width = 600
        self.height = 600
        self.x1 = x_1
        self.y1 = y_1
        self.rand = random.randint(1, 500)
        self.InitWindow()
        self.paintEvent(self.InitWindow(),)

    def InitWindow(self):#функция для инициализация окна(размер, название окна)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def paintEvent(self, event):#функция для рисования (настраивает рисовальщика и рисует квадрат)
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.black)
        painter.setBrush(QtCore.Qt.white)
        self.drawCustomLine(painter,self.x1,self.y1,self.x1+self.rand,self.y1)
        self.drawCustomLine(painter, self.x1, self.y1 + self.rand,self.x1+self.rand, self.y1 + self.rand)
        self.drawCustomLine(painter, self.x1,self.y1, self.x1,self.y1+self.rand)
        self.drawCustomLine(painter, self.x1+self.rand,self.y1, self.x1+self.rand,self.y1+self.rand)

    def drawCustomLine(self,painter, x1,y1,x2,y2): #функция рисующая прямую с помощью двух точек

        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1

        error, t = el / 2, 0

        painter.drawPoint(x, y)

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            painter.drawPoint(x, y)



app1 = QApplication(sys.argv)
window = Window(100,100)
window.show()
sys.exit(app1.exec())
