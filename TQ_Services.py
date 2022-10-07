#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'shiyinde'


from multiprocessing import Process, Manager
import time
import datetime
import sys
import os
from tqsdk import TqApi, TqKq, TqSim, TqAuth
from read_write_file import ReadWriteCsv, Logger


class TQServices(Process):

    def __init__(self, args):
        Process.__init__(self)
        self.self_selection = args[0]
        self.quote_dict = args[1]
        self.current_Kline = args[2]
        self.main_tq_account = args[3]
        self.main_tq__pwd = args[4]

        self.current_tmp = {}
        self.current_tmp['Contracts'] = ''
        self.ioModal = ReadWriteCsv()


    def run(self):
        sys.stdout = Logger(process_name='天勤行情数据服务日志')  # 由 logger 类实例化的对象接管系统标准输出
        self.api = TqApi(TqKq(), auth=TqAuth(self.main_tq_account, self.main_tq__pwd))
        while True:
            for key, value in self.self_selection.items():
                path = './Klines_data/' + value + '_15min.csv'
                if not os.path.exists(path):
                    self.create_new_file(value)
                    print('k线数据文件已保存')
                else:
                    # self.create_normal_klines(value)
                    print('合约有k线数据')
            if self.current_tmp['Contracts'] is None:
                print('self.current_tmp is None')
                self.current_tmp['Contracts'] = self.current_Kline['Contracts']
            else:
                if self.current_Kline['Contracts'] != self.current_tmp['Contracts']:
                    self.quote = self.api.get_quote(self.current_Kline['Contracts'])
                    print(self.quote)
                    print(' 运行到这里了')
                    self.current_tmp['Contracts'] = self.current_Kline['Contracts']
                    self.quote_dict_Assignment(self.quote)
                else:
                    self.api.wait_update()
                    self.quote_dict_Assignment(self.quote)


    def quote_dict_Assignment(self, dict):                  # 给quote_dict赋值
         self.quote_dict['datetime'] = dict['datetime']
         self.quote_dict['ask_price1'] = dict['ask_price1']
         self.quote_dict['ask_volume1'] = dict['ask_volume1']
         self.quote_dict['bid_price1'] = dict['bid_price1']
         self.quote_dict['bid_volume1'] = dict['bid_volume1']
         self.quote_dict['ask_price2'] = dict['ask_price2']
         self.quote_dict['ask_volume2'] = dict['ask_volume2']
         self.quote_dict['bid_price2'] = dict['bid_price2']
         self.quote_dict['bid_volume2'] = dict['bid_volume2']
         self.quote_dict['ask_price3'] = dict['ask_price3']
         self.quote_dict['ask_volume3'] = dict['ask_volume3']
         self.quote_dict['bid_price3'] = dict['bid_price3']
         self.quote_dict['bid_volume3'] = dict['bid_volume3']
         self.quote_dict['ask_price4'] = dict['ask_price4']
         self.quote_dict['ask_volume4'] = dict['ask_volume4']
         self.quote_dict['bid_price4'] = dict['bid_price4']
         self.quote_dict['bid_volume4'] = dict['bid_volume4']
         self.quote_dict['ask_price5'] = dict['ask_price5']
         self.quote_dict['ask_volume5'] = dict['ask_volume5']
         self.quote_dict['bid_price5'] = dict['bid_price5']
         self.quote_dict['bid_volume5'] = dict['bid_volume5']
         self.quote_dict['last_price'] = dict['last_price']
         self.quote_dict['highest'] = dict['highest']
         self.quote_dict['lowest'] = dict['lowest']
         self.quote_dict['open'] = dict['open']
         self.quote_dict['close'] = dict['close']
         self.quote_dict['average'] = dict['average']
         self.quote_dict['volume'] = dict['volume']
         self.quote_dict['amount'] = dict['amount']
         self.quote_dict['open_interest'] = dict['open_interest']
         self.quote_dict['settlement'] = dict['settlement']
         self.quote_dict['upper_limit'] = dict['upper_limit']
         self.quote_dict['lower_limit'] = dict['lower_limit']
         self.quote_dict['pre_open_interest'] = dict['pre_open_interest']
         self.quote_dict['pre_settlement'] = dict['pre_settlement']
         self.quote_dict['pre_close'] = dict['pre_close']
         self.quote_dict['price_tick'] = dict['price_tick']
         self.quote_dict['price_decs'] = dict['price_decs']
         self.quote_dict['volume_multiple'] = dict['volume_multiple']
         self.quote_dict['max_limit_order_volume'] = dict['max_limit_order_volume']
         self.quote_dict['max_market_order_volume'] = dict['max_market_order_volume']
         self.quote_dict['min_limit_order_volume'] = dict['min_limit_order_volume']
         self.quote_dict['min_market_order_volume'] = dict['min_market_order_volume']
         self.quote_dict['underlying_symbol'] = dict['underlying_symbol']
         self.quote_dict['strike_price'] = dict['strike_price']
         self.quote_dict['ins_class'] = dict['ins_class']
         self.quote_dict['instrument_id'] = dict['instrument_id']
         self.quote_dict['instrument_name'] = dict['instrument_name']
         self.quote_dict['exchange_id'] = dict['exchange_id']
         self.quote_dict['expired'] = dict['expired']
         # self.quote_dict['trading_time'] = dict['trading_time']
         self.quote_dict['expire_datetime'] = dict['expire_datetime']
         self.quote_dict['delivery_year'] = dict['delivery_year']
         self.quote_dict['delivery_month'] = dict['delivery_month']
         self.quote_dict['last_exercise_datetime'] = dict['last_exercise_datetime']
         self.quote_dict['exercise_year'] = dict['exercise_year']
         self.quote_dict['exercise_month'] = dict['exercise_month']
         self.quote_dict['option_class'] = dict['option_class']
         self.quote_dict['exercise_type'] = dict['exercise_type']
         self.quote_dict['product_id'] = dict['product_id']
         self.quote_dict['iopv'] = dict['iopv']
         self.quote_dict['public_float_share_quantity'] = dict['public_float_share_quantity']
         self.quote_dict['stock_dividend_ratio'] = dict['stock_dividend_ratio']
         self.quote_dict['cash_dividend_ratio'] = dict['cash_dividend_ratio']
         self.quote_dict['expire_rest_days'] = dict['expire_rest_days']
         self.quote_dict['commission'] = dict['commission']
         self.quote_dict['margin'] = dict['margin']


    def create_normal_klines(self, value):
        klines_1min = self.api.get_kline_serial(value, duration_seconds=60, data_length=200)
        klines_15min = self.api.get_kline_serial(value, duration_seconds=60 * 15, data_length=200)
        klines_30min = self.api.get_kline_serial(value, duration_seconds=60 * 30, data_length=200)
        klines_1hour = self.api.get_kline_serial(value, duration_seconds=60 * 60, data_length=200)
        klines_2hour = self.api.get_kline_serial(value, duration_seconds=60 * 60 * 2, data_length=200)
        klines_4hour = self.api.get_kline_serial(value, duration_seconds=60 * 60 * 4, data_length=100)
        klines_1day = self.api.get_kline_serial(value, duration_seconds=60 * 60 * 24, data_length=50)

    def create_new_file(self, value):
        klines_1min = self.api.get_kline_serial(value, duration_seconds=60, data_length=8000)
        klines_15min = self.api.get_kline_serial(value, duration_seconds=60*15, data_length=8000)
        klines_30min = self.api.get_kline_serial(value, duration_seconds=60*30, data_length=6000)
        klines_1hour = self.api.get_kline_serial(value, duration_seconds=60*60, data_length=4000)
        klines_2hour = self.api.get_kline_serial(value, duration_seconds=60*60*2, data_length=2000)
        klines_4hour = self.api.get_kline_serial(value, duration_seconds=60*60*4, data_length=1000)
        klines_1day = self.api.get_kline_serial(value, duration_seconds=60*60*24, data_length=300)

        data1 = klines_1min.drop(klines_1min[klines_1min['id']<0].index)         # 删除空行
        data1 = data1.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_1min.csv'))
        self.ioModal.write_datas_to_csv_file(data1, path=('./Klines_data/' + value + '_1min.csv'))

        data2 = klines_15min.drop(klines_15min[klines_15min['id']<0].index)         # 删除空行
        data2 = data2.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_15min.csv'))
        self.ioModal.write_datas_to_csv_file(data2, path=('./Klines_data/' + value + '_15min.csv'))

        daya3 = klines_30min.drop(klines_30min[klines_30min['id']<0].index)         # 删除空行
        daya3 = daya3.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_30min.csv'))
        self.ioModal.write_datas_to_csv_file(daya3, path=('./Klines_data/' + value + '_30min.csv'))

        daya4 = klines_1hour.drop(klines_1hour[klines_1hour['id']<0].index)         # 删除空行
        daya4 = daya4.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_1hour.csv'))
        self.ioModal.write_datas_to_csv_file(daya4, path=('./Klines_data/' + value + '_1hour.csv'))

        daya5 = klines_2hour.drop(klines_2hour[klines_2hour['id']<0].index)         # 删除空行
        daya5 = daya5.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_2hour.csv'))
        self.ioModal.write_datas_to_csv_file(daya5, path=('./Klines_data/' + value + '_2hour.csv'))

        data6 = klines_4hour.drop(klines_4hour[klines_4hour['id']<0].index)         # 删除空行
        data6 = data6.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_4hour.csv'))
        self.ioModal.write_datas_to_csv_file(data6, path=('./Klines_data/' + value + '_4hour.csv'))

        data7 = klines_1day.drop(klines_1day[klines_1day['id']<0].index)         # 删除空行
        data7 = data7.reset_index(drop=True)                        # 重建索引
        self.ioModal.judge_config_exist(path=('./Klines_data/' + value + '_1day.csv'))
        self.ioModal.write_datas_to_csv_file(data7, path=('./Klines_data/' + value + '_1day.csv'))




if __name__ == '__main__':

    self_selection = Manager().dict()
    quote_dict = Manager().dict()
    current_Kline = Manager().dict()
    current_Kline['Contracts'] = 'DCE.i2301'
    main_tq_account = 'a哆啦a梦'
    main_tq__pwd = 'c168168'
    ioModal = ReadWriteCsv()
    data = ioModal.read_csv_file(path='./data/self_selection.csv')
    for index,row in data.iterrows():
        self_selection[index] = row['quote']
    t = TQServices(args=(self_selection, quote_dict, current_Kline, main_tq_account, main_tq__pwd))
    t.start()

    while True:
        time.sleep(1)
        print('自选列表:  ', self_selection)
        print('当前行情引用:  ', quote_dict)
        print('当前显示合约:  ', current_Kline)
        print('天勤账户:  ', main_tq_account)
        print('天勤密码:  ', main_tq__pwd)