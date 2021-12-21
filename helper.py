#!/usr/bin/python3.10
import datetime
#pip is required
#type
#!: wget https://bootstrap.pypa.io/get-pip.py
#!: sudo python get-pip.py
#program require serial library to install
#type 
#~: python -m pip install pyserial
#~: python -m pip install asyncio
#~: python -m pip install python-socketio
#~: python -m pip install PyJWT
#~: python -m pip install cryptography
#~: python -m pip install aiohttp

class CommonSettings(object):
    
        WriteToJson    = False
        SendViaHttp    = True
        ServerAddress  = 'localhost' # or 'localhost' '192.168.0.232'
        ApiVoteExtension   = '/api/topics/vote-pilots'
        ApiBatteryExtension = '/api/topics/battery-pilots'
        ApiNewPilotsExtension = '/api/topics/new-pilots'
        SocketIoServerAddress = 'https://staging.sesja.pl/socket.io/'
        SocketIoAuthQueryString = '?auth='
        SocketIoAuthLocation = 'Urzad_Nowy_Sacz_Czy_Cos'
        ResetRadioTimeout = 1

class FileNameSettings(object):

    __dateTimeFormat = "%Y%m%d_%H%M"

    def __init__(self):
        self.__fileName = "Glosowanie"
        self.__directoryName = "_sessionHistory"
        self.__sessionDateTime = datetime.datetime.now().strftime(self.__dateTimeFormat)

    def GetFileName(self):
        return '{0}_{1}.json'.format(self.__fileName, self.__sessionDateTime)
    
    def GetDirectoryName(self):
        return self.__directoryName

class Logger(object):
    @classmethod
    def Trace(self, methodName, time):
            print(f"___{methodName}: {time}[s]")
