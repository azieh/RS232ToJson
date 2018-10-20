#!/usr/bin/python3.6
from readPilots.common.commands import Commands
from readPilots.model.pilotModel import PilotModel
from readPilots.model.pilotBatteryModel import PilotBatteryModel
import serial 
import json
import time

class SesjaPilotsHandler(object):

    __readedData = None
    __serialStream = None

    __separatorSize = 0
    isPilotsPrepared = False

    #COM Settings
    __portName = "/dev/ttyUSB0"
    __baudRate = 115200
    __data = serial.EIGHTBITS
    __parity = serial.PARITY_NONE
    __stopBits = serial.STOPBITS_ONE

    def __init__(self):
        self.__serialStream = serial.Serial(
            port = self.__portName,
            baudrate = self.__baudRate,
            parity = self.__parity,
            stopbits = self.__stopBits,
            bytesize = self.__data
        )
        if self.__serialStream.isOpen() == False:
            self.__serialStream.open()
        self.__serialStream.isOpen()

    def ClearPilots(self):
        response = b''
        self.__serialStream.write(Commands.CLEAR())
        time.sleep(1)
        while self.__serialStream.inWaiting() > 0:
            response += self.__serialStream.readline()
            
        if Commands.ISACK(response):
            self.isPilotsPrepared = True
            print("ClearPilots: OK")

    def ReadPilots(self, pilotsData):
        dataList = self.__readPilots(Commands.LIST())
        self.__separatorSize = 0
        self.__parseDataListIntoPilotModel(dataList, pilotsData, PilotModel)

    def ReadBatteryStatus(self, pilotsData):
        dataList = self.__readPilots(Commands.BATTERYSTATUS())
        self.__separatorSize = 3
        self.__parseDataListIntoPilotModel(dataList, pilotsData, PilotBatteryModel)

    def CloseStream(self):
        self.__serialStream.close()
        
    def __readPilots(self, command):
        dataList = list()
        self.__serialStream.write(command)
        time.sleep(1)
        while self.__serialStream.inWaiting() > 0:
            data = self.__serialStream.readline()
            dataList.append(data)

        if Commands.ISACK(dataList) == False:
            return list()

        self.__preparePilotsResponse(dataList)
        return dataList

    def __preparePilotsResponse(self, dataList):
        dataList.pop(0) # first data is useless
        count = len(dataList)
        #last 3 data are useless
        dataList.pop(count - 1)
        dataList.pop(count - 2)
        dataList.pop(count - 3)

    def __parseDataListIntoPilotModel(self, dataList, pilotsData, DataModel):
        parsedList = list()
        for data in dataList:
            stringData = str(data)
            separatorData = stringData.find(':')
            if separatorData < 0:
                continue

            name = data[0 : separatorData - 2].decode("utf-8")
            value = data[separatorData - 1 : separatorData + self.__separatorSize].decode("utf-8")
            parsedInt = int(name, 16)
            pilot = DataModel(str(parsedInt), "Pilot_" + str(parsedInt), str(value))

            parsedList.append(pilot)

        sortedData = sorted(parsedList, key=lambda pilotModel: pilotModel.Id)
        for data in sortedData:
            pilotsData.append(data)
