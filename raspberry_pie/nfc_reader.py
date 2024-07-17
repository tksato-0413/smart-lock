from time import time
from logging import getLogger
from os.path import basename, splitext

import nfc

from raspberry_pie.utils import set_logging

logger = getLogger(__name__)

NFC_READER_ID = "usb:054c:06c3" # Sony RC-S380は全てこのID. lsusbコマンドで確認可能.
SERVICE_CODE = 0x100B

class NFCReader:
    def on_connect(self, tag):
        logger.debug("Detected NFC Card")
        
    def read(self, wait_time:int) -> bool:
        clf = nfc.ContactlessFrontend(NFC_READER_ID)
        timeout = lambda: time() - started > wait_time
        started = time()
        logger.info("Waiting for NFC Card ...")
        if clf.connect(rdwr={"on-connect": self.on_connect}, terminate=timeout): # タッチされた時のみon_connectメソッドが発火
            return True
        else:
            logger.debug("NOT Detected NFC Card")
            return False

class StudentCardReader(NFCReader):
    def on_connect(self, tag):
        logger.debug("Get Student Number")
        sc = nfc.tag.tt3.ServiceCode(SERVICE_CODE >> 6, SERVICE_CODE & 0x3f)
        logger.debug("sc: "+ str(sc))
        bc = nfc.tag.tt3.BlockCode(0,service=0)
        logger.debug("bc: "+str(bc))
        self._student_id = tag.read_without_encryption([sc],[bc]).decode()[2:2+8]
        logger.debug(self._student_id)
        bc = nfc.tag.tt3.BlockCode(1)
        self._student_name = (
            tag.read_without_encryption([sc], [bc])
            .decode("shift-jis")
            .rstrip("\x00")
        )
        return super().on_connect(tag)
    
    def get_student_id(self):
        return self._student_id

    def get_student_name(self):
        return self._student_name
    
    def get_student_info(self):
        return self._student_id, self._student_name
    
if __name__=='__main__':
    log_file_name = splitext(basename(__file__))[0]
    set_logging('log',log_file_name, stdout_log_level = "DEBUG",)
    nfc_reader = StudentCardReader()
    if nfc_reader.read(wait_time=5):
        logger.info(f'Student ID is {nfc_reader.get_student_id()}')
        logger.info(f'Student Name is {nfc_reader.get_student_name()}')
    else:
        logger.info("Not Detected NFC Card")
