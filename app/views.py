from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from app import models as m


class SignupView(MethodView):
    def post(self):
        body = request.json
        username = body["username"]
        password = body["password"]
        user = m.UserModel.signup(username=username, password=password)
        return (
            jsonify(access_token=create_access_token(identity=user.username)),
            200,
        )


class LoginView(MethodView):
    def post(self):
        pass
