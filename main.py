# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os
from PySide6.QtWidgets import QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog, QLabel
from PySide6.QtCore import Qt, Signal, QThread, QStringListModel
import pyqtgraph as pg
import pandas as pd
import datetime
from tqsdk import TqApi, TqAuth, TargetPosTask, TqKq, TqBacktest, tafunc
from tqsdk import ta, tafunc
from datetime import date
from read_write_file import ReadWriteCsv
from KLineWidget import *
from MainFrame import Ui_Form


class MainWindows(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        
        self.setupUi(self)
        self.main_tq_account = None  # 主账户
        self.main_tq__pwd = None  # 主账户密码
        self.Quote_klines_dict = {}  # 自选合约字典,用来存放所有的自选合约klines
        self.TQ_services_pid = None  # 用来记录天勤数据服务进程的pid
        self.current_dissplayed_Kline = None  # 当前显示的k线品种

        self.ioModal = ReadWriteCsv()
        self.KLineWidget = KLineWidget()
        self.current_dissplayed_Kline = None
        self.verticalLayout_klines.setContentsMargins(0, 0, 0, 0)   # 设置窗口边界
        self.verticalLayout_klines.addWidget(self.KLineWidget)
        self.ioModal.judge_dirs_exist(dirs='./data')
        self.ioModal.judge_config_exist(path='./data/main_tq_account.csv')
        self.ioModal.judge_config_exist(path='./data/self_selection.csv')
        self.add_paramer_to_container_by_hand()


        self.self_selection_listview.setFocusPolicy(Qt.NoFocus)
        self.self_selection_listview.clicked.connect(self.set_current_dissplayed_Kline)
        self.Btn_draw_line_order.clicked.connect(self.KLineWidget.draw_line_by_mouse)
        self.Btn_draw_line_style.clicked.connect(self.KLineWidget.set_draw_line_style)
        self.Btn_add_self_selection_contracts.clicked.connect(self.add_self_selection_list)

        self.Btn_start_TQ_services.clicked.connect(self.start_TQ_services)
        self.Btn_stop_TQ_services.clicked.connect(self.stop_TQ_services)
        self.Btn_klines_1min.clicked.connect(self.show_1min_kline)
        self.Btn_klines_15min.clicked.connect(self.show_15min_kline)
        self.Btn_klines_30min.clicked.connect(self.show_30min_kline)
        self.Btn_klines_1hour.clicked.connect(self.show_1hour_kline)
        self.Btn_klines_2hour.clicked.connect(self.show_2hour_kline)
        self.Btn_klines_4hour.clicked.connect(self.show_4hour_kline)
        self.Btn_klines_daily.clicked.connect(self.show_1day_kline)

    def start_TQ_services(self):    # 开启天勤数据行情服务
        self.chack_main_tq_account()
        if self.main_tq_account and self.main_tq_psd:
            self.label_TQ_services_info.setText('天勤数据行情服务正在运行中')

    def stop_TQ_services(self):     # 关闭天勤数据行情服务
        if self.TQ_services_pid:
            self.kill_process(self.TQ_services_pid)
            try:
                parent_proc = psutil.Process(self.TQ_services_pid)
                for child_proc in parent_proc.children(recursive=True):
                    child_proc.kill()
                parent_proc.kill()

                print('\npid为 ' + str(pid) + ' 的子进程 关闭成功 ！！！\n')
            except Exception as e:
                print('\npid为 ' + str(pid) + ' 的子进程 关闭失败 ！！！\n')
                print(e, '\n')

            self.TQ_services_pid = None
        self.label_TQ_services_info.setText('天勤数据行情服务已关闭')

    def chack_main_tq_account(self):            # 检查主账号是否存在
        path = './data/main_tq_account.csv'
        if os.path.exists(path):
            data = self.ioModal.read_csv_file(path=path)
            if data.empty:                                     # 判断self.data是否为空
                print('\n\nmain_tq_account.csv文件里没有帐户，请先在设置里添加天勤主账号和密码')
            else:
                self.main_tq_account = data.iloc[0, 0]
                self.main_tq_psd = data.iloc[0, 1]

    def add_self_selection_list(self):  # 将天勤自选行情引用数据添加到 csv 文件中
        my_dict = {}
        exchange = self.comboBox_add_quote_exchange.currentText().split()[-1]  # 获取列表框选择的字符串分割后的最后一部分
        quote = exchange + '.' + self.add_quote_symbol.text()
        if self.add_quote_symbol.text():
            my_dict['quote'] = quote
            df = pd.DataFrame(my_dict, index=[0])
            # self.ceate_TQ_klines_and_quote(quote)
            self.ioModal.add_dict_to_csv(df, path='./data/self_selection.csv')
            text = '新的自选合约： ' + str(quote) + '  已添加'
            self.label_kline_info.setText(text)
            self.add_quote_symbol.clear()
            self.add_paramer_to_container_by_hand()
        else:
            self.label_kline_info.setText('请输入正确的合约名再点添加')

    def set_current_dissplayed_Kline(self, qModelIndex):  # 点击自选列表时,设置并显示当前k线
        row = qModelIndex.row()
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        self.current_dissplayed_Kline = str(data.loc[row]['quote'])
        self.show_kline(self.current_dissplayed_Kline,period='15min')

    def show_1min_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline,period='1min')


    def show_15min_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='15min')


    def show_30min_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='30min')


    def show_1hour_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='1hour')


    def show_2hour_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='2hour')


    def show_4hour_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='4hour')


    def show_1day_kline(self):
        if self.current_dissplayed_Kline:
            self.show_kline(self.current_dissplayed_Kline, period='1day')


    def show_kline(self, Species, period):
        file_path = './Klines_Data/' + Species + '_' + period + '.csv'
        if os.path.exists(file_path):
            kline_data = self.ioModal.read_csv_file(path=file_path)
            self.KLineWidget.loadData(kline_data)
            self.KLineWidget.refreshAll()
            self.label_kline_info.setText(Species + '_' + period)
        else:
            self.label_kline_info.setText('没有数据,请检查合约名是否正确')

    def add_paramer_to_container_by_hand(self):         # 将参数添加到面板各容器中, 人工动作驱动部分

        self_selection_model = QStringListModel()
        self.self_selection_list = self.get_self_selection_quote_list()
        self_selection_model.setStringList(self.self_selection_list)
        self.self_selection_listview.setModel(self_selection_model)

    def get_self_selection_quote_list(self):  # 获取自选行情列表
        quote_list = []
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        if data.empty:
            quote_list = []
        else:
            for index, item in data.iterrows():
                quote_list.append(str(item['quote']))
        #         self.self_selection_dict[str(item['quote'] + '_1_min')] = str(item['quote'] + '_1_min')
        #         self.self_selection_dict[str(item['quote'] + '_15_min')] = str(item['quote'] + '_15_min')
        #         self.self_selection_dict[str(item['quote'] + '_30_min')] = str(item['quote'] + '_30_min')
        #         self.self_selection_dict[str(item['quote'] + '_60_min')] = str(item['quote'] + '_60_min')
        #         self.self_selection_dict[str(item['quote'] + '_120_min')] = str(item['quote'] + '_120_min')
        #         self.self_selection_dict[str(item['quote'] + '_240_min')] = str(item['quote'] + '_240_min')
        #         self.self_selection_dict[str(item['quote'] + '_1440_min')] = str(item['quote'] + '_1440_min')

        # print(self.self_selection_dict)
        return quote_list



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindows()
    mainWindow.show()
    sys.exit(app.exec()) # 开启事件循环直到应用程序退出