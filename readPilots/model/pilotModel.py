#!/usr/bin/python3.6
import json

class PilotModel(object):

    def __init__(self, id, name, vote):
            self.Id = int(id)
            self.PilotName = name
            self.Vote = vote
   

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def __repr__(self):
        return repr((self.Id, self.PilotName, self.Vote))