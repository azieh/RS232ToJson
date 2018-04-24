#!/usr/bin/python3.6

class Commands(object):

    @staticmethod
    def CLEAR():
        return 'CLR\r\n'.encode()

    @staticmethod
    def LIST():
        return 'LST\r\n'.encode()
    
    @staticmethod
    def ISACK(response):
        if type(response) == bytes:
            return Commands.__ackHelper(response)

        if type(response)  == list:
            for data in response:
                if Commands.__ackHelper(data):
                    return True
            return False

    @staticmethod
    def __ackHelper(responseString):
        decodedResponse = responseString.decode('ascii')
        if "OK" in decodedResponse:
            return True
        else:
            return False
