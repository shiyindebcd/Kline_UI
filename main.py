# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets
import sys
from PySide6.QtWidgets import QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog, QLabel
from PySide6.QtCore import Qt, Signal, QThread
import pyqtgraph as pg
import pandas as pd
import datetime
from tqsdk import TqApi, TqAuth, TargetPosTask, TqKq, TqBacktest, tafunc
from tqsdk import ta, tafunc
from datetime import date
from KLineClass import *
from MainFrame import Ui_Form


class MainWindows(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        
        self.setupUi(self)

        self.UI_K_chart = KLineWidget()
        self.Current_Species = ''
        self.verticalLayout_klines.setContentsMargins(0, 0, 0, 0)   # 设置窗口边界
        self.verticalLayout_klines.addWidget(self.UI_K_chart)

        self.Btn_add_K_charts_i.clicked.connect(self.show_i_K_chart)
        self.Btn_add_K_charts_rb.clicked.connect(self.show_rb_K_chart)
        self.Btn_klines_1min.clicked.connect(lambda: self.show_candels(self.Current_Species, '1min'))
        self.Btn_klines_15min.clicked.connect(lambda: self.show_candels(self.Current_Species, '15min'))
        self.Btn_klines_30min.clicked.connect(lambda: self.show_candels(self.Current_Species, '30min'))
        self.Btn_klines_1hour.clicked.connect(lambda: self.show_candels(self.Current_Species, '1hour'))
        self.Btn_klines_2hour.clicked.connect(lambda: self.show_candels(self.Current_Species, '2hour'))
        self.Btn_klines_4hour.clicked.connect(lambda: self.show_candels(self.Current_Species, '4hour'))
        self.Btn_klines_daily.clicked.connect(lambda: self.show_candels(self.Current_Species, '1day'))

        self.show_i_K_chart()


    def show_i_K_chart(self):
        self.Current_Species = 'i2301'
        self.show_candels(self.Current_Species,period='15min')
        self.label_kline_info.setText(self.Current_Species + '_15min')
        self.UI_K_chart.refreshAll()

    def show_rb_K_chart(self):
        self.Current_Species = 'rb2210'
        self.show_candels(self.Current_Species, period='15min')
        self.label_kline_info.setText(self.Current_Species + '_15min')
        self.UI_K_chart.refreshAll()

    def show_candels(self, Species, period):
        path ='./klines_data/' + Species + '_' + period + '.csv'
        self.UI_K_chart.loadData(pd.read_csv(path))
        self.UI_K_chart.refreshAll()
        self.label_kline_info.setText(self.Current_Species + '_' + period)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindows()
    mainWindow.show()
    sys.exit(app.exec()) # 开启事件循环直到应用程序退出