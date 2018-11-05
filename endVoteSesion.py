#!/usr/bin/python3.6

from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from saveData.jsonHandler import JsonHandler
from sendViaHttp.httpHandler import HttpHandler
from helper import CommonSettings

import os
import time
print("End vote session")

pilotLogic = SesjaPilotsHandler()
pilotLogic.InitConnection()
pilotLogic.EndVoteSession()
pilotLogic.CloseStream()

print("Done")
