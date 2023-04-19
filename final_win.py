from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from instr import *
from second_win import *


class final_win(QWidget):
    def __init__(self,exp,index):
        super().__init__()
        self.index = index
        self.set_appear()
        self.exp = exp
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.V = QVBoxLayout()
        self.T1 = QLabel(txt_workheart + str(self.exp))
        self.T2= QLabel(txt_index + str(self.index))
        self.V.addWidget(self.T1,alignment = Qt.AlignCenter)
        self.V.addWidget(self.T2,alignment = Qt.AlignCenter)  
        self.setLayout(self.V)