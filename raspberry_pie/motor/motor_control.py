import os
import sys
import RPi.GPIO as GPIO
import time
import json
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import utils
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = Path(current_dir).parent # 親ディレクトリの取得(loggerの設定のため)

def neutral(params):
    """モーターをニュートラルに戻す関数
    """
    servo_pin = params["servo_pin"]
    freq = params["freq"]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin,GPIO.OUT)
    pwm = GPIO.PWM(servo_pin,freq)
    pwm.start(7.0)
    time.sleep(1)
    pwm.ChangeDutyCycle(7.25)
    time.sleep(1)

def control(order,params, current_angle):
    """鍵の状態をコントロールするための関数
    Args:
        order   (str): 解錠または施錠の指示
        params  (dict): サーボモーターを動作させるためのパラメータ
        current_angle (str): 現在の鍵の角度
        
    Return:
        status  (str): 現在の鍵の状態を表す文字列
        current_state (str):  操作後の鍵の角度
    """
    
    log_dir = os.path.join(parent_dir,"log/")
    logger = utils.set_logging(log_dir,"servo_status")
       
    servo_pin = params["servo_pin"]
    freq = params["freq"]
    
    logger.info("モーターを動作させます。")
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin,GPIO.OUT)
    pwm = GPIO.PWM(servo_pin,freq)
    
    #file_path = parent_dir / 'lock_status' / 'servo_angle.txt'

    #with open(file_path, 'r') as f:
    #    current_angle = int(f.read().strip()) # 現在の鍵の角度
        
    logger.info(f"現在の鍵の角度：{current_angle} °C")
    
    orders={ # 指示に対するモーターの動作
        "unlock":unlock,
        "lock":lock
    }
    
    func = orders.get(order,"other_order")
    if func == "other_order":
        status, current_state, warn_msg = other_order(params,pwm,params["lock"],order,logger)
        logger.warning(f"無効なメッセージが入力されました。: {warn_msg}")
        #with open(file_path,'w') as f:
        #    f.write(str(params["lock"]["angle"]))
    else:
        status, current_state = func(current_angle,pwm,params[order])
        #with open(file_path,'w') as f:
        #    f.write(str(params[order]["angle"]))
    logger.info(status)
    

    
    return status, current_state
    
def set_servo_angle(param,pwm):
    """実際にサーボモーターを動作させる関数
    Args:
        param   (dict): サーボモーターを動作させるためのパラメーター
        pwm     (object):PWM制御を行うためのオブジェクト
    """
    pwm.start(7.0)
    pwm.ChangeDutyCycle(param["duty_cycle"])
    time.sleep(2)
    
    
    
def unlock(current_angle,pwm,unlock_param):
    """解錠を行うための関数
    Args:
        current_angle   (str) : 現在の鍵の角度
        pwm             (object): PWM制御を行うためのオブジェクト
        params          (dict): サーボモーターを動作させるためのパラメータ
    Return:
        status  (str): 現在の鍵の状態を示す文字列
    """

    if current_angle==str(unlock_param["angle"]):
        status = "Already unlocked."
    else:
        set_servo_angle(unlock_param,pwm)
        status = "Unlocking"
        
    return status, str(unlock_param["angle"])
    
    
def lock(current_angle,pwm,lock_param):
    """施錠を行うための関数
    Args:
        current_angle   (str) : 現在の鍵の角度
        pwm             (object): PWM制御を行うためのオブジェクト
        params          (dict): サーボモーターを動作させるためのパラメータ
    Return:
        status          (str): 現在の鍵の状態を示す文字列
    """
    if current_angle==str(lock_param["angle"]):
        status = "Already locked."
    else:
        set_servo_angle(lock_param,pwm)
        status = "Locking"
        
    return status, str(lock_param["angle"])

def other_order(current_angle,pwm,lock_param,msg,logger):
    """無効な指令が入力された場合の例外処理
    Args:
        current_angle   (str): 現在の鍵の角度
        pwm             (object): pwm制御を行うためのオブジェクト
        lock_param      ()
        
    Return:
        warn_msg  (str): 無効な指令が与えられたことに対する警告文
    """
    status, current_state = lock(current_angle,pwm,lock_param)
    
    logger.warning(f"無効なメッセージが入力されました。\n 内容：{msg}")
    
    return status, current_state, warn_msg
    
    


if __name__ == "__main__":
    with open('motor/motor_config.json', 'r') as f:
        params = json.load(f)
    args = sys.argv
    if args[1] =="neutral":
        neutral(params)
    else:
        order = "unlock"

        status = control(order,params)
        print(status)