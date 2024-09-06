import RPi.GPIO
import time
import json


def control(order,params):
    """鍵の状態をコントロールするための関数
    Args:
        order   (text): 解錠または施錠の指示
        params  (dict): サーボモーターを動作させるためのパラメータ
        
    Return:
        status  (text): 現在の鍵の状態を表す文字列
    """
    
    with open('log/servo_angle.txt', 'r') as f:
        current_angle = int(f.read().strip())
    orders={
        "open":unlock(params),
        "lock":lock(params)
    }
    
    status = orders.get(order,other_order(params))
    
def unlock(params):
    """解錠を行うための関数
    Args:
        params  (dict): サーボモーターを動作させるためのパラメータ
    
    """
    
def lock(params):
    """施錠を行うための関数
    
    """

def other_order(params):
    """無効な指令が入力された場合の例外処理
    Args:
        params  (dict): サーボモーターを動作させるためのパラメータ
        
    Return:
        status  (text): 無効な指令が与えられたことに対する警告文
    """
    lock(params)
    
    


if __name__ == "__main__":
    order = "open"

    with open('motor_config.json', 'r') as f:
        params = json.load(f)
    
    control(order,params)