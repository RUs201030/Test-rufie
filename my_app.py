from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from instr import *
from second_win import *


    

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.T1 = QLabel(Text1)
        self.T2 = QLabel(Text2)
        self.T2.setWordWrap(True)
        self.button = QPushButton('Начать')
        self.V = QVBoxLayout()
        self.V.addWidget(self.T1,alignment = Qt.AlignCenter)
        self.V.addWidget(self.T2,alignment = Qt.AlignCenter)
        self.V.addWidget(self.button,alignment = Qt.AlignCenter)
        self.setLayout(self.V)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()


#main_win = QWidget()
#main_win.setWindowTitle('Тест Руфье')
#main_win.resize(2000,1000)
'''T1 = QLabel('...')
T2 = QLabel('.....')
button = QPushButton('Начать')
V = QVBoxLayout()
V.addWidget(T1,alignment = Qt.AlignLeft)
V.addWidget(T2,alignment = Qt.AlignLeft)
V.addWidget(button,alignment = Qt.AlignCenter)'''
#main_win.setLayout(V)
#main_win.show()
app = QApplication([])
a = MainWin()
app.exec_()


