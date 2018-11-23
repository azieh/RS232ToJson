#!/usr/bin/python3.6
import time
import http.client
from helper import Logger

class HttpHandler(object):

    def __init__(self):
        self.__headers = {'Content-type': 'application/json'}

    def SendData(self, serverAddress, apiExtension, json):
        startTime = time.time()
        try:
            connection = http.client.HTTPConnection(serverAddress, 80, 2)
            connection.request('POST', apiExtension, json, self.__headers)
            print("Send data via HTTP: OK")
        except Exception as ex:
            print("Send data via HTTP: NOK")
            print(ex)
        stopTime = time.time()
        Logger.Trace("SendViaHttp", stopTime - startTime)