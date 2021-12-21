#!/usr/bin/python3.10

import asyncio
from asyncio.events import AbstractEventLoop
from asyncio.tasks import Task
from time import sleep
import socketio

from authorization.jwtHandler import JwtHandler

sio = socketio.AsyncClient(
    reconnection=True,
    reconnection_attempts=0,
    reconnection_delay=1,
    reconnection_delay_max=5,
    randomization_factor=0.5,)

checkRemotesTask: Task
voteLoopTask: Task

async def srint():
    count = 1
    while True: 
        count += 1
        await asyncio.sleep(1)
        print('WorkWorkWork', count)

@sio.on('connect')
async def connect():
    print('Connection established')

@sio.on('remotes_control')
async def on_remotes_control(data):
    global checkRemotesTask
    if data == 'start_check_remotes':
        checkRemotesTask = asyncio.create_task(srint())
        return 'OK'
    if data == 'stop_check_remotes':
        checkRemotesTask.cancel()
        return 'OK'

@sio.on('*')
async def all(sid, data):
    print(sid)
    print(data)

async def main():
    await sio.connect('https://staging.sesja.pl/socket.io/?auth='+ JwtHandler.Generate())
    print("Url: ", sio.connection_url)
    print(sio.namespaces)
    
    await sio.emit("connected")
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())