from flask import Flask, request, jsonify
import os
import requests
import json
import time
import datetime
import sqlite3

from motor.motor_control import control
import utils

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.json') # config.json への相対パスを指定
motor_config_path = os.path.join(current_dir,"motor/motor_config.json")
txt_path = os.path.join(current_dir,"lock_status/servo_angle.txt") # 鍵の角度を保存するファイルへのパス
log_path = os.path.join(current_dir,"log/") # logファイルの出力先のpath を指定

with open(config_path) as f: 
    config = json.load(f)
external_server_url = config["external_server_url"]

motor_config =None
current_angle = None

logger = utils.set_logging(log_path, "HTTP_status")

def authentication(user_id):
    """読み取ったユーザーIDが登録済みかどうかを確認する関数
    Args:
        user_id (str): ユーザーID
    Return:
        auth    (str): 登録済みかどうか
    """
    logger.info("accessing database")
    try:
        db_path = os.path.join(current_dir,"users.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(1) FROM users WHERE username = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()

        if result[0] >0:
            auth = "accept"
        else:
            auth = "fail"
        return auth
    except Exception as e:
        logger.error(f"データベースへのアクセス失敗: {e}")
        auth = "fail"
        return auth

def load_motor_config():
    """モーターを動かすための設定ファイルを読み取り、パラメーターを保持
    """
    global motor_config
    try:
        with open(motor_config_path, "r") as f:
            motor_config = json.load(f)
        logger.info(str(motor_config))
    except:
        motor_config = None
    

def notify_external_server(message, status):
    """鍵の状態を外部の記録サーバーに通知する関数
    Args:
        message    (dict): アクションがあった時のメッセージ(id, 不正アクセスかどうか)
        status     (str) : 現在の鍵の状態
    """



    data = {
        "datetime": str(datetime.datetime.now()),
        "user_id": message["user_id"],
        "authentication":message["authentication"],
        "status":status
    }

    try:
        response = requests.post(f"{external_server_url}/log_status",json=data)
        if response.status_code==200:
            logger.info("現在の状態をサーバーに通知しました。")
        else:
            logger.info(f"サーバーへの通知に失敗しました : {response.status_code}")
        
    except Exception as e:
        logger.info(f"サーバーへの通知エラー : {str(e)}")

def toggle_motor(user_id,auth="fail"):
    """NFCリーダーがアクセスを受けた場合の処理
    Args:
        user_id (str): 登録されているID
        auth    (str): ユーザーIDが認証されたか
    """
    #auth = "accept" # データベースの設計が完了するまで仮で認証させる
    global motor_config
    global current_angle
    status = None
    logger.info(f"users status: {auth}")
    if motor_config is None:
        logger.error("モーターの設定ファイルへのアクセスに失敗")
        return jsonify({'status': 'error', 'message':'Do not load motor config.'}),500
    if auth == "accept":
        logger.info("ユーザーが認証されました")
        if current_angle == str(motor_config["lock"]["angle"]):
            status, current_angle = control("unlock",motor_config, current_angle)
        elif current_angle == str(motor_config["unlock"]["angle"]):
            status, current_angle = control("lock", motor_config, current_angle)
        else:
            status, current_angle = control("lock", motor_config, current_angle)
            
        with open(txt_path, "w") as f:
            f.write(current_angle)

    else: # 登録外のユーザーデータを読み取った場合の処理
        status = control("lock", motor_config, current_angle)
    
    message = {
        "user_id":user_id,
        "authentication":True
    }

    notify_external_server(message, status)
    return jsonify({'message':status})

@app.route('/http_motor', methods=['POST'])
def http_motor():
    """鍵を動作させるコマンドを実行するための関数
    Args:
        None
    """
    if motor_config is None:
        return jsonify({'status': 'error', 'message':'Do not load motor config.'}),500
    
    data = request.get_json()
    order = data.get('order') # "unlock" or "lock"
    user_id = data.get("user_id")
    status = control(order, motor_config)
    notify_external_server(user_id, status)
    return jsonify({'message':status})

@app.route('/nfc_event', methods=['POST'])
def nfc_event():
    global logger
    data = request.get_json()
    user_id = data.get("user_id")
    logger.info(f"User ID : {user_id}")
    auth = authentication(user_id)
    status = toggle_motor(user_id, auth)
    message = {
        "user_id":user_id,
        "authentication":True
    }
    notify_external_server(message, status)
    return jsonify({'message':str(status)})

if __name__=="__main__":
    load_motor_config()
    
    with open(txt_path, "r") as f:
        current_angle = f.read()
    
    app.run(host = '0.0.0.0', port =5560)