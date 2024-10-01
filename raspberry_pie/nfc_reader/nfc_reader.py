import os
import sys
from time import time as ti
import time
import ndef
import nfc
import requests
from logging import getLogger
from os.path import basename, splitext

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import set_logging

logger = getLogger(__name__)

NFC_READER_ID = "usb:054c:06c3" # Sony RC-S380は全てこのID. lsusbコマンドで確認可能.
SERVICE_CODE = 0x100B

class NFCReader:
    def on_connect(self, tag):
        logger.debug("Detected NFC Card")
        
    def read(self, wait_time:int) -> bool:
        clf = nfc.ContactlessFrontend(NFC_READER_ID)
        timeout = lambda: ti() - started > wait_time
        started = ti()
        logger.info("Waiting for NFC Card ...")
        if clf.connect(rdwr={"on-connect": self.on_connect}, terminate=timeout): # タッチされた時のみon_connectメソッドが発火
            return True
        else:
            logger.debug("NOT Detected NFC Card")
            return False

class UserCardReader(NFCReader):
    def on_connect(self, tag):
        logger.debug("Get user Number")
        sc = nfc.tag.tt3.ServiceCode(SERVICE_CODE >> 6, SERVICE_CODE & 0x3f)
        logger.debug("sc: "+ str(sc))
        bc = nfc.tag.tt3.BlockCode(0,service=0)
        logger.debug("bc: "+str(bc))
        self._user_id = tag.read_without_encryption([sc],[bc]).decode()[2:2+8]
        logger.debug(self._user_id)
        bc = nfc.tag.tt3.BlockCode(1)
        self._user_name = (
            tag.read_without_encryption([sc], [bc])
            .decode("shift-jis")
            .rstrip("\x00")
        )
        return super().on_connect(tag)
    
    def get_user_id(self):
        try:
            user_id = str(self._user_id)
            response = requests.post('http://localhost:5560/nfc_event', json = {"user_id":user_id})
            if response.status_code ==200:
                logger.info(f"Flask_server に通知しました")
            else:
                print(f"通知失敗： {response.status_code}")
        except Exception as e:
            logger.info(f"通知エラー: {e}")
        return self._user_id

    def get_user_name(self):
        return self._user_name
    
    def get_user_info(self):
        return self._user_id, self._user_name
    
if __name__=='__main__':
    log_file_name = splitext(basename(__file__))[0]
    set_logging('log',log_file_name, stdout_log_level = "DEBUG",)
    while True:
        nfc_reader = UserCardReader()
        if nfc_reader.read(wait_time=10):
            user_id = nfc_reader.get_user_id()
            logger.info(f'user ID is {user_id}')
            logger.info(f'user Name is {nfc_reader.get_user_name()}')
            time.sleep(10)

        else:
            logger.info("Not Detected NFC Card")
