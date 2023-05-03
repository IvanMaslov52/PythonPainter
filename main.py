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

        dx = x2 - x1 #проекция на ось x
        dy = y2 - y1 #проекция на ось y

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0 #Определяем, в какую сторону нужно будет сдвигаться. Если dx < 0, т.е. отрезок идёт
                                                      # справа налево по иксу, то sign_x будет равен -1.
	                                                  #Это будет использоваться в цикле постороения.
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0 #Аналогично. Если рисуем отрезок снизу вверх -
	                                                  #это будет отрицательный сдвиг для y (иначе - положительный).

        if dx < 0: dx = -dx #dx = |dx|
        if dy < 0: dy = -dy #dy = |dy|

        if dx > dy: #определяем наклон отрезка
            # Если dx > dy, то значит отрезок "вытянут" вдоль оси икс, т.е. он скорее длинный, чем высокий.
            # Значит в цикле нужно будет идти по икс (строчка el = dx;), значит "протягивать" прямую по иксу
            pdx, pdy = sign_x, 0
            es, el = dy, dx ;
        else:#случай, когда прямая скорее "высокая", чем длинная, т.е. вытянута по оси y
            pdx, pdy = 0, sign_y
            es, el = dx, dy #тогда в цикле будем двигаться по y

        x, y = x1, y1

        error, t = el / 2, 0

        painter.drawPoint(x, y) #ставим первую точку
        #все последующие точки возможно надо сдвигать, поэтому первую ставим вне цикла

        while t < el: #идём по всем точкам, начиная со второй и до последней
            error -= es
            if error < 0:
                error += el
                x += sign_x #сдвинуть прямую (сместить вверх или вниз, если цикл проходит по иксам)
                y += sign_y #или сместить влево-вправо, если цикл проходит по y
            else:
                x += pdx #продолжить тянуть прямую дальше, т.е. сдвинуть влево или вправо, если
                y += pdy #цикл идёт по иксу; сдвинуть вверх или вниз, если по y
            t += 1
            painter.drawPoint(x, y) #



app1 = QApplication(sys.argv)
window = Window(100,100)
window.show()
sys.exit(app1.exec())
