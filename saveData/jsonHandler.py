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

    def IsDifferenceWithPreviousVote(self, previousJson, newJson):
        if previousJson == "":
            return False
        
        a, b = json.loads(previousJson), json.loads(newJson)
        isTheSame = self.__compare(a, b)
        if not isTheSame:
            print(previousJson)
            print(newJson)
        return isTheSame

    def __compare(self, data_a, data_b):
        if (type(data_a) is list):
            if ((type(data_b) != list) or (len(data_a) != len(data_b))):
                return False

            for list_index,list_item in enumerate(data_a):
                if (not self.__compare(list_item,data_b[list_index])):
                    return False
            return True

        if (type(data_a) is dict):
            if (type(data_b) != dict):
                return False

            for dict_key,dict_value in data_a.items():
                if ((dict_key not in data_b) or (not self.__compare(dict_value,data_b[dict_key]))):
                    return False

            return True
        
        return (
			(data_a == data_b) and
			(type(data_a) is type(data_b))
		)