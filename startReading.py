#!/usr/bin/python3.6

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from readPilots.radioModuleHandler import RadioModuleHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import FileNameSettings, CommonSettings

import os
import time

print("Start")
__openCommunicationTry = 0

fileProperties  = FileNameSettings()
saveFileName    = fileProperties.GetFileName()
saveDirectory   = fileProperties.GetDirectoryName()
serverAddress = CommonSettings.ServerAddress
apiExtension  = CommonSettings.ApiVoteExtension

if(CommonSettings.WriteToJson):
    print('{0} {1}/{2}'.format("Data will be stored at:", saveDirectory, saveFileName))

if(CommonSettings.SendViaHttp):
    print('{0} {1}{2}'.format("Data will be send to:", serverAddress, apiExtension))

pilotLogic = SesjaPilotsHandler()
try:
    pilotLogic.InitConnection()
except:
    RadioModuleHandler.RadioHardRestart()
    pilotLogic.InitConnection()

while pilotLogic.isPilotsPrepared == False:
    pilotLogic.ClearPilots()
    __openCommunicationTry += __openCommunicationTry
    if __openCommunicationTry >= 10:
        RadioModuleHandler.RadioHardRestart()
        pilotLogic.InitConnection()
        __openCommunicationTry = 0

while True:
    pilotsData = list()
    pilotLogic.ReadPilots(pilotsData)
    
    if len(pilotsData) == 0:
        continue

    json = JsonHandler().ParseToJson(pilotsData)
    
    if CommonSettings.WriteToJson:
        JsonHandler().WriteVoteData(
            directoryName =  saveDirectory, 
            fileName = saveFileName, 
            json = json)

    if CommonSettings.SendViaHttp:
        HttpHandler().SendData(
            serverAddress = serverAddress,
            apiExtension = apiExtension,
            json = json)
