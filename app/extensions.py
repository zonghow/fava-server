import json
from flask import Response


def json_response(payload=None, code=200):
    response = Response(
        response=json.dumps(payload), status=code, mimetype="application/json"
    )
    return response


class FavaError(Exception):
    def __init__(self, message, code=400):
        super().__init__(message)
        self.code = code
        self.message = message
