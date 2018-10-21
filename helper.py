#!/usr/bin/python3.6
import datetime
#pip is required
#type
#!: wget https://bootstrap.pypa.io/get-pip.py
#!: sudo python3.6 get-pip.py
#program require serial library to install
#type 
#~: python3.6 -m pip install pyserial

class CommonSettings(object):
    
        WriteToJson    = False
        SendViaHttp    = True
        ServerAddress  = 'localhost' # or 'localhost' '192.168.0.232'
        ApiVoteExtension   = '/api/topics/vote-pilots'
        ApiBatteryExtension = '/api/topics/battery-pilots'
        ApiNewPilotsExtension = '/api/topics/new-pilots'

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
