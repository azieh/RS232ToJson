import json

class JsonHandler(object):

    def WriteVoteData(self, directoryName, fileName, json):
        try:
            path = '{0}/{1}'.format(directoryName, fileName)
            with open(path, "w+") as voteData:
                voteData.write(json)
            print("Save data as JSON: OK")
        except Exception as ex:
            print("Save data as JSON: NOK")
            print(ex)
        

    def ParseToJson(self, pilotsData):
        jsonArray = []
        for data in pilotsData:
            jsonArray.append(str(data.toJSON()))

        json = "[%s]" % ",\n".join(jsonArray)

        return json