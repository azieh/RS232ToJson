#!/usr/bin/python3.10

import asyncio
import socketio

from authorization.jwtHandler import JwtHandler

sio = socketio.AsyncClient(
    reconnection=True,
    reconnection_attempts=0,
    reconnection_delay=1,
    reconnection_delay_max=5,
    randomization_factor=0.5,)

@sio.on('check_remotes', namespace='remotes_control')
async def check_remotes():
    print('check remotes')

@sio.on('start', namespace='remotes_control')
async def start():
    print('message received with')
    ##await sio.emit('my response', {'response': 'my response'})

@sio.event('stop', namespace='remotes_control')
async def stop():
    print('disconnected from server')

async def main():
    await sio.connect('https://staging.sesja.pl/socket.io/?auth='+ JwtHandler.Generate(), namespaces='remotes_control')
    await sio.connect('https://staging.sesja.pl/socket.io/?auth='+ JwtHandler.Generate(), namespaces='remotes_response')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())