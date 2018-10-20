#!/usr/bin/python3.6

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import CommonSettings

import os
import time
print("Start reading battery status from pilots")
serverAddress = CommonSettings.ServerAddress
apiExtension  = CommonSettings.ApiBatteryExtension

pilotLogic = SesjaPilotsHandler()
while pilotLogic.isPilotsPrepared == False:
    pilotLogic.ClearPilots()

pilotsData = list()
pilotLogic.ReadBatteryStatus(pilotsData)
json = JsonHandler().ParseToJson(pilotsData)
print(json)
HttpHandler().SendData(
            serverAddress = serverAddress,
            apiExtension = apiExtension,
            json = json)

print("Done")
