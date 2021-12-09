#!/usr/bin/python3.10

class Commands(object):

    @staticmethod
    def CLEAR():
        return 'CLR\r\n'.encode()

    @staticmethod
    def LIST():
        return 'LST\r\n'.encode()

    @staticmethod
    def BATTERYSTATUS():
        return 'BAT\r\n'.encode()

    @staticmethod
    def SCANFORPILOTS():
        return 'SCN\r\n'.encode()
    
    @staticmethod
    def PRINTPILOTLIST_RAM():
        return 'CLL\r\n'.encode()

    @staticmethod
    def DELETEPILOTBYNUMBER_RAM(pilotNumber):
        command = 'DEL={0}\r\n'.format(pilotNumber)
        return command.encode()
    
    @staticmethod
    def DELETEPILOTALL_RAM():
        return 'ACD\r\n'.encode()

    @staticmethod
    def SAVEALLPILOTS_EEPROM():
        return 'ACD\r\n'.encode()

    @staticmethod
    def ENDVOTE():
        return 'END\r\n'.encode()

    @staticmethod
    def PROGRAMPILOTRADIOCHANNEL(channelNumber):
        command = 'CHP={0}\r\n'.format(channelNumber)
        return command.encode()

    @staticmethod
    def PROGRAMCENTALRADIOCHANNEL(channelNumber):
        command = 'CHC={0}\r\n'.format(channelNumber)
        return command.encode()
    
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
