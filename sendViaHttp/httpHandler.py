#!/usr/bin/python3.6

import http.client

class HttpHandler(object):

    def __init__(self):
        self.__headers = {'Content-type': 'application/json'}

    def SendData(self, serverAddress, apiExtension, json):
        try:
            connection = http.client.HTTPConnection(serverAddress, 80, 2)
            connection.request('POST', apiExtension, json, self.__headers)
            print("Send data via HTTP: OK")
        except Exception as ex:
            print("Send data via HTTP: NOK")
            print(ex)