from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint
from instr import *
from final_win import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
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
        self.T1 = QLabel(t1)
        self.T2 = QLabel(t2)
        self.T3 = QLabel(t3)
        self.T4 = QLabel(t4)
        self.T5 = QLabel(t5)
        self.T5.setWordWrap(True)
        self.T3.setWordWrap(True)
        self.T4.setWordWrap(True)
        self.text_timer = QLabel()
        self.button1 = QPushButton('Начать первый тест')
        self.button2 = QPushButton('Начать делать приседание')
        self.button3 = QPushButton('Начать финальный тест')
        self.button4 = QPushButton('Отправить результаты')
        self.P1 = QLineEdit()
        self.P2 = QLineEdit()
        self.P3 = QLineEdit()
        self.P4 = QLineEdit()
        self.P5 = QLineEdit()
        self.H = QHBoxLayout()
        self.V1 = QVBoxLayout()
        self.V = QVBoxLayout()
        self.V1.addWidget(self.text_timer,alignment = Qt.AlignRight)
        self.V.addWidget(self.T1,alignment = Qt.AlignLeft)
        self.V.addWidget(self.P1,alignment = Qt.AlignLeft)
        self.V.addWidget(self.T2,alignment = Qt.AlignLeft)
        self.V.addWidget(self.P2,alignment = Qt.AlignLeft)
        self.V.addWidget(self.T3,alignment = Qt.AlignLeft)
        self.V.addWidget(self.button1,alignment = Qt.AlignLeft)
        self.V.addWidget(self.P3,alignment = Qt.AlignLeft)
        self.V.addWidget(self.T4,alignment = Qt.AlignLeft)
        self.V.addWidget(self.button2,alignment = Qt.AlignLeft)
        self.V.addWidget(self.T5,alignment = Qt.AlignLeft)
        self.V.addWidget(self.button3,alignment = Qt.AlignLeft)
        self.V.addWidget(self.P4,alignment = Qt.AlignLeft)
        self.V.addWidget(self.P5,alignment = Qt.AlignLeft)
        self.H.addLayout(self.V)
        self.V.addWidget(self.button4,alignment = Qt.AlignCenter)
        self.H.addLayout(self.V1)
        self.setLayout(self.H)

    def connects(self):
        self.button4.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.P2.text(),self.P3.text(),
                            self.P4.text(),self.P5.text())
        self.tw = final_win(self.results(),int(self.index))
    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def connects(self):
        self.button1.clicked.connect(self.timer_test)
    def timer_sits(self):
        #реализация аналогична реализации первого таймера
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        #одно приседание в 1.5 секунды
        self.timer.start(1500)
    def timer2Event(self):
        #реализация аналогична реализации первого обработчика
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
    def timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_final)
    def results(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index>=6 and self.index<11:
                return txt_res3
            elif self.index>=0.5 and self.index<6:
                return txt_res4
            elif self.index<0.4:
                return txt_res5
        elif int(self.exp.age) >=13 and int(self.exp.age) <=14 :
            if self.index >= 16.5:
                return txt_res1
            elif self.index >=12.5 and self.index<16.4:  
                return txt_res2
            elif self.index>=7.5 and self.index<12.4:
                return txt_res3
            elif self.index>2 and self.index<=7.4:
                return txt_res4
            elif self.index<1.9:
                return txt_res5
        elif int(self.exp.age) >= 11 and int(self.exp.age) <=12:
            if self.index >= 18:
                return txt_res1
            elif self.index<14 and self.index>=17.9:
                return txt_res2
            elif self.index>=9 and self.index<13.9:
                return txt_res3
            elif self.index>=3.5 and self.index<8.9:
                return txt_res4
            elif self.index<3.4:
                return txt_res5
        elif int(self.exp.age) >= 9 and int(self.exp.age) <=10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index<15.5 and self.index>=19.4:
                return txt_res2
            elif self.index>=10.5 and self.index<15.4:
                return txt_res3
            elif self.index>=5 and self.index<10.4:
                return txt_res4
            elif self.index<4.9:
                return txt_res5
        elif int(self.exp.age) >= 7 and int(self.exp.age) <=8:
            if self.index >= 21:
                return txt_res1
            elif self.index<17 and self.index>=20.9:
                return txt_res2
            elif self.index>=12 and self.index<16.9:
                return txt_res3
            elif self.index>=6.5 and self.index<11.9:
                return txt_res4
            elif self.index<6.4:
                return txt_res5