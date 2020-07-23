from flask import Blueprint
from app import views as v
from app.extensions import FavaError
from app.extensions import json_response

bp = Blueprint("/", __name__)

bp.add_url_rule("/auth/signup", view_func=v.SignupView.as_view("auth_signup"))

bp.add_url_rule("/auth/login", view_func=v.LoginView.as_view("auth_login"))


@bp.errorhandler(FavaError)
def handle(error):
    return json_response(payload={"message": error.message}, code=error.code)
