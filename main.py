#!/usr/bin/python3.10

from asyncio.tasks import Task
import asyncio
import socketio
from saveData.jsonHandler import JsonHandler
from readPilots.sesjaPilotsHandler import SesjaPilotsHandler
from readPilots.radioModuleHandler import RadioModuleHandler
from helper import FileNameSettings, CommonSettings
from authorization.jwtHandler import JwtHandler

serverAddress = CommonSettings.SocketIoServerAddress
authQueryString  = CommonSettings.SocketIoAuthQueryString
authLocation = CommonSettings.SocketIoAuthLocation

sio = socketio.AsyncClient(
    reconnection=True,
    reconnection_attempts=0,
    reconnection_delay=1,
    reconnection_delay_max=5,
    randomization_factor=0.5,)

pilotLogic: SesjaPilotsHandler
checkRemotesTask: Task = None
voteLoopTask: Task = None

async def ScanForPilots():
    print("Start reading new pilots")
    global pilotLogic
    pilotLogic = SesjaPilotsHandler()
    pilotLogic.InitConnection()
    pilotLogic.ClearPilotsJob()
    pilotLogic.ScanForPilotsInit()
    while True:
        pilotsData = list()
        await sio.sleep(0.1)
        pilotLogic.ScanForPilotsLeasning(pilotsData)
        if not pilotsData:
            continue

        json = JsonHandler().ParseToJson(pilotsData)
        print(json)
        await sio.emit('remotes_response', json)

async def EndScanForVotes():
    global pilotLogic
    pilotLogic.InitConnection()
    pilotLogic.EndVoteSession()
    pilotLogic.CloseStream()
    print("End scan for votes")

async def ScanForVotes():
    print("Start scan for votes")
    
    fileProperties  = FileNameSettings()
    saveFileName:str    = fileProperties.GetFileName()
    saveDirectory:str   = fileProperties.GetDirectoryName()
    resetRadioTimeout:int = CommonSettings.ResetRadioTimeout
    previousJson:str = ""

    if(CommonSettings.WriteToJson):
        print('{0} {1}/{2}'.format("Data will be stored at:", saveDirectory, saveFileName))
    
    global pilotLogic
    pilotLogic = SesjaPilotsHandler()
    try:
        pilotLogic.InitConnection()
    except:
        RadioModuleHandler.RadioHardRestart(resetRadioTimeout)
        pilotLogic.InitConnection()

    while pilotLogic.isPilotsPrepared == False:
        pilotLogic.ClearPilotsJob()
        if pilotLogic.isPilotsPrepared == False:
            RadioModuleHandler.RadioHardRestart(resetRadioTimeout)
            pilotLogic = SesjaPilotsHandler()
            pilotLogic.InitConnection()
    
    while True:
        pilotsData = list()
        pilotLogic.ReadPilots(pilotsData)

        if len(pilotsData) == 0:
            continue

        json = JsonHandler().ParseToJson(pilotsData)
        
        if not JsonHandler().IsDifferenceWithPreviousVote(previousJson, json):
            previousJson = json
            if CommonSettings.WriteToJson:
                JsonHandler().WriteVoteData(
                    directoryName =  saveDirectory,
                    fileName = saveFileName,
                    json = json)

            await sio.emit('remotes_response', json)
        await sio.sleep(0.1)

@sio.on('connect')
async def connect():
    print('Connection established')

@sio.on('remotes_control')
async def on_remotes_control(data):
    global checkRemotesTask
    global voteLoopTask
    if data == 'start_check_remotes':
        checkRemotesTask = sio.start_background_task(ScanForPilots)
        return "Ok"
    if data == 'start':
        voteLoopTask = sio.start_background_task(ScanForVotes)
        return "Ok"
    if data == 'stop' or data == 'stop_check_remotes':
        if checkRemotesTask is not None:
            checkRemotesTask.cancel()
        if voteLoopTask is not None:
            voteLoopTask.cancel()
        voteLoopTask = None
        checkRemotesTask = None
        sio.start_background_task(EndScanForVotes)
    
    print('Waiting for commands')
    await sio.wait()

@sio.on('*')
async def all(sid, data):
    print(sid)
    print(data)

async def main():
    await sio.connect(serverAddress + authQueryString + JwtHandler.Generate(authLocation))
    print("Url: ", sio.connection_url)

    await sio.emit("connected")
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())