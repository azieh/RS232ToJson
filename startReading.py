#!/usr/bin/python3.6

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import FileNameSettings, CommonSettings

import os
import time

print("Start")

fileProperties  = FileNameSettings()
saveFileName    = fileProperties.GetFileName()
saveDirectory   = fileProperties.GetDirectoryName()
serverAddress = CommonSettings.ServerAddress
apiExtension  = CommonSettings.ApiExtension

if(CommonSettings.WriteToJson):
    print('{0} {1}/{2}'.format("Data will be stored at:", saveDirectory, saveFileName))

if(CommonSettings.SendViaHttp):
    print('{0} {1}{2}'.format("Data will be send to:", serverAddress, apiExtension))

pilotLogic      = SesjaPilotsHandler()

while pilotLogic.isPilotsPrepared == False:
    pilotLogic.ClearPilots()

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