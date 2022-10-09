from tqsdk import TqApi, TqKq, TqAuth
import pandas as pd

api = TqApi(TqKq(), auth=TqAuth('shiyindebcd', 'shiyinde1234TQ'))

DCE_Main = api.query_cont_quotes(exchange_id="DCE")         # 主力合约
DCE_Cont = api.query_quotes(ins_class='CONT', exchange_id="DCE")        # 主连
DCE_Future = api.query_quotes(ins_class='FUTURE', exchange_id="DCE")    # 期货
DCE_Index = api.query_quotes(ins_class='INDEX', exchange_id="DCE")      # 指数
DCE_option = api.query_quotes(ins_class='OPTION', exchange_id="DCE")    # 期权

SHFE_Cont = api.query_quotes(ins_class='CONT', exchange_id="SHFE")        # 主连
SHFE_Future = api.query_quotes(ins_class='FUTURE', exchange_id="SHFE")    # 期货
SHFE_Index = api.query_quotes(ins_class='INDEX', exchange_id="SHFE")      # 指数
SHFE_option = api.query_quotes(ins_class='OPTION', exchange_id="SHFE")    # 期权

CZCE_Cont = api.query_quotes(ins_class='CONT', exchange_id="CZCE")        # 主连
CZCE_Future = api.query_quotes(ins_class='FUTURE', exchange_id="CZCE")    # 期货
CZCE_Index = api.query_quotes(ins_class='INDEX', exchange_id="CZCE")      # 指数
CZCE_option = api.query_quotes(ins_class='OPTION', exchange_id="CZCE")    # 期权

CFFEX_Cont = api.query_quotes(ins_class='CONT', exchange_id="CFFEX")        # 主连
CFFEX_Future = api.query_quotes(ins_class='FUTURE', exchange_id="CFFEX")    # 期货
CFFEX_Index = api.query_quotes(ins_class='INDEX', exchange_id="CFFEX")      # 指数
CFFEX_option = api.query_quotes(ins_class='OPTION', exchange_id="CFFEX")    # 期权

INE_Cont = api.query_quotes(ins_class='CONT', exchange_id="INE")        # 主连
INE_Future = api.query_quotes(ins_class='FUTURE', exchange_id="INE")    # 期货
INE_Index = api.query_quotes(ins_class='INDEX', exchange_id="INE")      # 指数
INE_option = api.query_quotes(ins_class='OPTION', exchange_id="INE")    # 期权

klines = api.get_kline_serial('KQ.i@DCE.m', duration_seconds=60, data_length=200)


print(ls)
