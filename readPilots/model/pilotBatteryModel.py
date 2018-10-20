#!/usr/bin/python3.6
import json

class PilotBatteryModel(object):

    def __init__(self, id, name, voltage):
            self.Id = int(id)
            self.PilotName = name
            self.BatteryVolts = voltage
   
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def __repr__(self):
        return repr((self.Id, self.PilotName, self.BatteryVolts))