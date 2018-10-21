#!/usr/bin/python3.6

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import CommonSettings

import os
import time

print("Start reading new pilots")
serverAddress = CommonSettings.ServerAddress
apiExtension  = CommonSettings.ApiNewPilotsExtension

pilotLogic = SesjaPilotsHandler()
pilotLogic.ClearPilots()
pilotLogic.ScanForPilotsInit()
while True:
    pilotsData = list()
    pilotLogic.ScanForPilotsLeasning(pilotsData)
    if not pilotsData:
        continue

    json = JsonHandler().ParseToJson(pilotsData)
    print(json)
    HttpHandler().SendData(
            serverAddress = serverAddress,
            apiExtension = apiExtension,
            json = json)
    time.sleep(1)
