# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os
import psutil
from PySide6.QtWidgets import QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog, QLabel
from PySide6.QtCore import Qt, Signal, QThread, QStringListModel, QTimer
import pyqtgraph as pg
import pandas as pd
import datetime
from multiprocessing import Process, Manager
from TQ_Services import TQServices
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
        self.main_tq_psd = None  # 主账户密码
        self.Quote_klines_dict = {}  # 自选合约字典,用来存放所有的自选合约klines
        self.quote_dict = {}    # 当前行情切片字典
        self.self_selection = {}    # 自选合约字典
        self.TQ_services_pid = None  # 用来记录天勤数据服务进程的pid
        self.current_dissplayed_Kline = None  # 当前显示的k线品种

        self.ioModal = ReadWriteCsv()
        self.KLineWidget = KLineWidget()
        self.verticalLayout_klines.setContentsMargins(0, 0, 0, 0)   # 设置窗口边界
        self.verticalLayout_klines.addWidget(self.KLineWidget)
        self.ioModal.judge_dirs_exist(dirs='./data')
        self.ioModal.judge_file_exist(path='./data/main_tq_account.csv')
        self.ioModal.judge_file_exist(path='./data/self_selection.csv')
        self.add_paramer_to_container_by_hand()

        # self.add_contracts_to_comboBox_symbol()
        # 面板参数刷新定时器
        self.parameters_refresh = QTimer(self)
        self.parameters_refresh.timeout.connect(self.check_TQ_Services_Status)
        self.parameters_refresh.start(1000)

        self.self_selection_listview.setFocusPolicy(Qt.NoFocus)
        self.self_selection_listview.clicked.connect(self.set_current_dissplayed_Kline)
        self.Btn_draw_line_order.clicked.connect(self.KLineWidget.draw_line_by_mouse)
        self.Btn_draw_line_style.clicked.connect(self.KLineWidget.set_draw_line_style)
        self.Btn_add_self_selection_contracts.clicked.connect(self.add_self_selection_list)

        self.comboBox_add_quote_exchange.activated.connect(self.add_contracts_to_comboBox_symbol)   # comboBox 信号槽函数
        self.comboBox_contract_type.activated.connect(self.add_contracts_to_comboBox_symbol)
        # self.comboBox_symbol.clicked.connect(self.add_contracts_to_comboBox_symbol)

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
            self.self_selection = Manager().dict()
            self.quote_dict = Manager().dict()
            self.current_Kline = Manager().dict()
            self.current_Kline['Contracts'] = self.current_dissplayed_Kline
            data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
            for index, row in data.iterrows():
                self.self_selection[index] = row['quote']
            t = TQServices(args=(self.self_selection, self.quote_dict, self.current_Kline, self.main_tq_account, self.main_tq_psd))
            t.start()
            self.TQ_services_pid = t.pid
            self.label_TQ_services_info.setText('天勤数据行情服务正在运行中')

    def stop_TQ_services(self):     # 关闭天勤数据行情服务
        if self.TQ_services_pid:
            # self.kill_process(self.TQ_services_pid)
            try:
                parent_proc = psutil.Process(self.TQ_services_pid)
                for child_proc in parent_proc.children(recursive=True):
                    child_proc.kill()
                parent_proc.kill()

                print('\npid为 ' + str(self.TQ_services_pid) + ' 的子进程 关闭成功 ！！！\n')
            except Exception as e:
                print('\npid为 ' + str(self.TQ_services_pid) + ' 的子进程 关闭失败 ！！！\n')
                print(e, '\n')

            self.TQ_services_pid = None
        self.label_TQ_services_info.setText('天勤数据行情服务已关闭')
        self.clear_quote_paramer_panel()

    def chack_main_tq_account(self):            # 检查主账号是否存在
        path = './data/main_tq_account.csv'
        if os.path.exists(path):
            data = self.ioModal.read_csv_file(path=path)
            if data.empty:                                     # 判断self.data是否为空
                print('\n\nmain_tq_account.csv文件里没有帐户，请先在设置里添加天勤主账号和密码')
            else:
                self.main_tq_account = data.loc[0, 'tq_account']
                self.main_tq_psd = data.loc[0, 'qt_psd']

    def add_self_selection_list(self):  # 将天勤自选行情引用数据添加到 csv 文件中
        path = './data/self_selection.csv'
        self.ioModal.judge_file_exist(path)
        my_dict = {}
        if self.comboBox_symbol.currentText():
            quote = self.comboBox_symbol.currentText()
            list = self.ioModal.read_csv_file(path)['quote'].tolist()
            if quote in list:
                self.label_kline_info.setText('该合约已在自选列表中,无需添加')
            else:
                my_dict['quote'] = quote
                df = pd.DataFrame(my_dict, index=[0])
                # self.ceate_TQ_klines_and_quote(quote)
                self.ioModal.add_dict_to_csv(df, path)
                text = '新的自选合约： ' + str(quote) + '  已添加'
                self.label_kline_info.setText(text)
                self.add_paramer_to_container_by_hand()
        else:
            self.label_kline_info.setText('请先选择合约后再点添加')

    def set_current_dissplayed_Kline(self, qModelIndex):  # 点击自选列表时,设置并显示当前k线
        row = qModelIndex.row()
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        self.current_dissplayed_Kline = str(data.loc[row]['quote'])
        self.current_Kline['Contracts'] = self.current_dissplayed_Kline
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
        self.self_selection_list, self.quote_dict = self.get_self_selection_quote_list()
        self.current_dissplayed_Kline = self.self_selection_list[0]
        self_selection_model.setStringList(self.self_selection_list)
        self.self_selection_listview.setModel(self_selection_model)

    def get_self_selection_quote_list(self):  # 获取自选行情列表和字典
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        if data.empty:
            quote_list = []
            quote_dict = {}
        else:
            quote_list = data['quote'].tolist()
            quote_dict = data['quote'].to_dict()

        return quote_list, quote_dict

    def add_contracts_to_comboBox_symbol(self):
        if self.comboBox_contract_type.currentText():
            exchange = self.comboBox_add_quote_exchange.currentText().split()[-1]
            type = self.comboBox_contract_type.currentText().split()[-1]
            pth = './available_contracts/' + exchange + '_' + type + '.csv'
            if os.path.exists(pth):
                data = self.ioModal.read_csv_file(path=pth)
                list = data['0'].tolist()
                self.comboBox_symbol.clear()
                self.comboBox_symbol.addItems(list)

    def get_alive_process_pid_list(self):  # 获取运行着的子进程 pid列表
        p = psutil.Process(os.getpid())
        children = p.children()             # 获取p.children()中的所有子进程pid，并生成一个列表
        living_pid_list = []
        for child in children:
            if child.name() == 'python.exe':        # 这里只需要自己策略创建的名为python.exe的子进程,主进程创建的名为conhost.exe的不要
                pid = child.pid
                if pid not in living_pid_list:
                    living_pid_list.append(pid)
            else:
                pass
        return living_pid_list

    def check_TQ_Services_Status(self):
        if self.TQ_services_pid:
            pid_list = self.get_alive_process_pid_list()
            if self.TQ_services_pid in pid_list:
                self.label_TQ_services_info.setText('天勤数据行情服务正在运行中')
                print('\n\n从天勤行情服务中获得的切片数据为:', self.quote_dict)
                if len(self.quote_dict) > 0:
                    self.add_quote_paramer_to_panel()
            else:
                self.label_TQ_services_info.setText('天勤数据行情服务已停止')


    def add_quote_paramer_to_panel(self):
        self.label_instrument_name.setText(str(self.quote_dict['instrument_name']))  # 合约中文名称
        self.label_instrument_id.setText(str(self.quote_dict['instrument_id']))  # 合约代码
        self.label_last_price.setText(str(self.quote_dict['last_price']))  # 最新价格
        self.label_ask_price1.setText(str(self.quote_dict['ask_price1']))  # 卖一价格
        self.label_bid_price1.setText(str(self.quote_dict['bid_price1']))  # 买一价格
        self.label_ask_volume1.setText(str(self.quote_dict['ask_volume1']))  # 卖一数量
        self.label_bid_volume1.setText(str(self.quote_dict['bid_volume1']))  # 买一数量
        self.label_open.setText(str(self.quote_dict['open']))  # 开盘价
        self.label_highest.setText(str(self.quote_dict['highest']))  # 最高价
        self.label_lowest.setText(str(self.quote_dict['lowest']))  # 最低价
        self.label_pre_close.setText(str(self.quote_dict['pre_close']))  # 昨收盘价
        self.label_pre_settlement.setText(str(self.quote_dict['pre_settlement']))  # 昨结算价
        self.label_upper_limit.setText(str(self.quote_dict['upper_limit']))  # 涨停价
        self.label_lower_limit.setText(str(self.quote_dict['lower_limit']))  # 跌停价
        self.label_volume.setText(str(self.quote_dict['volume']))  # 成交量
        self.label_open_interest.setText(str(self.quote_dict['open_interest']))  # 持仓量
        self.label_settlement.setText(str(self.quote_dict['settlement']))  # 结算价
        self.label_expire_rest_days.setText(str(self.quote_dict['expire_rest_days']))  # 到期剩余天数
        percent_increase = (self.quote_dict['last_price'] - self.quote_dict['pre_close']) / (self.quote_dict['pre_close'])  # 涨跌幅
        if percent_increase >= 0:
            self.label_percent_increase.setStyleSheet(u"color: rgb(255, 0, 0);\n""font: 700 14pt \"\u7b49\u7ebf\";")
        else:
            self.label_percent_increase.setStyleSheet(u"color: rgb(0, 255, 0);\n""font: 700 14pt \"\u7b49\u7ebf\";")
        self.label_percent_increase.setText('{:.2%}'.format(percent_increase))  # 涨跌幅
        self.label_daily_increase.setText(str((self.quote_dict['open_interest'] - self.quote_dict['pre_open_interest'])))  # 日增仓= 持仓量-昨持仓量


    def clear_quote_paramer_panel(self):
        self.label_instrument_name.setText('')
        self.label_instrument_id.setText('')
        self.label_last_price.setText('')
        self.label_ask_price1.setText('')
        self.label_bid_price1.setText('')
        self.label_ask_volume1.setText('')
        self.label_bid_volume1.setText('')
        self.label_open.setText('')
        self.label_highest.setText('')
        self.label_lowest.setText('')
        self.label_pre_close.setText('')
        self.label_pre_settlement.setText('')
        self.label_upper_limit.setText('')
        self.label_lower_limit.setText('')
        self.label_volume.setText('')
        self.label_open_interest.setText('')
        self.label_settlement.setText('')
        self.label_expire_rest_days.setText('')
        self.label_percent_increase.setText('')
        self.label_daily_increase.setText('')








if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindows()
    mainWindow.show()
    sys.exit(app.exec()) # 开启事件循环直到应用程序退出