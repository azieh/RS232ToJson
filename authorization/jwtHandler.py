import jwt
import os

class JwtHandler(object):
    @staticmethod
    def Generate(location):
        slash = "/"
        if os.name == 'nt':
            slash = "\\"
        privateKey = open(os.path.abspath(os.path.dirname(__file__)) + slash + "privateKey.pem")
        encoded_jwt = jwt.encode({"location": location}, privateKey.read(), algorithm="RS256")
        return encoded_jwt