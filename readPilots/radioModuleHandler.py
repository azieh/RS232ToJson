
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
    def RadioHardRestart(timeout):
        RadioModuleHandler.__disconnectRadioModule()
        time.sleep(timeout)
        RadioModuleHandler.__connectRadioModule()
        time.sleep(timeout)
        print("Hard restart of radio module has been done")
