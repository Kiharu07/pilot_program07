import yaml #config.yamlを読み取る
import time 
import random
import statistics #統計関数を使うため
import keyboard
import logging 
from logging.handlers import RotatingFileHandler

#数値置場
BUY_STANDARD = 30
SELL_STANDARD = 70
now_price = 140 #初期価格
turn = 0 #初期ターン数
buy_point = 0 #初期買い点
sell_point = 0 #初期売り点
status = "IDLE" #初期ステータス

#開発メモ
# def f(a):
#     a += 1
#     return a
#関数内にて
# a = f (a)　aの値を更新する
#更新するときは値を受け取ることが大切
#returnで返した値を使うことが多い
#returnは変更された値を返す


#初期設定
def setup_app(status):
    status = "IDLE"
    return status 

#ターン進行(qキー)
def advance_turn01(turn):
    if keyboard.is_pressed('q'):
        turn += 1
    return turn

#ターン進行(時間)
def advance_turn02(turn):
    time.sleep(2)  # 2秒待機
    turn += 1
    return turn

#ダミー価格生成
def dummy_price(now_price):
    now_price += random.uniform(-0.02, 0.02)
    return now_price

#ダミー売買点生成
def dummy_buy_sell_points(buy_point, sell_point):
    buy_point = random.uniform(0, 100)
    sell_point = random.uniform(0, 100)
    return buy_point, sell_point

#下落ストッパー
def decline_stopper(trade_price,now_price):
    if trade_price > now_price*0.95 :
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

#ロスカット
def loss_cut(trade_price, now_price, stop_loss_rate):
    if now_price < trade_price * (1 - stop_loss_rate): 
        return True
    else:
        return False

#買い点取得
def get_buy_point(*buys):#chatgptに要望:今後引数が増えても対応するようにしたい
    buy_point =statistics.mean(buys)
    return buy_point

#売り点取得
def get_sell_point(*sells):#chatgptに要望:今後引数が増えても対応するようにしたい   
    sell_point = statistics.mean(sells)
    return sell_point

#取引処理
def trade_execution(buy_point,sell_point,status):
    if status == "IDLE" and buy_point > BUY_STANDARD:
        status = "TRADING"
        # 買い注文を出す処理をここに追加(chatgptよろしく)
    elif status == "TRADING" and sell_point > SELL_STANDARD:
        status = "IDLE"
        # 売り注文を出す処理をここに追加(chatgptよろしく)
    return status

#点数挙動テスト
def test(turn, now_price, status, buy_point, sell_point, ):
    buy_point, sell_point = dummy_buy_sell_points(buy_point, sell_point)
    now_price = dummy_price(now_price)
    status = trade_execution(buy_point, sell_point, status)
    print([turn, now_price, status, buy_point, sell_point])
    return buy_point, sell_point,status

#メイン関数
def main(turn, now_price,status, buy_point,sell_point):
    while True:
        if turn <= 20:
            buy_point,sell_point,status = test(turn, now_price, status, buy_point, sell_point)
            turn = advance_turn02(turn)
            
        else:
            print("ターン数が終点に達しました。プログラムを終了します。")
            break
    return buy_point, sell_point, status, turn

if __name__ == "__main__":
    buy_point, sell_point, status, turn = main(turn, now_price, status, buy_point, sell_point)
    