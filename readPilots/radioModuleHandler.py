
from gpio import gpio
import time

class RadioModuleHandler(object):

    @staticmethod
    def __disconnectRadioModule():
        gpio.setup(174,'in')

    @staticmethod
    def __connectRadioModule():
        gpio.setup(174,'out')

    @staticmethod
    def RadioHardRestart():
        RadioModuleHandler.__disconnectRadioModule()
        time.sleep(10)
        RadioModuleHandler.__connectRadioModule()
        time.sleep(15)
        print("Hard restart of radio module has been done")
