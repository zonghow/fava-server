import peewee as pw
from werkzeug.security import generate_password_hash
from app.extensions import FavaError


db = pw.MySQLDatabase(
    "fava", user="root", password="toor333666", host="mysql", port=3306
)


class BaseModel(pw.Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    username = pw.CharField(unique=True)
    pw_hash = pw.TextField()

    @classmethod
    def signup(cls, username, password):
        if cls.select().where(cls.username == username):
            raise FavaError(message=f"用户{username}已存在", code=409)
        user = cls.create(
            username=username, pw_hash=generate_password_hash(password)
        )
        return user
