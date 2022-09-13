import pandas
from datetime import datetime
from tqsdk import tafunc
path = './klines_data/' + 'i2301_1day' + '.csv'
datas = pandas.read_csv(path)
xAixs = 100

# dict = datas.loc[xAixs]
# print(dict['datetime'])
# tickDatetime = tafunc.time_to_str(dict['datetime'])

# dict = datas.to_dict(orient='index', into=dict)
dict1 = dict(zip(datas.index,datas['datetime']))
print(tickDatetime)