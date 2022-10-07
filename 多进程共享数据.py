from multiprocessing import Process,Manager
import os
import time
from read_write_file import ReadWriteCsv, Logger


class TQServices(Process):

    def __init__(self, args):
        Process.__init__(self)
        self.dict_quote = args[0]
        self.list_selection = args[1]
        self.current_Kline = args[2]
        self.ioModal = ReadWriteCsv()
        self.data = self.ioModal.read_csv_file(path='Klines_data/DCE.i2301_1day.csv')

    def run(self):
        while True:
            for index, row in self.data.iterrows():

                self.dict_quote['open'] = row['open']
                self.dict_quote['high'] = row['high']
                self.dict_quote['low'] = row['low']
                self.dict_quote['close'] = row['close']
                self.dict_quote['volume'] = row['volume']

                # self.list_selection.append(index)
                # self.list_selection.append(row['datetime'])
                # self.list_selection.append(row['symbol'])
                # self.list_selection.append(row['duration'])

                self.current_Kline['current_dissplayed_Kline'] = row['datetime']
                time.sleep(5)



if __name__ == '__main__':
    manager = Manager()
    current_Kline = manager.dict()
    dict_quote = manager.dict()          # 生成一个字典,用于在多个进程之间共享
    list_selection = manager.list()          # 生成一个列表,用于在多个进程之间共享
    p = TQServices(args=(dict_quote,list_selection, current_Kline))
    p.start()

    while True:
        print('当前行的字典为: ', dict_quote)
        # print('列表为: ', list_selection)
        print('current_Kline: ', current_Kline)
        time.sleep(5)

