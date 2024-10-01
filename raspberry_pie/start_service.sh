#!/bin/bash

# Flask serverを起動
/home/comnets/smart-lock/raspberry_pie/venv/bin/python /home/comnets/smart-lock/raspberry_pie/flask_server.py &

# NFCリーダーを起動
/home/comnets/smart-lock/raspberry_pie/venv/bin/python /home/comnets/smart-lock/raspberry_pie/nfc_reader/nfc_reader.py &
