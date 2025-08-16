import yaml #config.yamlを読み取る
import time 
import random
import statistics #統計関数を使うため
import logging 
from logging.handlers import RotatingFileHandler



def unchi(a,b):
    c =a+b
    return c

def main():
    m = input("数字をいえよ")
    n = input("もひとついえよ")
    print(unchi(m,n))
    return None


#下落ストッパー
def pricedown_stopper(trade_price,now_price):
    if trade_price > nowprice*0.95
        return True
    else:
        return False

#移動平均を計算する関数    
def moving_average(price_history,period):
    return statistics.mean(price_history[-period:]) #リストの最後のperiod個の平均

#短期移動平均
def short_term_moving_average(price_history,short_period):
    return moving_average(price_history,short_period)

#長期移動平均
def long_term_moving_average(price_history,long_period):    
    return moving_average(price_history,long_period)

#RSIを計算する関数(買いすぎ売りすぎ)(意味わからんので解説ください)
def RSI(UP,DOWN):
    RSI = 100 - (100 / (1 + UP / DOWN))
    return RSI

#MACDを計算する関数
def MACD(short_term,long_term):
    MACD = short_term - long_term
    return MACD
#わけわからん教えて





if __name__ == "__main__":
    main()
    