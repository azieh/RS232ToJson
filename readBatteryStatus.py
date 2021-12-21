#!/usr/bin/python3.10

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import CommonSettings

print("Start reading battery status from pilots")
serverAddress = CommonSettings.ServerAddress
apiExtension  = CommonSettings.ApiBatteryExtension

pilotLogic = SesjaPilotsHandler()
pilotLogic.InitConnection()
pilotsData = list()
pilotLogic.ReadBatteryStatus(pilotsData)
json = JsonHandler().ParseToJson(pilotsData)
print(json)
HttpHandler().SendData(
            serverAddress = serverAddress,
            apiExtension = apiExtension,
            json = json)

print("Done")
