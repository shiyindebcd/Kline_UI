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
        
        self.verticalLayout_klines.setContentsMargins(0, 0, 0, 0)   # 设置窗口边界
        self.verticalLayout_klines.addWidget(self.UI_K_chart)
        # self.UI_K_chart.refreshAll()

        self.Btn_add_K_charts_i.clicked.connect(self.show_i_K_chart)
        self.Btn_add_K_charts_rb.clicked.connect(self.show_rb_k_chart)
        self.Btn_klines_1min.clicked.connect(self.print_y_range)
        self.show_i_K_chart()

    # def del_ui_k_chart(self):
    #     self.UI_K_chart.pwVol.clear()
    #     self.UI_K_chart.pwKL.clear()
    #     self.UI_K_chart.pwInd.clear()
    #     self.UI_K_chart.clearData()

    def print_y_range(self):
        self.UI_K_chart.get_item_y_range()

    def show_i_K_chart(self):
        self.UI_K_chart.loadData(pd.read_csv('./DCE_i2209.csv'))
        self.UI_K_chart.refreshAll()
        # self.UI_K_chart.initplotKline()
        # self.UI_K_chart.initplotVol()
        # self.UI_K_chart.initplotIndicators()
        # self.UI_K_chart.plotKline()
        # self.UI_K_chart.generatePicture()

    def show_rb_k_chart(self):
        self.UI_K_chart.loadData(pd.read_csv('./RB9999.csv'))
        self.UI_K_chart.refreshAll()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindows()
    mainWindow.show()
    sys.exit(app.exec()) # 开启事件循环直到应用程序退出