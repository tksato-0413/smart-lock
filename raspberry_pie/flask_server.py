from flask import Flask, request, jsonify

import requests
import json
import time
import datetime
import sqlite3

from motor.motor_control import control
import utils

app = Flask(__name__)

with open("config.json") as f: 
    config = json.load(f)
external_server_url = config["external_server_url"]

motor_config =None
current_state = None

def authentication(user_id):
    """読み取ったユーザーIDが登録済みかどうかを確認する関数
    Args:
        user_id (str): ユーザーID
    Return:
        auth    (str): 登録済みかどうか
    """
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(1) FROM users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()

        if result[0] >0:
            auth = "accept"
            return auth
        else:
            auth = "fail"
            return auth
    except Exception as e:
        auth = "fail"
        return auth

def load_motor_config():
    """モーターを動かすための設定ファイルを読み取り、パラメーターを保持
    """
    global motor_config
    try:
        with open("motor/motor_config.json", "r") as f:
            motor_config = json.load(f)
    except:
        motor_config = None

def notify_external_server(message, status):
    """鍵の状態を外部の記録サーバーに通知する関数
    Args:
        message    (dict): アクションがあった時のメッセージ(id, 不正アクセスかどうか)
        status     (str) : 現在の鍵の状態
    """

    logger = utils.set_logging("log/", "HTTP_status")

    data = {
        "datetime": str(datetime.datetime.now()),
        "student_id": message["id"],
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
    global current_state
    if motor_config is None:
        return jsonify({'status': 'error', 'message':'Do not load motor config.'}),500
    if auth == "accept":
        if current_state == config["lock"]["angle"]:
            status = control("unlock",motor_config)
        elif current_state == config["unlock"]["angle"]:
            status = control("lock", motor_config)

    else: # 登録外のユーザーデータを読み取った場合の処理
        status = control("lock", motor_config)
    
    notify_external_server(user_id, status)
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
    data = request.json
    user_id = data.get("user_id")
    auth = authentication(user_id)
    status = toggle_motor(user_id, auth)
    notify_external_server(user_id, status)
    return jsonify({'message':status})

if __name__=="__main__":
    load_motor_config()
    with open("lock_status/servo_angle.txt", "r") as f:
        current_state = f.read()
    
    app.run(host = '0.0.0.0', port =556)