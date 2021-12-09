import jwt
import os

class JwtHandler(object):

    @staticmethod
    def Generate():
        privateKey = open(os.path.abspath(os.path.dirname(__file__)) + "\privateKey.pem")
        encoded_jwt = jwt.encode({"some": "payload"}, privateKey.read(), algorithm="RS256")
        print(encoded_jwt)
        return encoded_jwt