import RPi.GPIO as GPIO
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
       
    servo_pin = params["servo_pin"]
    freq = params["freq"]
    open_angle = params["unlock_angle"]
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin,GPIO.OUT)
    pwm = GPIO.PWM(servo_pin,freq)
    
    with open('lock_status/servo_angle.txt', 'r') as f:
        current_angle = int(f.read().strip()) # 現在の鍵の角度
    orders={ # 指示に対するモーターの動作
        "unlock":unlock(current_angle,pwm),
        "lock":lock(current_angle)
    }
 
    
    status = orders.get(order,other_order(params))
    
def set_servo_angle(angle,pwm):
    """実際にサーボモーターを動作させる関数
    Args:
        angle   (int): モーターの回転角
        pwm     (object):pwm制御を行うためのオブジェクト
    """
    
def unlock(current_angle,open_angle):
    """解錠を行うための関数
    Args:
        current_angle   (int) : 現在の鍵の角度
        params          (dict): サーボモーターを動作させるためのパラメータ
    Return:
        status  (text): 現在の鍵の状態を示す文字列
    """

    
    if current_angle==open_angle:
        status = "Already unlocked."
    else:
        a=1
        
    return status
    
    
def lock(current_angle):
    """施錠を行うための関数
    Args:
    current_angle   (int) : 現在の鍵の角度
        params      (dict): サーボモーターを動作させるためのパラメータ
    Return:
        status      (text): 現在の鍵の状態を示す文字列
    """

def other_order(current_angle):
    """無効な指令が入力された場合の例外処理
    Args:
        params  (dict): サーボモーターを動作させるためのパラメータ
        
    Return:
        status  (text): 無効な指令が与えられたことに対する警告文
    """
    lock(current_angle)
    
    


if __name__ == "__main__":
    order = "unlock"

    with open('motor/motor_config.json', 'r') as f:
        params = json.load(f)
    
    control(order,params)