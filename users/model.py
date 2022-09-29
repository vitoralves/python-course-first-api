from db import db
from passlib.hash import pbkdf2_sha256


class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = pbkdf2_sha256.hash(password)

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }

    @classmethod
    def find_user_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
