from flask import Flask
from app.urls import bp
from flask_jwt_extended import JWTManager
from datetime import timedelta
from app.models import db, UserModel

# from flask_peewee.db import Database

# DATABASE = {
#     "name": "fava",
#     "engine": "peewee.MySQLDatabase",
#     "user": "root",
#     "host": "mysql",
#     "passwd": "toor333666",
# }
DEBUG = True
JWT_SECRET_KEY = "super-secret"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)

app = Flask(__name__)
app.config.from_object(__name__)

jwt = JWTManager(app)

# db = Database(app)


# @app.route("/hello")
# def hello():
#     return "world"


app.register_blueprint(bp)

db.create_tables([UserModel])
